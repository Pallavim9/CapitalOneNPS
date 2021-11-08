import requests
import json
import operator
import os


url = "https://developer.nps.gov/api/v1/"
api_key = os.environ['api_key']

#=================================================================================================
#
# Calls NPS service to retrieve all activities
# Returns a dict of activity id and activity name
#
def get_activities():
	result = {}

	if api_key:
		try:
			activities = retrieve_data(url + "activities?limit=500&api_key=" + api_key)

			if activities:
				for activity in activities["data"]:
					result[activity["id"]] = activity["name"]

			return result
		except:
			return None
	else:
		return None

#==================================================================================================
#
# Calls NPS service to retrieve all parks
# Returns a dict of park code and park full name
#
def get_parks():
	result = {}

	if api_key:
		try:
			parks_data = retrieve_data(url + "parks?limit=500&api_key=" + api_key)
			
			if parks_data:
				for park in parks_data["data"]:
					result[park["parkCode"]] = park["fullName"] + " - " + park["states"]

			return result
		except:
			return None
	else:
		return None

#=================================================================================================
#
# Calls NPS service to retrieve park alerts by park code
# Returns a dict of alert title and url
#
def get_park_alerts(park_code):
	result = {}

	if api_key:
		try:
			alerts = retrieve_data(url + "alerts?limit=500&parkCode=" + park_code + 
				"&api_key=" + api_key)

			if alerts:
				for alert in alerts["data"]:
					result[alert["title"]] = alert["url"]

			return result
		except:
			return None
	else:
		return None

#==================================================================================================
#
# Calls NPS service to retrieve all parks filtered by selected activity id
# Returns a dict of park full name and park url
#
def get_parksbyactivity(activity_id):
	result = {}

	if api_key:
		try:
			if activity_id:
				parks= retrieve_data(url + "activities/parks?limit=500&id=" + activity_id + 
					"&api_key=" + api_key)

				if parks:
					for park in parks["data"][0]["parks"]:
						result[park["fullName"] + " - " + park["states"]] = park["url"]

				return result
		except:
			return None	
	else:
		return None

#==================================================================================================
#
# Calls NPS service to retrieve all park amenities filtered by selected park
# Returns a dict of park amenity name and url
#
def get_park_amenities(park_code):
	result = {}

	if api_key:
		try:
			amenities = retrieve_data(url + "amenities/parksplaces?limit=500&parkCode=" + park_code + 
				"&api_key=" + api_key)
			if amenities:
				for data in amenities["data"]:
					for parks in data[0]["parks"]:
						for places in parks["places"]:
							result[places["title"]] = places["url"]

				return result
			else:
				#Activity_id is required
				return result
		except:
			return None
	else:
		return None

#==================================================================================================
#
# Calls NPS service to retrieve all parks with camera info
# Returns a dict of park code and park full name
#
def get_allparkswithcam():
	result = {}
	
	if api_key:
		try:
			park_cams= retrieve_data(url + "webcams?limit=500&api_key=" + api_key)

			if park_cams:
				for cam in park_cams["data"]:
					for park in cam["relatedParks"]:
						result[park["parkCode"]] = park["fullName"] + " - " + park["states"]

			sorted_result = sorted(result.items(), key=operator.itemgetter(1))
			sorted_dict = {k: v for k, v in sorted_result}

			return sorted_dict
		except:
			return None
	else:
		return None

#=================================================================================================
#
# Calls NPS service to retrieve available web cam pictures for selected park
# Returns a dict of web cam title and web cam picture url
#
def get_parkcaminfo(park_code):
	result = {}
	
	if api_key:
		try:
			if park_code:
				cams= retrieve_data(url + "webcams?limit=500&parkCode=" + park_code + 
					"&api_key=" + api_key)

				if cams:
					for cam in cams["data"]:
						for image in cam["images"]:
							result[cam["title"]] = image["url"]
						
				return result
			else:
				#Park Code is required
				return result
		except:
			return None
	else:
		return None

#=================================================================================================

def retrieve_data(url):
	if url:
		return requests.get(url).json()
	else:
		#url is required
		return None

#================================================================================================
