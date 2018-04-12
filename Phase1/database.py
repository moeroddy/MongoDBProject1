import pymongo 
from pymongo import MongoClient
import datetime
import pprint
import json
from bson import json_util

# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://mrmoe:123123123@cluster0-3drqj.mongodb.net/test") # database string
# the mongodb atlas database 
db=client.test_database
posts = db.posts # create database colection 

with open("airports.json") as json_data:
	d = json.load(json_data)
	#load json file


#posts.insert_many(d)  if you uncomment this and run the app then you'll insert another 3885 
# documents of airport locations

def findCountry(country):
	num = 0
	for post in posts.find({"country": country}):
		for k, v in post.items():
			print (k, ": ", v)
		print("*********************************") 
		num = num + 1
	return num

def findState(state):
	num = 0
	for post in posts.find({"state": state}):
		for k, v in post.items():
			print (k, ": ", v)
		print("*********************************") 
		num = num + 1
	return num

def findCity(city):
	num = 0
	for post in posts.find({"city": city}):
		for k, v in post.items():
			print (k, ": ", v)
		print("*********************************") 
		num = num + 1
	return num

def findCountry1(country):
	num = 0
	for post in posts.find({"country": country}):
		num = num + 1
	return num

def findState1(state):
	num = 0
	for post in posts.find({"state": state}):
		num = num + 1
	return num

def findCity1(city):
	num = 0
	for post in posts.find({"city": city}):
		num = num + 1
	return num

def searchBy():
	code = input("Please enter 1 to search by City, 2 to search by State, 3 to search by Country=> ")
	while code != "1" and code != "2" and code != "3":
		print("please Enter the right number")
		code = input("Please enter 1 to search by City, 2 to search by State, 3 to search by Country => ")
	return code



city = ""
state = ""
country = ""

code = searchBy()

if code == "1":
	city = input("Please enter the city name >> ")
	city= city[:1].upper() + city[1:]
elif code == "2":
	state = input("Please enter the State name >> ")
	state= state[:1].upper() + state[1:]
elif code == "3":
	country = input("Please enter the Country name >> ")
	country= country[:1].upper() + country[1:]


# perform the functions to find out if we get any results back based on the input
#because if for example city = "" then we might have nonsense results  
numCity = findCity1(city)
numState = findState1(state)
numCountry = findCountry1(country)


if len(city) == 0 or numCity == 0:
	if len(state) == 0 or numState == 0:
		if len(country) == 0 or numCountry == 0:
			print("resart the program and please enter a value")
		elif len(country) > 0:
			numberOfAirports = findCountry(country)
	elif len(state) > 0:
		numberOfAirports = findState(state)
elif len(city) > 0: 
	numberOfAirports = findCity(city)




