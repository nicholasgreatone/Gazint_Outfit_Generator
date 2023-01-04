

#Outfit generator
import colorama
from colorama import Fore
import requests
import json 
appid = '982531ce4594fcdd1bdc25ad954f4f71'
from art import *

###################only_works_for_hern_for_now_add_BV_soon#############################
##################Weather_calulation_for_proper_attire_for_temp########################





#city_input \033[1;33m --- \033[0m
print ("\033[1;33m ")
tprint("gazint","isometric3")
print (" \033[0m ")
print (" ")
print (" ")
print(" ")
print (" ")
welcome_text = ("\033[3m     ,Hello! My name is \033[1;33mGazint\033[0m! Im your personal wardrobe specialist!\033[0m ")
print (welcome_text)
aprint("bear squiting")
print (" ")
print (" ")
city_name = input ("\nEnter city here:")
print (" ")


#API_Location_Used_only_for_lon_lat_calculation_for_weather_reading_API
location_url_two = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={appid}'



#grabbing_lon_lat_data_for_Herndon_need_revise_for_any_location_use
req_location = requests.get(location_url_two)
complete_info = req_location.json()
print (' ')
bulk_info = complete_info[1]
lat = complete_info[1]['lat']
lon = complete_info[1]['lon']

#Weather_API
weather_reading = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}'


#Weather_data_Display_and_conversion_for_K_to_F_temps
req_weather = requests.get(weather_reading)
complete_weather_info = req_weather.json()
condition =  complete_weather_info['weather'][0]['main']
temp =  complete_weather_info['main']['temp']
new_temp = round(9 / 5 * (temp - 273.15) + 32, 3)
print(' ')
print('_'*68)
print(" ")
print(" ")
print(f'| \033[1;33m{city_name}\033[0m visability looks: \033[1;33m{condition}\033[0m | Current fahrenheit temp: \033[1;33m{new_temp}\033[0m | ')
print(" ")
print('_'*68)
print(" ")
print(" ")


#########################Warmth_level_for_clothes_based_on_temp########################

Warm = 80- 130
Nice = 70-80
Chilly = 60-70
Cold = 40-60
really_cold = 1-40

###############################Outfit_colors_selection##################################


outfit_colors = ['Green', 'Blue', 'White', 'Black', 'Red', 'Camo','Brown']
print()
base_color = input ("What color would you like to base your outfit on?\nEnter color here: ")

#print (upper_base_color)
upper_base_color = ( base_color.title() )

print(" ")
print(" ")

if upper_base_color in outfit_colors:
  print (f"\033[0;32m     ,The color {upper_base_color} works, generating outfit based on your selection!\033[0m")
  aprint("bear squiting")
else:
  print(f"\033[0;31m     ,Sorry! I failed to find a {upper_base_color} color in your wardrobe, try again with another color.\033[0m")
  aprint("bear squiting")
  
  
##################################Outfit_combos####################################
  
#green_outfits
#blue_outfits


black_outfits = [
####
  ##
]


#white_outfits
#red_outfits
#camo_outfits

 #######items_visual######### 
"""
headwear_visual = ('-~-')
glasses_visual = ('o-o ')
shirt_visual = ('-|-')
pants_visual = ('/\ ')
shoe_visual = ('|_ ')


  #########
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(headwear_visual)
print(glasses_visual)
print(shirt_visual)
print(pants_visual)
print(shoe_visual)
#print (black_outfits)
print (" ")
 """

#######################

###########################

  

##########janky v1 of outfit combos####################

black_outfits = [
  {
    'color': 'Black',
    'name' : 'The "Black N Silver" outfit: ',
    'headwear' : [' ~     N/A'],
    'glass' : ['o-o    Aviator sunglasses (green tint) or silver aviators'],
    'shirt' : ['-|-    Black & Silver Nike T-shirt (Add shirt-stays)'], 
    'belt' : [' =     Black Dress Belt'],
    'pant' : ['/ \    Black chino or black corduroy pants '],
    'footwear' : [' L     Doc Martins + black socks '], 
  }

  
]
print ("\n \n")

if upper_base_color == ("Black"):
  for b_fit in black_outfits:
    print(f'{b_fit.get("name")}\n ')
    for hats in b_fit.get("headwear"):
        print(f'\t{hats}')
    for glasses in b_fit.get("glass"):
      print(f"\t{glasses}")
    for shirts in b_fit.get("shirt"):
      print(f"\t{shirts}")
    for belts in b_fit.get("belt"):
      print(f"\t{belts}")
    for pants in b_fit.get("pant"):
      print(f"\t{pants}")
    for shoes in b_fit.get("footwear"):
      print(f"\t{shoes}")
print (" ")
print (" ")
print (" ")
print (" ")

