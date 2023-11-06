import unittest
import os
import pickle

import weather.configurator
import weather.path
import weather.pbp

def remove_if_there(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError:
        pass    

class TestPoweredByPickles(unittest.TestCase):
    def test_PoweredByPickles(self):
        # save some settings into a pickle
        cfg = weather.pbp.PoweredByPickles('test_PoweredByPickles')
        remove_if_there(cfg.filepath)
        keys = 'abcdef'
        for value, key in enumerate(keys):
            cfg[key] = value

        # load the pickle and check the settings
        with open(cfg.filepath, 'rb') as f:
            result = pickle.load(f)            
        for value, key in enumerate(keys):
            self.assertTrue(result[key] == value)
        remove_if_there(cfg.filepath)

        # can find expected key in cfg keys
        for key in keys:
            self.assertTrue(key in cfg)

        # can find cfg key in expected keys
        for key in cfg:
            self.assertTrue(key in keys)

class TestConfigurator(unittest.TestCase):
    def test_Configurator(self):
        # create config file with existing values
        fname = 'test_Configurator'
        pbp = weather.pbp.PoweredByPickles(fname)
        remove_if_there(pbp.filepath)
        keys = 'abcdef'
        for value, key in enumerate(keys):
            pbp[key] = value
        
        # test staging functionality        
        cfg = weather.configurator.Configurator(fname)
        self.assertFalse(cfg.modified)
        save_flag = cfg.save()
        self.assertEqual(save_flag, weather.configurator.NOT_MODIFIED)

        # stage some changes to existing keys
        cfg['b'] = -1
        cfg['c'] = -1
        cfg['e'] = -1
        cfg['f'] = -1
        self.assertTrue(cfg.modified)

        # revert some staged changes
        cfg.revert('e')
        cfg.revert('f')
        
        # add some new keys
        more_keys = 'ghijk'
        for value, key in enumerate(more_keys):
            cfg[key] = value + len(keys)

        # commit staged changes
        save_flag = cfg.save()
        self.assertEqual(save_flag, weather.configurator.SUCCESS)
        self.assertFalse(cfg.modified)

        # load pickle and check results
        with open(cfg.filepath, 'rb') as f:
            result = pickle.load(f)
        for value, key in enumerate(keys + more_keys):
            if key == 'b' or key == 'c':
                value = -1
            self.assertEqual(result[key], value)

        # start over
        remove_if_there(pbp.filepath)
        keys = 'abcdef'
        for value, key in enumerate(keys):
            pbp[key] = value
        cfg.reload()

        # stage some changes to existing keys
        cfg['b'] = -1
        cfg['c'] = -1
        cfg['e'] = -1
        cfg['f'] = -1
        self.assertEqual(cfg._modified, 4)
        
        # revert all changes
        cfg.revert()
        cfg.save()

        # load pickle and check results
        with open(cfg.filepath, 'rb') as f:
            result = pickle.load(f)
        for value, key in enumerate(keys):
            self.assertEqual(result[key], value)


        remove_if_there(cfg.filepath)
        
class TestDefaultSetter(unittest.TestCase):
    def test_DefaultSetter(self):
        # create some existing config settings
        fname = 'test_DefaultSetter'
        pbp = weather.pbp.PoweredByPickles(fname)
        remove_if_there(pbp.filepath)
        keys = 'abcdef'
        for value, key in enumerate(keys):
            pbp[key] = value

        # set "default" values for keys not present
        more_keys = 'ghijk'
        cfg = weather.configurator.DefaultSetter(fname)
        for value, key in enumerate(keys + more_keys):
            cfg[key] = value + 10
        self.assertTrue(cfg.modified)

        # commit changes and load pickle
        save_flag = cfg.save()
        self.assertEqual(save_flag, weather.configurator.SUCCESS)
        with open(cfg.filepath, 'rb') as f:
            result = pickle.load(f)

        # existing keys should be untouched by DefaultSetter
        for value, key in enumerate(keys + more_keys):
            if value > len(keys) - 1: value += 10
            self.assertEqual(result[key], value)
            
        
        remove_if_there(cfg.filepath)

if __name__ == '__main__':
    unittest.main()
