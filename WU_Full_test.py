import urllib2
import json
APIKEY = "61656f824e31c38b"
STATIONID = "KMDLAURE30"

WUAPI = urllib2.urlopen('http://api.wunderground.com/api/%s/conditions/astronomy/alerts/q/pws:%s.json' % (APIKEY, STATIONID))
json_string = WUAPI.read()
current_json = json.loads(json_string)


station_id = current_json['current_observation']['station_id']
observation_time = current_json['current_observation']['observation_time']
location = current_json['current_observation']['observation_location']['full']
weather = current_json['current_observation']['weather']
temp_f = current_json['current_observation']['temp_f']
feelslike_f = current_json['current_observation']['feelslike_f']
relative_humidity = current_json['current_observation']['relative_humidity']
dewpoint_f = current_json['current_observation']['dewpoint_f']
pressure_in = current_json['current_observation']['pressure_in']
wind_string = current_json['current_observation']['wind_string']
percentIlluminated = current_json['moon_phase']['percentIlluminated']
phaseofMoon = current_json['moon_phase']['phaseofMoon']
sunrise_h = current_json['moon_phase']['sunrise']['hour']
sunrise_m = current_json['moon_phase']['sunrise']['minute']
sunset_h = current_json['moon_phase']['sunset']['hour']
sunset_m = current_json['moon_phase']['sunset']['minute']

#description = current_json['alerts'][0]['description']
#message = current_json['alerts'][0]['message']

WUAPI.close()





WUAPI = urllib2.urlopen('http://api.wunderground.com/api/%s/almanac/forecast/q/MD/Baltimore.json' % (APIKEY))
json_string = WUAPI.read()
current_json = json.loads(json_string)
#WU Almanac
almanac_airport_code = current_json['almanac']['airport_code']
almanac_temp_high_normalF = current_json['almanac']['temp_high']['normal']['F']
almanac_temp_high_normalC = current_json['almanac']['temp_high']['normal']['C']
almanac_temp_high_recordF = current_json['almanac']['temp_high']['record']['F']
almanac_temp_high_recordC = current_json['almanac']['temp_high']['record']['C']
almanac_temp_high_recordyear = current_json['almanac']['temp_high']['recordyear']
almanac_temp_low_normalF = current_json['almanac']['temp_low']['normal']['F']
almanac_temp_low_normalC = current_json['almanac']['temp_low']['normal']['C']
almanac_temp_low_recordF = current_json['almanac']['temp_low']['record']['F']
almanac_temp_low_recordC = current_json['almanac']['temp_low']['record']['C']
almanac_temp_low_recordyear = current_json['almanac']['temp_low']['recordyear']
#WU Forecast
forecast_txt_forecast_date = current_json['forecast']['txt_forecast']['date']
forecast_txt_forecast_forecastday_0_period = current_json['forecast']['txt_forecast']['forecastday'][0]['period']
forecast_txt_forecast_forecastday_0_icon = current_json['forecast']['txt_forecast']['forecastday'][0]['icon']
forecast_txt_forecast_forecastday_0_icon_url = current_json['forecast']['txt_forecast']['forecastday'][0]['icon_url']
forecast_txt_forecast_forecastday_0_title = current_json['forecast']['txt_forecast']['forecastday'][0]['title']
forecast_txt_forecast_forecastday_0_fcttext = current_json['forecast']['txt_forecast']['forecastday'][0]['fcttext']
forecast_txt_forecast_forecastday_0_fcttext_metric = current_json['forecast']['txt_forecast']['forecastday'][0]['fcttext_metric']
forecast_txt_forecast_forecastday_0_pop = current_json['forecast']['txt_forecast']['forecastday'][0]['pop']

forecast_txt_forecast_forecastday_1_period = current_json['forecast']['txt_forecast']['forecastday'][1]['period']
forecast_txt_forecast_forecastday_1_icon = current_json['forecast']['txt_forecast']['forecastday'][1]['icon']
forecast_txt_forecast_forecastday_1_icon_url = current_json['forecast']['txt_forecast']['forecastday'][1]['icon_url']
forecast_txt_forecast_forecastday_1_title = current_json['forecast']['txt_forecast']['forecastday'][1]['title']
forecast_txt_forecast_forecastday_1_fcttext = current_json['forecast']['txt_forecast']['forecastday'][1]['fcttext']
forecast_txt_forecast_forecastday_1_fcttext_metric = current_json['forecast']['txt_forecast']['forecastday'][1]['fcttext_metric']
forecast_txt_forecast_forecastday_1_pop = current_json['forecast']['txt_forecast']['forecastday'][1]['pop']

forecast_txt_forecast_forecastday_2_period = current_json['forecast']['txt_forecast']['forecastday'][2]['period']
forecast_txt_forecast_forecastday_2_icon = current_json['forecast']['txt_forecast']['forecastday'][2]['icon']
forecast_txt_forecast_forecastday_2_icon_url = current_json['forecast']['txt_forecast']['forecastday'][2]['icon_url']
forecast_txt_forecast_forecastday_2_title = current_json['forecast']['txt_forecast']['forecastday'][2]['title']
forecast_txt_forecast_forecastday_2_fcttext = current_json['forecast']['txt_forecast']['forecastday'][2]['fcttext']
forecast_txt_forecast_forecastday_2_fcttext_metric = current_json['forecast']['txt_forecast']['forecastday'][2]['fcttext_metric']
forecast_txt_forecast_forecastday_2_pop = current_json['forecast']['txt_forecast']['forecastday'][2]['pop']

forecast_txt_forecast_forecastday_3_period = current_json['forecast']['txt_forecast']['forecastday'][3]['period']
forecast_txt_forecast_forecastday_3_icon = current_json['forecast']['txt_forecast']['forecastday'][3]['icon']
forecast_txt_forecast_forecastday_3_icon_url = current_json['forecast']['txt_forecast']['forecastday'][3]['icon_url']
forecast_txt_forecast_forecastday_3_title = current_json['forecast']['txt_forecast']['forecastday'][3]['title']
forecast_txt_forecast_forecastday_3_fcttext = current_json['forecast']['txt_forecast']['forecastday'][3]['fcttext']
forecast_txt_forecast_forecastday_3_fcttext_metric = current_json['forecast']['txt_forecast']['forecastday'][3]['fcttext_metric']
forecast_txt_forecast_forecastday_3_pop = current_json['forecast']['txt_forecast']['forecastday'][3]['pop']

forecast_txt_forecast_forecastday_4_period = current_json['forecast']['txt_forecast']['forecastday'][4]['period']
forecast_txt_forecast_forecastday_4_icon = current_json['forecast']['txt_forecast']['forecastday'][4]['icon']
forecast_txt_forecast_forecastday_4_icon_url = current_json['forecast']['txt_forecast']['forecastday'][4]['icon_url']
forecast_txt_forecast_forecastday_4_title = current_json['forecast']['txt_forecast']['forecastday'][4]['title']
forecast_txt_forecast_forecastday_4_fcttext = current_json['forecast']['txt_forecast']['forecastday'][4]['fcttext']
forecast_txt_forecast_forecastday_4_fcttext_metric = current_json['forecast']['txt_forecast']['forecastday'][4]['fcttext_metric']
forecast_txt_forecast_forecastday_4_pop = current_json['forecast']['txt_forecast']['forecastday'][4]['pop']

forecast_txt_forecast_forecastday_5_period = current_json['forecast']['txt_forecast']['forecastday'][5]['period']
forecast_txt_forecast_forecastday_5_icon = current_json['forecast']['txt_forecast']['forecastday'][5]['icon']
forecast_txt_forecast_forecastday_5_icon_url = current_json['forecast']['txt_forecast']['forecastday'][5]['icon_url']
forecast_txt_forecast_forecastday_5_title = current_json['forecast']['txt_forecast']['forecastday'][5]['title']
forecast_txt_forecast_forecastday_5_fcttext = current_json['forecast']['txt_forecast']['forecastday'][5]['fcttext']
forecast_txt_forecast_forecastday_5_fcttext_metric = current_json['forecast']['txt_forecast']['forecastday'][5]['fcttext_metric']
forecast_txt_forecast_forecastday_5_pop = current_json['forecast']['txt_forecast']['forecastday'][5]['pop']

forecast_txt_forecast_forecastday_6_period = current_json['forecast']['txt_forecast']['forecastday'][6]['period']
forecast_txt_forecast_forecastday_6_icon = current_json['forecast']['txt_forecast']['forecastday'][6]['icon']
forecast_txt_forecast_forecastday_6_icon_url = current_json['forecast']['txt_forecast']['forecastday'][6]['icon_url']
forecast_txt_forecast_forecastday_6_title = current_json['forecast']['txt_forecast']['forecastday'][6]['title']
forecast_txt_forecast_forecastday_6_fcttext = current_json['forecast']['txt_forecast']['forecastday'][6]['fcttext']
forecast_txt_forecast_forecastday_6_fcttext_metric = current_json['forecast']['txt_forecast']['forecastday'][6]['fcttext_metric']
forecast_txt_forecast_forecastday_6_pop = current_json['forecast']['txt_forecast']['forecastday'][6]['pop']

forecast_txt_forecast_forecastday_7_period = current_json['forecast']['txt_forecast']['forecastday'][7]['period']
forecast_txt_forecast_forecastday_7_icon = current_json['forecast']['txt_forecast']['forecastday'][7]['icon']
forecast_txt_forecast_forecastday_7_icon_url = current_json['forecast']['txt_forecast']['forecastday'][7]['icon_url']
forecast_txt_forecast_forecastday_7_title = current_json['forecast']['txt_forecast']['forecastday'][7]['title']
forecast_txt_forecast_forecastday_7_fcttext = current_json['forecast']['txt_forecast']['forecastday'][7]['fcttext']
forecast_txt_forecast_forecastday_7_fcttext_metric = current_json['forecast']['txt_forecast']['forecastday'][7]['fcttext_metric']
forecast_txt_forecast_forecastday_7_pop = current_json['forecast']['txt_forecast']['forecastday'][7]['pop']

forecast_simpleforecast_forecastday_0_date_epoch = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['epoch']
forecast_simpleforecast_forecastday_0_date_pretty = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['pretty']
forecast_simpleforecast_forecastday_0_date_day = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['day']
forecast_simpleforecast_forecastday_0_date_month = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['month']
forecast_simpleforecast_forecastday_0_date_year = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['year']
forecast_simpleforecast_forecastday_0_date_yday = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['yday']
forecast_simpleforecast_forecastday_0_date_hour = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['hour']
forecast_simpleforecast_forecastday_0_date_min = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['min']
forecast_simpleforecast_forecastday_0_date_sec = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['sec']
forecast_simpleforecast_forecastday_0_date_isdist = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['isdist']
forecast_simpleforecast_forecastday_0_date_monthname = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['monthname']
forecast_simpleforecast_forecastday_0_date_monthname_short = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['monthname_short']
forecast_simpleforecast_forecastday_0_date_weekday_short = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['weekday_short']
forecast_simpleforecast_forecastday_0_date_weekday = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['weekday']
forecast_simpleforecast_forecastday_0_date_ampm = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['ampm']
forecast_simpleforecast_forecastday_0_date_tz_short = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['tz_short']
forecast_simpleforecast_forecastday_0_date_tz_long = current_json['forecast']['simple_forecast']['forecastday'][0]['date']['tz_long']
forecast_simpleforecast_forecastday_0_high_fahrenheit = current_json['forecast']['simple_forecast']['forecastday'][0]['high']['fahrenheit']
forecast_simpleforecast_forecastday_0_high_celsius = current_json['forecast']['simple_forecast']['forecastday'][0]['high']['celsius']
forecast_simpleforecast_forecastday_0_low_fahrenheit = current_json['forecast']['simple_forecast']['forecastday'][0]['low']['fahrenheit']
forecast_simpleforecast_forecastday_0_low_celsius = current_json['forecast']['simple_forecast']['forecastday'][0]['low']['celsius']
forecast_simpleforecast_forecastday_0_conditions = current_json['forecast']['simple_forecast']['forecastday'][0]['conditions']
forecast_simpleforecast_forecastday_0_icon = current_json['forecast']['simple_forecast']['forecastday'][0]['icon']
forecast_simpleforecast_forecastday_0_icon_url = current_json['forecast']['simple_forecast']['forecastday'][0]['icon_url']
forecast_simpleforecast_forecastday_0_skyicon = current_json['forecast']['simple_forecast']['forecastday'][0]['skyicon']
forecast_simpleforecast_forecastday_0_pop = current_json['forecast']['simple_forecast']['forecastday'][0]['pop']
forecast_simpleforecast_forecastday_0_qpf_allday_in = current_json['forecast']['simple_forecast']['forecastday'][0]['qpf_allday']['in']
forecast_simpleforecast_forecastday_0_qpf_allday_mm = current_json['forecast']['simple_forecast']['forecastday'][0]['qpf_allday']['mm']
forecast_simpleforecast_forecastday_0_qpf_day_in = current_json['forecast']['simple_forecast']['forecastday'][0]['qpf_day']['in']
forecast_simpleforecast_forecastday_0_qpf_day_mm = current_json['forecast']['simple_forecast']['forecastday'][0]['qpf_day']['mm']
forecast_simpleforecast_forecastday_0_qpf_night_in = current_json['forecast']['simple_forecast']['forecastday'][0]['qpf_night']['in']
forecast_simpleforecast_forecastday_0_qpf_night_mm = current_json['forecast']['simple_forecast']['forecastday'][0]['qpf_night']['mm']
forecast_simpleforecast_forecastday_0_snow_allday_in = current_json['forecast']['simple_forecast']['forecastday'][0]['snow_allday']['in']
forecast_simpleforecast_forecastday_0_snow_allday_cm = current_json['forecast']['simple_forecast']['forecastday'][0]['snow_allday']['cm']
forecast_simpleforecast_forecastday_0_snow_day_in = current_json['forecast']['simple_forecast']['forecastday'][0]['snow_day']['in']
forecast_simpleforecast_forecastday_0_snow_day_cm = current_json['forecast']['simple_forecast']['forecastday'][0]['snow_day']['cm']
forecast_simpleforecast_forecastday_0_snow_night_in = current_json['forecast']['simple_forecast']['forecastday'][0]['snow_night']['in']
forecast_simpleforecast_forecastday_0_snow_night_cm = current_json['forecast']['simple_forecast']['forecastday'][0]['snow_night']['cm']
forecast_simpleforecast_forecastday_0_maxwind_mph = current_json['forecast']['simple_forecast']['forecastday'][0]['maxwind']['mph']
forecast_simpleforecast_forecastday_0_maxwind_kph = current_json['forecast']['simple_forecast']['forecastday'][0]['maxwind']['kph']
forecast_simpleforecast_forecastday_0_maxwind_dir = current_json['forecast']['simple_forecast']['forecastday'][0]['maxwind']['dir']
forecast_simpleforecast_forecastday_0_maxwind_degrees = current_json['forecast']['simple_forecast']['forecastday'][0]['maxwind']['degrees']
forecast_simpleforecast_forecastday_0_avewind_mph = current_json['forecast']['simple_forecast']['forecastday'][0]['avewind']['mph']
forecast_simpleforecast_forecastday_0_avewind_kph = current_json['forecast']['simple_forecast']['forecastday'][0]['avewind']['kph']
forecast_simpleforecast_forecastday_0_avewind_dir = current_json['forecast']['simple_forecast']['forecastday'][0]['avewind']['dir']
forecast_simpleforecast_forecastday_0_avewind_degrees = current_json['forecast']['simple_forecast']['forecastday'][0]['avewind']['degrees']
forecast_simpleforecast_forecastday_0_avehumidity = current_json['forecast']['simple_forecast']['forecastday'][0]['avehumidity']
forecast_simpleforecast_forecastday_0_maxhumidity = current_json['forecast']['simple_forecast']['forecastday'][0]['maxhumidity']
forecast_simpleforecast_forecastday_0_minhumidity = current_json['forecast']['simple_forecast']['forecastday'][0]['minhumidity']
#print "%s" % (airport_code)


file = open("/var/www/html/localweather.txt","w")
file.write("Current Conditions at %s in %s...last updated %s\n" % (station_id, location,observation_time))
file.write("Current Weather: %s\n" % (weather))
file.write("Current Temperature: %s / Feels like %s\n" % (temp_f, feelslike_f))
file.write("Current Relative Humidity: %s\n" % (relative_humidity))
file.write("Current Dewpoint: %s\n" % (dewpoint_f))
file.write("Current Pressure: %s in\n" % (pressure_in))
file.write("Current Wind: %s\n" % (wind_string))
file.write("Current Moon: %s | %s%%\n" % (phaseofMoon, percentIlluminated))
file.write("Today's Sunrise: %s:%s\n" % (sunrise_h, sunrise_m))
file.write("Today's Sunset: %s:%s\n" % (sunset_h, sunset_m))
file.write("\n")
file.write("almanac_airport_code: %s\n" % (almanac_airport_code))
file.write("almanac_temp_high_normalF: %s\n" % (almanac_temp_high_normalF))
file.write("almanac_temp_high_normalC: %s\n" % (almanac_temp_high_normalC))
file.write("almanac_temp_high_recordF: %s\n" % (almanac_temp_high_recordF))
file.write("almanac_temp_high_recordC: %s\n" % (almanac_temp_high_recordC))
file.write("almanac_temp_high_recordyear: %s\n" % (almanac_temp_high_recordyear))
file.write("almanac_temp_low_normalF: %s\n" % (almanac_temp_low_normalF))
file.write("almanac_temp_low_normalC: %s\n" % (almanac_temp_low_normalC))
file.write("almanac_temp_low_recordF: %s\n" % (almanac_temp_low_recordF))
file.write("almanac_temp_low_recordC: %s\n" % (almanac_temp_low_recordC))
file.write("almanac_temp_low_recordyear: %s\n" % (almanac_temp_low_recordyear))
file.write("\n")
file.write("forecast_txt_forecast_date: %s\n" % (forecast_txt_forecast_date))
file.write("forecast_txt_forecast_forecastday_0_period: %s\n" % (forecast_txt_forecast_forecastday_0_period))
file.write("forecast_txt_forecast_forecastday_0_icon: %s\n" % (forecast_txt_forecast_forecastday_0_icon))
file.write("forecast_txt_forecast_forecastday_0_icon_url: %s\n" % (forecast_txt_forecast_forecastday_0_icon_url))
file.write("forecast_txt_forecast_forecastday_0_title: %s\n" % (forecast_txt_forecast_forecastday_0_title))
file.write("forecast_txt_forecast_forecastday_0_fcttext: %s\n" % (forecast_txt_forecast_forecastday_0_fcttext))
file.write("forecast_txt_forecast_forecastday_0_fcttext_metric: %s\n" % (forecast_txt_forecast_forecastday_0_fcttext_metric))
file.write("forecast_txt_forecast_forecastday_0_pop: %s\n" % (forecast_txt_forecast_forecastday_0_pop))
file.write("\n")
file.write("forecast_txt_forecast_forecastday_1_period: %s\n" % (forecast_txt_forecast_forecastday_1_period))
file.write("forecast_txt_forecast_forecastday_1_icon: %s\n" % (forecast_txt_forecast_forecastday_1_icon))
file.write("forecast_txt_forecast_forecastday_1_icon_url: %s\n" % (forecast_txt_forecast_forecastday_1_icon_url))
file.write("forecast_txt_forecast_forecastday_1_title: %s\n" % (forecast_txt_forecast_forecastday_1_title))
file.write("forecast_txt_forecast_forecastday_1_fcttext: %s\n" % (forecast_txt_forecast_forecastday_1_fcttext))
file.write("forecast_txt_forecast_forecastday_1_fcttext_metric: %s\n" % (forecast_txt_forecast_forecastday_1_fcttext_metric))
file.write("forecast_txt_forecast_forecastday_1_pop: %s\n" % (forecast_txt_forecast_forecastday_1_pop))
file.write("\n")
file.write("forecast_txt_forecast_forecastday_2_period: %s\n" % (forecast_txt_forecast_forecastday_2_period))
file.write("forecast_txt_forecast_forecastday_2_icon: %s\n" % (forecast_txt_forecast_forecastday_2_icon))
file.write("forecast_txt_forecast_forecastday_2_icon_url: %s\n" % (forecast_txt_forecast_forecastday_2_icon_url))
file.write("forecast_txt_forecast_forecastday_2_title: %s\n" % (forecast_txt_forecast_forecastday_2_title))
file.write("forecast_txt_forecast_forecastday_2_fcttext: %s\n" % (forecast_txt_forecast_forecastday_2_fcttext))
file.write("forecast_txt_forecast_forecastday_2_fcttext_metric: %s\n" % (forecast_txt_forecast_forecastday_2_fcttext_metric))
file.write("forecast_txt_forecast_forecastday_2_pop: %s\n" % (forecast_txt_forecast_forecastday_2_pop))
file.write("\n")
file.write("forecast_txt_forecast_forecastday_3_period: %s\n" % (forecast_txt_forecast_forecastday_3_period))
file.write("forecast_txt_forecast_forecastday_3_icon: %s\n" % (forecast_txt_forecast_forecastday_3_icon))
file.write("forecast_txt_forecast_forecastday_3_icon_url: %s\n" % (forecast_txt_forecast_forecastday_3_icon_url))
file.write("forecast_txt_forecast_forecastday_3_title: %s\n" % (forecast_txt_forecast_forecastday_3_title))
file.write("forecast_txt_forecast_forecastday_3_fcttext: %s\n" % (forecast_txt_forecast_forecastday_3_fcttext))
file.write("forecast_txt_forecast_forecastday_3_fcttext_metric: %s\n" % (forecast_txt_forecast_forecastday_3_fcttext_metric))
file.write("forecast_txt_forecast_forecastday_3_pop: %s\n" % (forecast_txt_forecast_forecastday_3_pop))
file.write("\n")
file.write("forecast_txt_forecast_forecastday_4_period: %s\n" % (forecast_txt_forecast_forecastday_4_period))
file.write("forecast_txt_forecast_forecastday_4_icon: %s\n" % (forecast_txt_forecast_forecastday_4_icon))
file.write("forecast_txt_forecast_forecastday_4_icon_url: %s\n" % (forecast_txt_forecast_forecastday_4_icon_url))
file.write("forecast_txt_forecast_forecastday_4_title: %s\n" % (forecast_txt_forecast_forecastday_4_title))
file.write("forecast_txt_forecast_forecastday_4_fcttext: %s\n" % (forecast_txt_forecast_forecastday_4_fcttext))
file.write("forecast_txt_forecast_forecastday_4_fcttext_metric: %s\n" % (forecast_txt_forecast_forecastday_4_fcttext_metric))
file.write("forecast_txt_forecast_forecastday_4_pop: %s\n" % (forecast_txt_forecast_forecastday_4_pop))
file.write("\n")
file.write("forecast_txt_forecast_forecastday_5_period: %s\n" % (forecast_txt_forecast_forecastday_5_period))
file.write("forecast_txt_forecast_forecastday_5_icon: %s\n" % (forecast_txt_forecast_forecastday_5_icon))
file.write("forecast_txt_forecast_forecastday_5_icon_url: %s\n" % (forecast_txt_forecast_forecastday_5_icon_url))
file.write("forecast_txt_forecast_forecastday_5_title: %s\n" % (forecast_txt_forecast_forecastday_5_title))
file.write("forecast_txt_forecast_forecastday_5_fcttext: %s\n" % (forecast_txt_forecast_forecastday_5_fcttext))
file.write("forecast_txt_forecast_forecastday_5_fcttext_metric: %s\n" % (forecast_txt_forecast_forecastday_5_fcttext_metric))
file.write("forecast_txt_forecast_forecastday_5_pop: %s\n" % (forecast_txt_forecast_forecastday_5_pop))
file.write("\n")
file.write("forecast_txt_forecast_forecastday_6_period: %s\n" % (forecast_txt_forecast_forecastday_6_period))
file.write("forecast_txt_forecast_forecastday_6_icon: %s\n" % (forecast_txt_forecast_forecastday_6_icon))
file.write("forecast_txt_forecast_forecastday_6_icon_url: %s\n" % (forecast_txt_forecast_forecastday_6_icon_url))
file.write("forecast_txt_forecast_forecastday_6_title: %s\n" % (forecast_txt_forecast_forecastday_6_title))
file.write("forecast_txt_forecast_forecastday_6_fcttext: %s\n" % (forecast_txt_forecast_forecastday_6_fcttext))
file.write("forecast_txt_forecast_forecastday_6_fcttext_metric: %s\n" % (forecast_txt_forecast_forecastday_6_fcttext_metric))
file.write("forecast_txt_forecast_forecastday_6_pop: %s\n" % (forecast_txt_forecast_forecastday_6_pop))
file.write("\n")
file.write("forecast_txt_forecast_forecastday_7_period: %s\n" % (forecast_txt_forecast_forecastday_7_period))
file.write("forecast_txt_forecast_forecastday_7_icon: %s\n" % (forecast_txt_forecast_forecastday_7_icon))
file.write("forecast_txt_forecast_forecastday_7_icon_url: %s\n" % (forecast_txt_forecast_forecastday_7_icon_url))
file.write("forecast_txt_forecast_forecastday_7_title: %s\n" % (forecast_txt_forecast_forecastday_7_title))
file.write("forecast_txt_forecast_forecastday_7_fcttext: %s\n" % (forecast_txt_forecast_forecastday_7_fcttext))
file.write("forecast_txt_forecast_forecastday_7_fcttext_metric: %s\n" % (forecast_txt_forecast_forecastday_7_fcttext_metric))
file.write("forecast_txt_forecast_forecastday_7_pop: %s\n" % (forecast_txt_forecast_forecastday_7_pop))
file.write("\n")
file.write("forecast_simpleforecast_forecastday_0_date_epoch: %s\n" % (forecast_simpleforecast_forecastday_0_date_epoch))
file.write("forecast_simpleforecast_forecastday_0_date_pretty: %s\n" % (forecast_simpleforecast_forecastday_0_date_pretty))
file.write("forecast_simpleforecast_forecastday_0_date_day: %s\n" % (forecast_simpleforecast_forecastday_0_date_day))
file.write("forecast_simpleforecast_forecastday_0_date_month: %s\n" % (forecast_simpleforecast_forecastday_0_date_month))
file.write("forecast_simpleforecast_forecastday_0_date_year: %s\n" % (forecast_simpleforecast_forecastday_0_date_year))
file.write("forecast_simpleforecast_forecastday_0_date_yday: %s\n" % (forecast_simpleforecast_forecastday_0_date_yday))
file.write("forecast_simpleforecast_forecastday_0_date_hour: %s\n" % (forecast_simpleforecast_forecastday_0_date_hour))
file.write("forecast_simpleforecast_forecastday_0_date_min: %s\n" % (forecast_simpleforecast_forecastday_0_date_min))
file.write("forecast_simpleforecast_forecastday_0_date_sec: %s\n" % (forecast_simpleforecast_forecastday_0_date_sec))
file.write("forecast_simpleforecast_forecastday_0_date_isdist: %s\n" % (forecast_simpleforecast_forecastday_0_date_isdist))
file.write("forecast_simpleforecast_forecastday_0_date_monthname: %s\n" % (forecast_simpleforecast_forecastday_0_date_monthname))
file.write("forecast_simpleforecast_forecastday_0_date_monthname_short: %s\n" % (forecast_simpleforecast_forecastday_0_date_monthname_short))
file.write("forecast_simpleforecast_forecastday_0_date_weekday_short: %s\n" % (forecast_simpleforecast_forecastday_0_date_weekday_short))
file.write("forecast_simpleforecast_forecastday_0_date_weekday: %s\n" % (forecast_simpleforecast_forecastday_0_date_weekday))
file.write("forecast_simpleforecast_forecastday_0_date_ampm: %s\n" % (forecast_simpleforecast_forecastday_0_date_ampm))
file.write("forecast_simpleforecast_forecastday_0_date_tz_short: %s\n" % (forecast_simpleforecast_forecastday_0_date_tz_short))
file.write("forecast_simpleforecast_forecastday_0_date_tz_long: %s\n" % (forecast_simpleforecast_forecastday_0_date_tz_long))
file.write("forecast_simpleforecast_forecastday_0_high_fahrenheit: %s\n" % (forecast_simpleforecast_forecastday_0_high_fahrenheit))
file.write("forecast_simpleforecast_forecastday_0_high_celsius: %s\n" % (forecast_simpleforecast_forecastday_0_high_celsius))
file.write("forecast_simpleforecast_forecastday_0_low_fahrenheit: %s\n" % (forecast_simpleforecast_forecastday_0_low_fahrenheit))
file.write("forecast_simpleforecast_forecastday_0_low_celsius: %s\n" % (forecast_simpleforecast_forecastday_0_low_celsius))
file.write("forecast_simpleforecast_forecastday_0_conditions: %s\n" % (forecast_simpleforecast_forecastday_0_conditions))
file.write("forecast_simpleforecast_forecastday_0_icon: %s\n" % (forecast_simpleforecast_forecastday_0_icon))
file.write("forecast_simpleforecast_forecastday_0_icon_url: %s\n" % (forecast_simpleforecast_forecastday_0_icon_url))
file.write("forecast_simpleforecast_forecastday_0_skyicon: %s\n" % (forecast_simpleforecast_forecastday_0_skyicon))
file.write("forecast_simpleforecast_forecastday_0_pop: %s\n" % (forecast_simpleforecast_forecastday_0_pop))
file.write("forecast_simpleforecast_forecastday_0_qpf_allday_in: %s\n" % (forecast_simpleforecast_forecastday_0_qpf_allday_in))
file.write("forecast_simpleforecast_forecastday_0_qpf_allday_mm: %s\n" % (forecast_simpleforecast_forecastday_0_qpf_allday_mm))
file.write("forecast_simpleforecast_forecastday_0_qpf_day_in: %s\n" % (forecast_simpleforecast_forecastday_0_qpf_day_in))
file.write("forecast_simpleforecast_forecastday_0_qpf_day_mm: %s\n" % (forecast_simpleforecast_forecastday_0_qpf_day_mm))
file.write("forecast_simpleforecast_forecastday_0_qpf_night_in: %s\n" % (forecast_simpleforecast_forecastday_0_qpf_night_in))
file.write("forecast_simpleforecast_forecastday_0_qpf_night_mm: %s\n" % (forecast_simpleforecast_forecastday_0_qpf_night_mm))
file.write("forecast_simpleforecast_forecastday_0_snow_allday_in: %s\n" % (forecast_simpleforecast_forecastday_0_snow_allday_in))
file.write("forecast_simpleforecast_forecastday_0_snow_allday_cm: %s\n" % (forecast_simpleforecast_forecastday_0_snow_allday_cm))
file.write("forecast_simpleforecast_forecastday_0_snow_day_in: %s\n" % (forecast_simpleforecast_forecastday_0_snow_day_in))
file.write("forecast_simpleforecast_forecastday_0_snow_day_cm: %s\n" % (forecast_simpleforecast_forecastday_0_snow_day_cm))
file.write("forecast_simpleforecast_forecastday_0_snow_night_in: %s\n" % (forecast_simpleforecast_forecastday_0_snow_night_in))
file.write("forecast_simpleforecast_forecastday_0_snow_night_cm: %s\n" % (forecast_simpleforecast_forecastday_0_snow_night_cm))
file.write("forecast_simpleforecast_forecastday_0_maxwind_mph: %s\n" % (forecast_simpleforecast_forecastday_0_maxwind_mph))
file.write("forecast_simpleforecast_forecastday_0_maxwind_kph: %s\n" % (forecast_simpleforecast_forecastday_0_maxwind_kph))
file.write("forecast_simpleforecast_forecastday_0_maxwind_dir: %s\n" % (forecast_simpleforecast_forecastday_0_maxwind_dir))
file.write("forecast_simpleforecast_forecastday_0_maxwind_degrees: %s\n" % (forecast_simpleforecast_forecastday_0_maxwind_degrees))
file.write("forecast_simpleforecast_forecastday_0_avewind_mph: %s\n" % (forecast_simpleforecast_forecastday_0_avewind_mph))
file.write("forecast_simpleforecast_forecastday_0_avewind_kph: %s\n" % (forecast_simpleforecast_forecastday_0_avewind_kph))
file.write("forecast_simpleforecast_forecastday_0_avewind_dir: %s\n" % (forecast_simpleforecast_forecastday_0_avewind_dir))
file.write("forecast_simpleforecast_forecastday_0_avewind_degrees: %s\n" % (forecast_simpleforecast_forecastday_0_avewind_degrees))
file.write("forecast_simpleforecast_forecastday_0_avehumidity: %s\n" % (forecast_simpleforecast_forecastday_0_avehumidity))
file.write("forecast_simpleforecast_forecastday_0_maxhumidity: %s\n" % (forecast_simpleforecast_forecastday_0_maxhumidity))
file.write("forecast_simpleforecast_forecastday_0_minhumidity: %s\n" % (forecast_simpleforecast_forecastday_0_minhumidity))




file.close()