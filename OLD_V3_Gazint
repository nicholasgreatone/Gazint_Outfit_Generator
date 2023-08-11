                    #Gazint Outfit generator By Nicholasgreatone / Altoids_exe#


#imports for styling and to make the code not break lol
import colorama
from colorama import Fore
import requests
import json 
appid = '982531ce4594fcdd1bdc25ad954f4f71' # API key for weather
from art import *
import random

#outfit bank
from outfits_list import black_outfits
from outfits_list import green_outfits
from outfits_list import red_outfits
from outfits_list import blue_outfits
from outfits_list import purple_outfits
from outfits_list import brown_outfits
from outfits_list import yellow_outfits
from outfits_list import grey_outfits
from outfits_list import white_outfits



          #################################city_input################################  

#main color --->  \033[1;33m --- \033[0m
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


   #################API_Location_Used_only_for_lon_lat_calculation_for_weather_reading_API################
location_url_two = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={appid}'



      ################grabbing_lon_lat_data_for_Herndon_need_revise_for_any_location_use##################
req_location = requests.get(location_url_two)
complete_info = req_location.json()
print (' ')
bulk_info = complete_info[1]
lat = complete_info[1]['lat']
lon = complete_info[1]['lon']

                       ###################Weather_API##################
weather_reading = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}'


    ##################Weather_data_Display_and_conversion_for_K_to_F_temps##################
req_weather = requests.get(weather_reading)
complete_weather_info = req_weather.json()
condition =  complete_weather_info['weather'][0]['main']
temp =  complete_weather_info['main']['temp']
new_temp = round(9 / 5 * (temp - 273.15) + 32, 3)  # K to F conversion happens here
print(' ')
print('_'*68)
print(" ")
print(" ")
print(f'| \033[1;33m{city_name}\033[0m visability looks: \033[1;33m{condition}\033[0m | Current fahrenheit temp: \033[1;33m{new_temp}\033[0m | ')
print(" ")
print('_'*68)
print(" ")
print(" ")

##################Weather_calulation_for_proper_attire_for_temp########################


if new_temp <= 40:
  print ("Gazint says: ʕᵔᴥᵔʔ Its really cold outside, wear something super warm!")
elif new_temp <= 60:
  print (" Gazint says: ʕᵔᴥᵔʔ Its starting to get colder!, wear something nice and warm!")
elif new_temp <= 70:
  print ("Gazint says: ʕᵔᴥᵔʔ its still a bit nice out, but starting to get a little chilly... dont forget a sweatshirt!")
elif new_temp <= 80:
  print ("Gazint says: ʕᵔᴥᵔʔ hurray! its nice out, wear something nice a cool ")
else:
  print ("error: temp range is broken")
  
#########################Warmth_level_for_clothes_based_on_temp########################

Warm = 80- 130
Nice = 70-80
Chilly = 60-70
Cold = 40-60
really_cold = 1-40

###############################Outfit_colors_selection##################################


outfit_colors = ['Green', 'Blue', 'White', 'Black', 'Red', 'Camo','Brown', 'Purple', 'Grey', 'Yellow']
print()
base_color = input ("What color would you like to base your outfit on? (Green, Black, White, Brown, Blue, Red, Purple, Grey, or Yellow?)\nEnter color here: ")

#print (upper_base_color)
upper_base_color = ( base_color.title() )

print(" ")
print(" ")

if upper_base_color in outfit_colors:
  print (f"\033[0;32m     ,The color {upper_base_color} works, generating outfit based on your selection!\033[0m")
  aprint("bear squiting")
else:
  print(f"\033[0;31m     ,Sorry! I failed to find a {upper_base_color} color in your wardrobe, try again with another color! \033[0m")
  aprint("bear squiting")
  
  
##################################Outfit_combos####################################
  
#green_outfits
#blue_outfits
#white_outfits
#red_outfits
#camo_outfits
#blue_outfits
#green_outfits
#red_outfits
#yellow_outfits

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

print ("\n \n")
#####################################

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
      print(" ")
      print(" ")

#####################################

if upper_base_color == ("Green"):
  for b_fit in green_outfits:
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
      print(" ")
      print(" ")
##################################### 

if upper_base_color == ("Red"):
  for b_fit in red_outfits:
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
      print(" ")
      print(" ")
#####################################

if upper_base_color == ("White"):
  for b_fit in white_outfits:
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
      print(" ")
      print(" ")
#####################################

if upper_base_color == ("Brown"):
  for b_fit in brown_outfits:
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
      print(" ")
      print(" ")
#####################################

if upper_base_color == ("Blue"):
  for b_fit in blue_outfits:
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
      print(" ")
      print(" ")
#####################################

if upper_base_color == ("Purple"):
  for b_fit in purple_outfits:
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
      print(" ")
      print(" ")
#####################################
if upper_base_color == ("Grey"):
  for b_fit in grey_outfits:
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
      print(" ")
      print(" ")
#####################################
if upper_base_color == ("Yellow"):
  for b_fit in yellow_outfits:
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
      print(" ")
      print(" ")
#####################################


print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print ("Outfit list complete. ")
print (" ")
