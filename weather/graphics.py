from . import path

weather_icons = {
    "Fair": {
        "day": "skc",
        "night": "nskc",
        "qualifier": ""
    },
    "Clear": {
        "day": "skc",
        "night": "nskc",
        "qualifier": ""
    },
    "Fair with Haze": {
        "day": "skc",
        "night": "nskc",
        "qualifier": ""
    },
    "Clear with Haze": {
        "day": "skc",
        "night": "nskc",
        "qualifier": ""
    },
    "Fair and Breezy": {
        "day": "skc",
        "night": "nskc",
        "qualifier": ""
    },
    "Clear and Breezy": {
        "day": "skc",
        "night": "nskc",
        "qualifier": ""
    },
    "A Few Clouds": {
        "day": "few",
        "night": "nfew",
        "qualifier": ""
    },
    "A Few Clouds with Haze": {
        "day": "few",
        "night": "nfew",
        "qualifier": ""
    },
    "A Few Clouds and Breezy": {
        "day": "few",
        "night": "nfew",
        "qualifier": ""
    },
    "Partly Cloudy": {
        "day": "sct",
        "night": "nsct",
        "qualifier": ""
    },
    "Partly Cloudy with Haze": {
        "day": "sct",
        "night": "nsct",
        "qualifier": ""
    },
    "Partly Cloudy and Breezy": {
        "day": "sct",
        "night": "nsct",
        "qualifier": ""
    },
    "Mostly Cloudy": {
        "day": "bkn",
        "night": "bkn",
        "qualifier": ""
    },
    "Mostly Cloudy with Haze": {
        "day": "bkn",
        "night": "bkn",
        "qualifier": ""
    },
    "Mostly Cloudy and Breezy": {
        "day": "bkn",
        "night": "bkn",
        "qualifier": ""
    },
    "Overcast": {
        "day": "ovc",
        "night": "novc",
        "qualifier": ""
    },
    "Overcast with Haze": {
        "day": "ovc",
        "night": "novc",
        "qualifier": ""
    },
    "Overcast and Breezy": {
        "day": "ovc",
        "night": "novc",
        "qualifier": ""
    },
    "Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Showers": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow Showers": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Snow Showers": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Showers Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Showers Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Showers Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Snow Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Showers Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow Showers Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Snow Showers Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Showers Snow Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Showers Snow Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Showers Snow Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Fog": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow Fog": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Snow Fog": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Showers Fog": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow Showers Fog": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Snow Showers Fog": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Showers in Vicinity Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Showers in Vicinity": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Showers in Vicinity Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Showers in Vicinity Fog": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Low Drifting Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Blowing Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Low Drifting Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Blowing Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow Low Drifting Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow Blowing Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow Blowing Snow Fog/Mist": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Snow Low Drifting Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Snow Blowing Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Thunderstorm Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Thunderstorm Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Thunderstorm Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Snow Grains": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Light Snow Grains": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Snow Grains": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Heavy Blowing Snow": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Blowing Snow in Vicinity": {
        "day": "sn",
        "night": "nsn",
        "qualifier": ""
    },
    "Rain Snow": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Light Rain Snow": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Heavy Rain Snow": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Snow Rain": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Light Snow Rain": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Heavy Snow Rain": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Drizzle Snow": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Light Drizzle Snow": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Heavy Drizzle Snow": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Snow Drizzle": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Light Snow Drizzle": {
        "day": "ra_sn",
        "night": "nra_sn",
        "qualifier": ""
    },
    "Rain Ice Pellets": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Light Rain Ice Pellets": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Heavy Rain Ice Pellets": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Drizzle Ice Pellets": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Light Drizzle Ice Pellets": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Heavy Drizzle Ice Pellets": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Ice Pellets Rain": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Light Ice Pellets Rain": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Heavy Ice Pellets Rain": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Ice Pellets Drizzle": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Light Ice Pellets Drizzle": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Heavy Ice Pellets Drizzle": {
        "day": "raip",
        "night": "nraip",
        "qualifier": ""
    },
    "Freezing Rain": {
        "day": "fzra",
        "night": "fzra",
        "qualifier": ""
    },
    "Freezing Drizzle": {
        "day": "fzra",
        "night": "fzra",
        "qualifier": ""
    },
    "Light Freezing Rain": {
        "day": "fzra",
        "night": "fzra",
        "qualifier": ""
    },
    "Light Freezing Drizzle": {
        "day": "fzra",
        "night": "fzra",
        "qualifier": ""
    },
    "Heavy Freezing Rain": {
        "day": "fzra",
        "night": "fzra",
        "qualifier": ""
    },
    "Heavy Freezing Drizzle": {
        "day": "fzra",
        "night": "fzra",
        "qualifier": ""
    },
    "Freezing Rain in Vicinity": {
        "day": "fzra",
        "night": "fzra",
        "qualifier": ""
    },
    "Freezing Drizzle in Vicinity": {
        "day": "fzra",
        "night": "fzra",
        "qualifier": ""
    },
    "Freezing Rain Rain": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Light Freezing Rain Rain": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Heavy Freezing Rain Rain": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Rain Freezing Rain": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Light Rain Freezing Rain": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Heavy Rain Freezing Rain": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Freezing Drizzle Rain": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Light Freezing Drizzle Rain": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Heavy Freezing Drizzle Rain": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Rain Freezing Drizzle": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Light Rain Freezing Drizzle": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Heavy Rain Freezing Drizzle": {
        "day": "ra_fzra",
        "night": "nra_fzra",
        "qualifier": ""
    },
    "Freezing Rain Snow": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Light Freezing Rain Snow": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Heavy Freezing Rain Snow": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Freezing Drizzle Snow": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Light Freezing Drizzle Snow": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Heavy Freezing Drizzle Snow": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Snow Freezing Rain": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Light Snow Freezing Rain": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Heavy Snow Freezing Rain": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Snow Freezing Drizzle": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Light Snow Freezing Drizzle": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Heavy Snow Freezing Drizzle": {
        "day": "fzra_sn",
        "night": "nfzra_sn",
        "qualifier": ""
    },
    "Ice Pellets": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Light Ice Pellets": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Heavy Ice Pellets": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Ice Pellets in Vicinity": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Showers Ice Pellets": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Thunderstorm Ice Pellets": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Ice Crystals": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Hail": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Small Hail/Snow Pellets": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Light Small Hail/Snow Pellets": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Heavy small Hail/Snow Pellets": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Showers Hail": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Hail Showers": {
        "day": "ip",
        "night": "nip",
        "qualifier": ""
    },
    "Snow Ice Pellets": {
        "day": "snip",
        "night": "nsnip",
        "qualifier": ""
    },
    "Light Rain": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Drizzle": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Light Drizzle": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Heavy Drizzle": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Light Rain Fog/Mist": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Drizzle Fog/Mist": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Light Drizzle Fog/Mist": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Heavy Drizzle Fog/Mist": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Light Rain Fog": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Drizzle Fog": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Light Drizzle Fog": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Heavy Drizzle Fog": {
        "day": "minus_ra",
        "night": "nra",
        "qualifier": ""
    },
    "Rain": {
        "day": "ra",
        "night": "ra",
        "qualifier": ""
    },
    "Heavy Rain": {
        "day": "ra",
        "night": "ra",
        "qualifier": ""
    },
    "Rain Fog/Mist": {
        "day": "ra",
        "night": "ra",
        "qualifier": ""
    },
    "Heavy Rain Fog/Mist": {
        "day": "ra",
        "night": "ra",
        "qualifier": ""
    },
    "Rain Fog": {
        "day": "ra",
        "night": "ra",
        "qualifier": ""
    },
    "Heavy Rain Fog": {
        "day": "ra",
        "night": "ra",
        "qualifier": ""
    },
    "Rain Showers": {
        "day": "shra",
        "night": "nshra",
        "qualifier": "(w/cloud cover > 60%)"
    },
    "Light Rain Showers": {
        "day": "shra",
        "night": "nshra",
        "qualifier": "(w/cloud cover > 60%)"
    },
    "Light Rain and Breezy": {
        "day": "shra",
        "night": "nshra",
        "qualifier": "(w/cloud cover > 60%)"
    },
    "Heavy Rain Showers": {
        "day": "shra",
        "night": "nshra",
        "qualifier": "(w/cloud cover > 60%)"
    },
    "Rain Showers in Vicinity": {
        "day": "shra",
        "night": "nshra",
        "qualifier": "(w/cloud cover > 60%)"
    },
    "Light Showers Rain": {
        "day": "shra",
        "night": "nshra",
        "qualifier": "(w/cloud cover > 60%)"
    },
    "Heavy Showers Rain": {
        "day": "shra",
        "night": "nshra",
        "qualifier": "(w/cloud cover > 60%)"
    },
    "Showers Rain": {
        "day": "shra",
        "night": "nshra",
        "qualifier": "(w/cloud cover > 60%)"
    },
    "Thunderstorm": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Rain": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Light Thunderstorm Rain": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Rain Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Light Thunderstorm Rain Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain Fog and Windy": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Showers in Vicinity": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Light Thunderstorm Rain Haze": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain Haze": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Light Thunderstorm Rain Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Light Rain": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Heavy Rain": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Light Rain Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Heavy Rain Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm in Vicinity Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm in Vicinity Haze": {
        "day": "hi_tsra",
        "night": "hi_ntsra",
        "qualifier": "(Cloud cover < 60%)"
    },
    "Thunderstorm Haze in Vicinity": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Light Rain Haze": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Heavy Rain Haze": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Light Rain Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Heavy Rain Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Hail": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Light Thunderstorm Rain Hail": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain Hail": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Rain Hail Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Light Thunderstorm Rain Hail Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain Hail Fog/Hail": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Showers in Vicinity Hail": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Light Thunderstorm Rain Hail Haze": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain Hail Haze": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Hail Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Light Thunderstorm Rain Hail Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain Hail Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Light Rain Hail": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Heavy Rain Hail": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Light Rain Hail Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Heavy Rain Hail Fog/Mist": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm in Vicinity Hail": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm in Vicinity Hail Haze": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Haze in Vicinity Hail": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Light Rain Hail Haze": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Heavy Rain Hail Haze": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Light Rain Hail Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Heavy Rain Hail Fog": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Small Hail/Snow Pellets": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm Rain Small Hail/Snow Pellets": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Light Thunderstorm Rain Small Hail/Snow Pellets": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Heavy Thunderstorm Rain Small Hail/Snow Pellets": {
        "day": "tsra",
        "night": "ntsra",
        "qualifier": "(w/cloud cover > 75%)"
    },
    "Thunderstorm in Vicinity": {
        "day": "hi_tsra",
        "night": "hi_ntsra",
        "qualifier": "(Cloud cover < 60%)"
    },
    "Thunderstorm in Vicinity Fog": {
        "day": "hi_tsra",
        "night": "hi_ntsra",
        "qualifier": "(Cloud cover < 60%)"
    },
    "Funnel Cloud": {
        "day": "fc",
        "night": "nfc",
        "qualifier": ""
    },
    "Funnel Cloud in Vicinity": {
        "day": "fc",
        "night": "nfc",
        "qualifier": ""
    },
    "Tornado/Water Spout": {
        "day": "fc",
        "night": "nfc",
        "qualifier": ""
    },
    "Tornado": {
        "day": "tor",
        "night": "ntor",
        "qualifier": ""
    },
    "Hurricane Warning": {
        "day": "hur_warn",
        "night": "",
        "qualifier": ""
    },
    "Hurricane Watch": {
        "day": "hur_watch",
        "night": "",
        "qualifier": ""
    },
    "Tropical Storm Warning": {
        "day": "ts_warn",
        "night": "",
        "qualifier": ""
    },
    "Tropical Storm Watch": {
        "day": "ts_watch",
        "night": "",
        "qualifier": ""
    },
    "Tropical Storm Conditions presently exist w/Hurricane Warning in effect": {
        "day": "ts_nowarn",
        "night": "",
        "qualifier": ""
    },
    "Windy": {
        "day": "wind_skc",
        "night": "nwind_skc",
        "qualifier": ""
    },
    "Breezy": {
        "day": "wind_skc",
        "night": "nwind_skc",
        "qualifier": ""
    },
    "Fair and Windy": {
        "day": "wind_skc",
        "night": "nwind_skc",
        "qualifier": ""
    },
    "A Few Clouds and Windy": {
        "day": "wind_few",
        "night": "nwind_few",
        "qualifier": ""
    },
    "Partly Cloudy and Windy": {
        "day": "wind_sct",
        "night": "nwind_sct",
        "qualifier": ""
    },
    "Mostly Cloudy and Windy": {
        "day": "wind_bkn",
        "night": "nwind_bkn",
        "qualifier": ""
    },
    "Overcast and Windy": {
        "day": "nwind_bkn",
        "night": "nwind_bkn",
        "qualifier": ""
    },
    "Dust": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Low Drifting Dust": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Blowing Dust": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Sand": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Blowing Sand": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Low Drifting Sand": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Dust/Sand Whirls": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Dust/Sand Whirls in Vicinity": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Dust Storm": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Heavy Dust Storm": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Dust Storm in Vicinity": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Sand Storm": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Heavy Sand Storm": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Sand Storm in Vicinity": {
        "day": "du",
        "night": "ndu",
        "qualifier": ""
    },
    "Smoke": {
        "day": "fu",
        "night": "fu",
        "qualifier": ""
    },
    "Haze": {
        "day": "hz",
        "night": "",
        "qualifier": ""
    },
    "Hot": {
        "day": "hot",
        "night": "",
        "qualifier": ""
    },
    "Cold": {
        "day": "cold",
        "night": "ncold",
        "qualifier": ""
    },
    "Blizzard": {
        "day": "blizzard",
        "night": "nblizzard",
        "qualifier": ""
    },
    "Fog/Mist": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Freezing Fog": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Shallow Fog": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Partial Fog": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Patches of Fog": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Fog in Vicinity": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Freezing Fog in Vicinity": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Shallow Fog in Vicinity": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Partial Fog in Vicinity": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Patches of Fog in Vicinity": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Showers in Vicinity Fog": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Light Freezing Fog": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    },
    "Heavy Freezing Fog": {
        "day": "fg",
        "night": "nfg",
        "qualifier": ""
    }
}

def _nws_icon(fname):
    fp = path.join('graphics', 'NWS', '%s.b64' % fname)
    with open(fp, 'rb') as f:
        b = f.read()
    return b

def icon_from_cc(current_conditions):
    if current_conditions is not None:
        cc = current_conditions['weather']
        obs_time = current_conditions['observation_time_rfc822']
        if cc in weather_icons:
            icon_data = _nws_icon(weather_icons[cc]['day'])
            tooltip = cc
        else:
            icon_data = _nws_icon('earth')
            tooltip = 'No specific icon found for "%s" conditions.' %\
                current_conditions['weather']
    else:
        icon_data = _nws_icon('void')
        tooltip = 'No weather data received.'
    return (icon_data, tooltip)
