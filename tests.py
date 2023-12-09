# tests.py

import unittest
import os
import pickle
import random

import weather.configurator
import weather.path
import weather.pbp
import weather.timer
import weather.geocoder
import weather.forecast

EXISTING_VALUE = 0
NEW_VALUE = -1
ONE_SECOND = weather.timer.ONE_SECOND

# skip tests that involve sleep commands
SKIP_TIMELY_TESTS = True


def remove_if_there(filepath):
    """Try to remove a file; if it's not there, we don't care."""
    try:
        os.remove(filepath)
    except FileNotFoundError:
        pass
    
def pickler(n, fname):
    """Create a PBP instance for testing. Adds some arbitrary
    key/values. Returns the PBP instance, the keys, some keys that
    haven't been used yet, and the values of the keys."""
    pbp = weather.pbp.PoweredByPickles(fname)
    weather.pbp.destroy_pickle(pbp)
    keys = [i for i in range(n)]
    new_keys = [i + 2*n for i in range(n)]
    values = [i for i in range(n)]
    for value, key in zip(values, keys):
        # save key-value pair to pickle
        pbp[key] = value
    assert(NEW_VALUE not in values)
    assert(EXISTING_VALUE in values)
    return pbp, keys, new_keys, values


cities = ['Akron', 'Cincinnati', 'Cleveland', 'Columbus',
          'Dayton', 'Marietta', 'Toledo']

def get_a_place(city=None, place=weather.geocoder.Place):
    if city is None:
        city = random.choice(cities)
    return place(city=city, state='Ohio')


class TestPoweredByPickles(unittest.TestCase):
    def setUp(self):
        """Create a PBP instance and load it with some values."""
        fname = 'test_PoweredByPickles'
        self.pbp, self.keys, _, self.values = pickler(10, fname)
    
    def tearDown(self):
        """Remove PBP's pickle file if it's there."""
        weather.pbp.destroy_pickle(self.pbp)

    def test_pickle_directly(self):
        """Load the PBP's pickle directly and make sure it contains
        what it should contain."""
        with open(self.pbp.filepath, 'rb') as f:
            result = pickle.load(f)            
        for value, key in zip(self.values, self.keys):
            self.assertEqual(result[key], value)

    def test_all_expected_keys_in_pbp(self):
        """We can find all the keys we expect to find in the PBP
        instance."""
        for key in self.keys:
            self.assertTrue(key in self.pbp)

    def test_pickle_keys_against_expected(self):
        """Make sure there are no unexpected keys in the PBP
        instance."""
        for key in self.pbp:
            self.assertTrue(key in self.keys)


class TestSetting(unittest.TestCase):    
    def s(self, existing_value=None):
        return weather.configurator.Setting(existing_value)
    
    def test_new_setting_not_staged(self):
        """A new setting without a value is not staged."""
        s = self.s()
        self.assertFalse(s.staged)
        self.assertEqual(s.value, weather.configurator.NO_VALUE)

    def test_new_setting_staged(self):
        """If we assign a value to a new setting, `value` has the new
        value, `saved_value` is None, and the setting is staged."""
        s = self.s()
        s.value = NEW_VALUE
        self.assertEqual(s.value, NEW_VALUE)
        self.assertEqual(s.saved_value, weather.configurator.NO_VALUE)
        self.assertTrue(s.staged)

    def test_new_setting_reverted(self):
        """If we assign a value to a new setting and then revert it,
        `value` is None, `saved_value` is None, and the setting is not
        staged."""
        s = self.s()
        s.value = NEW_VALUE
        s.revert()
        self.assertEqual(s.value, weather.configurator.NO_VALUE)
        self.assertEqual(s.saved_value, weather.configurator.NO_VALUE)
        self.assertFalse(s.staged)
        
    def test_with_existing_value(self):
        """A setting created with an existing value; `value` and
        `saved_value` are equal to the provided existing value and the
        setting is not staged."""
        s = self.s(EXISTING_VALUE)
        self.assertEqual(s.value, EXISTING_VALUE)
        self.assertEqual(s.saved_value, EXISTING_VALUE)
        self.assertFalse(s.staged)
       
    def test_change_from_existing_value(self):
        """If we change the value of a setting created with an
        existing value, `value` has the new value, `saved_value` has
        the existing value, and the setting is staged."""
        s = self.s(EXISTING_VALUE)
        s.value = NEW_VALUE
        self.assertEqual(s.value, NEW_VALUE)
        self.assertEqual(s.saved_value, EXISTING_VALUE)
        self.assertTrue(s.staged)

    def test_commit_from_existing_value(self):
        """If we commit a change to the value of a setting created
        with an existing value, `value` has the new value,
        `saved_value` has the new value, and the setting is no longer
        staged."""
        s = self.s(EXISTING_VALUE)
        s.value = NEW_VALUE
        s.commit()
        self.assertEqual(s.value, NEW_VALUE)
        self.assertEqual(s.saved_value, NEW_VALUE)
        self.assertFalse(s.staged)

    def test_revert_from_existing_value(self):
        """If we revert a change to the value of a setting created
        with an existing value, `value` has the original value,
        `saved_value` has the original value, and the setting is no
        longer staged."""
        s = self.s(EXISTING_VALUE)
        s.value = NEW_VALUE
        s.revert()
        self.assertEqual(s.value, EXISTING_VALUE)
        self.assertEqual(s.saved_value, EXISTING_VALUE)
        self.assertFalse(s.staged)


class TestConfigurator(unittest.TestCase):
    def random_keys(self, n):
        """Returns a list of `n` number of keys from self.keys
        list. Keys are chosen and ordered pseudorandomly."""
        if n > len(self.keys):
            raise Exception("Not enough keys.")
        keys = list()
        while len(keys) < n:
            keys.append(random.choice(self.keys))
        return keys
    
    def setUp(self):
        """Create a config file with existing values."""
        # create an existing config file with some values
        fname = 'test_Configurator'
        self.pbp, self.keys, self.new_keys,\
            self.values = pickler(10, fname)

        # create Configurator to operate on existing config file
        self.cfg = weather.configurator.Configurator(fname)

    def tearDown(self):
        """Remove PBP's pickle file if it's there."""
        weather.pbp.destroy_pickle(self.pbp)

    def test_not_modified(self):
        """Configurator reports correctly that there have been no
        modifications staged."""
        self.assertFalse(self.cfg.modified)

    def test_save_not_modified(self):
        """An unmodified Configurator produces NOT_MODIFIED flag when
        told to save."""
        flag = self.cfg.save()
        self.assertEqual(flag, weather.configurator.NOT_MODIFIED)
        
    def test_modified(self):
        """Configurator reports correctly that there have been
        modifications staged."""
        for i, key in enumerate(self.keys):
            self.cfg[key] = NEW_VALUE
            self.assertEqual(self.cfg.modification_count, i+1)
        self.assertTrue(self.cfg.modified)

    def test_modified_newkey(self):
        """Configurator reports correctly that there have been
        modifications staged after adding a new key."""
        for i, key in enumerate(self.new_keys):
            self.cfg[key] = NEW_VALUE
            self.assertEqual(self.cfg.modification_count, i+1)
        self.assertTrue(self.cfg.modified)

    def test_save_flag_success(self):
        """A modified Configurator produces SUCCESS flag when told to
        save."""
        for key in self.keys:
            self.cfg[key] = NEW_VALUE
            flag = self.cfg.save()
            self.assertEqual(flag, weather.configurator.SUCCESS)

    def test_save_flag_not_modified(self):
        """Setting keys to their current value does not trigger
        modification and saving produces a NOT_MODIFIED flag."""
        for i, key in enumerate(self.keys):
            self.cfg[key] = self.values[i]
            self.assertFalse(self.cfg.modified)
            flag = self.cfg.save()
            self.assertEqual(flag, weather.configurator.NOT_MODIFIED)

    def test_revert_modified(self):
        """Reverting all staged changes causes Configurator to no
        longer be modified."""
        for key in self.keys:
            self.cfg[key] = NEW_VALUE
            self.cfg.revert(key)
            self.assertFalse(self.cfg.modified)

    def test_newkey_in_Cfg(self):
        """A new key is seen as a member of the Configurator."""
        new_key = random.choice(self.new_keys)
        self.cfg[new_key] = NEW_VALUE
        self.assertTrue(new_key in self.cfg)

    def test_reverted_newkey_not_in_Cfg(self):
        """A reverted new key is not a member of the Configurator."""
        new_key = random.choice(self.new_keys)
        self.cfg[new_key] = NEW_VALUE
        self.cfg.revert(new_key)
        self.assertFalse(new_key in self.cfg)
        
    def test_newkey_makes_modified(self):
        """Adding a new key should make make Configurator modified."""
        new_key = random.choice(self.new_keys)
        self.cfg[new_key] = NEW_VALUE
        self.assertTrue(self.cfg.modified)

    def test_revert_newkey_makes_unmodified(self):
        """Reverting the addition of new keys should make make
        Configurator not modified."""
        for key in self.new_keys:
            self.cfg[key] = NEW_VALUE
        for key in self.new_keys:            
            self.cfg.revert(key)
        self.assertFalse(self.cfg.modified)
        
    def test_unmodified_after_save(self):
        """A Configurator reports as unmodified after saving staged
        changes."""
        key = random.choice(self.keys)
        self.cfg[key] = NEW_VALUE
        self.cfg.save()
        self.assertFalse(self.cfg.modified)

    def test_newkey_is_saved(self):
        new_key = random.choice(self.new_keys)
        self.cfg[new_key] = NEW_VALUE
        flag = self.cfg.save()
        self.assertEqual(flag, weather.configurator.SUCCESS)


class TestDefaultSetter(unittest.TestCase):
    def setUp(self):
        """Create a config file with existing values."""
        fname = 'test_DefaultSetter'
        self.pbp, self.keys, self.new_keys,\
            self.values = pickler(10, fname)

        # create DefaultSetter to operate on existing config file
        self.cfg = weather.configurator.DefaultSetter(fname)

    def tearDown(self):
        """Remove PBP's pickle file if it's there."""
        weather.pbp.destroy_pickle(self.pbp)
        
    def test_dont_override_existing(self):
        """DefaultSetter does not save over existing settings."""
        for value, key in zip(self.values, self.keys):
            self.cfg[key] = NEW_VALUE
        self.cfg.save()
        for value, key in zip(self.values, self.keys):
            self.assertEqual(self.cfg[key], value)

    def test_do_save_new_settings(self):
        """DefaultSetter DOES add new settings when needed."""
        for value, key in zip(self.values, self.new_keys):
            self.cfg[key] = value
        self.cfg.save()            
        for value, key in zip(self.values, self.keys):
            self.assertEqual(self.cfg[key], value)

            
@unittest.skipIf(SKIP_TIMELY_TESTS, "Skipping timely tests.")
class TestWeatherTimer(unittest.TestCase):
    def setUp(self):
        self.fpath = weather.path.data_file('test_timer.txt')

    def tearDown(self):
        remove_if_there(self.fpath)
    
    def make_file(self):
        """Create a file that contains a timestamp of when it was
        created."""
        with open(self.fpath, 'w') as f:
            f.write(str(weather.timer.current_time()))

    def read_file(self):
        """Return the timestamp of when the file was created."""
        with open(self.fpath, 'r') as f:
            return int(f.read())

    def wait_a_couple_seconds(self):
        """Sleep for 2 seconds."""
        for i in range(2):
            weather.timer.wait_a_sec()
            
    def test_timely_resource(self):
        """Testing get_timely_resource function. Create a file that
        contains a timestamp, give it a couple seconds to go stale,
        and then try to get it. Function should create a new one with
        a more recent timestamp."""
        self.make_file()
        t0 = self.read_file()
        self.wait_a_couple_seconds()
        t1 = weather.timer.get_timely_resource(
            self.fpath, self.make_file, self.read_file, stale=ONE_SECOND)
        self.assertGreaterEqual(t1 - t0, 2)
        
    def test_timely_object(self):
        """Make sure TimelyObject knows if it is stale or not."""
        t = weather.timer.TimelyObject(ONE_SECOND)
        self.assertFalse(t.stale)
        self.wait_a_couple_seconds()
        self.assertTrue(t.stale)

    def test_api_governor(self):
        """Make sure ApiGovernor is throttling API calls."""
        a = weather.timer.ApiGovernor(None)
        a._get_fn = lambda x: weather.timer.current_time()
        trials = 5
        times = [a.get(None) for t in range(trials)]
        for i in range(trials - 1):
            self.assertEqual(times[i+1] - times[i], ONE_SECOND)

    def test_timer_functions(self):
        t0 = weather.timer.current_time()
        weather.timer.wait_a_sec()
        t1 = weather.timer.seconds_since(t0)
        self.assertEqual(t1, ONE_SECOND)

        
class TestGeocodedPlace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbname = 'test_known_places'

    def tearDown(self):
        dbname = TestGeocodedPlace.dbname
        db = weather.geocoder.KnownPlaces(dbname)
        weather.pbp.destroy_pickle(db)

    def Place(self, **kwargs):
        dbname = TestGeocodedPlace.dbname
        return weather.geocoder.Place(dbname=dbname, **kwargs)

    def test_place(self):
        p = self.Place(city='Cleveland', state='Ohio')
        self.assertEqual(41.4996562, float(p.lat))
        self.assertEqual(-81.6936813, float(p.lon))

    def test_placenotfound(self):
        with self.assertRaises(weather.geocoder.PlaceNotFound):
            p = self.Place(city='NO-SUCH-PLACE', state='ERROR')


class TestGeography(unittest.TestCase):
    def Place(self, city):
        return weather.geocoder.Place(city=city, state='OH')
    
    def test_haversine_distance(self):
        """Make sure we get pretty close with this function."""
        p0, p1 = self.Place('Cleveland'), self.Place('Columbus')
        exp = 203350 # value from vcalc.com
        obs = weather.geography.haversine_distance(p0, p1)
        mag = 10**6
        self.assertAlmostEqual(exp/mag, obs/mag, 5)


class TestForecast(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.place = get_a_place()
    
    def setUp(self):
        self.place = TestForecast.place
        dbname = 'test_forecast_store'
        self.db = weather.forecast.ForecastStore(dbname)
        weather.pbp.destroy_pickle(self.db)
        
    def tearDown(self):
        weather.pbp.destroy_pickle(self.db)

    def test_forecast_keying(self):
        f = weather.forecast.Forecast(self.place, self.db)
        key = weather.forecast.point_to_forecast_key(self.place)
        self.assertEqual(f.key, key)

    def test_add_forecast(self):        
        self.db.add(self.place)
        self.assertTrue(self.place in self.db)

    def test_retrieve_forecast(self):
        self.db.add(self.place)
        forecast = self.db[self.place]
        forecast_t = weather.forecast.Forecast
        self.assertTrue(isinstance(forecast, forecast_t))

    def test_forecast_items(self):
        f = self.db.add(self.place)
        fid_t = weather.forecast.ForecastItemData
        for itm in ['index', 'hourly', 'daily']:
            self.assertTrue(isinstance(f[itm], fid_t))
            self.assertFalse(f[itm].stale)

    def test_hourly_forecast(self):
        f = self.db.add(self.place)
        self.assertEqual(len(f.hourly), 24)


class TestHourForecast(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.place = get_a_place()
        cls.db = weather.forecast.ForecastStore('test_forecast_store')
        cls.forecast = cls.db.add(cls.place)

    @classmethod
    def tearDownClass(cls):
        weather.pbp.destroy_pickle(cls.db)
        
    def setUp(self):
        self.forecast = TestHourForecast.forecast

    def test_HourForecast_t(self):
        h  = self.forecast.hourly[0]
        self.assertTrue(isinstance(h, weather.forecast.HourForecast))

    def test_ForecastTimestamp(self):
        h  = self.forecast.hourly[0]
        s, e = h.start_time, h.end_time
        ts_t = weather.forecast.ForecastTimestamp
        self.assertTrue(isinstance(s, ts_t))
        self.assertTrue(isinstance(e, ts_t))        

    def test_temperature(self):
        hourly_forecast = self.forecast.hourly
        to_c = lambda f: round((f - 32) * (5/9), 1)
        mag = 10**3
        for h in hourly_forecast:
            c, f = float(h.temp_c), float(h.temp_f)
            self.assertAlmostEqual(to_c(f)/mag, c/mag, 4)

    def test_weather(self):
        h  = self.forecast.hourly[0]
        self.assertTrue(isinstance(h.weather, str))
        
        
        

if __name__ == '__main__':
    unittest.main()
