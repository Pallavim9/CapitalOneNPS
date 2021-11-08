# CapitalOne-NPS

Capital One Summit Project Requirement:
	Build a web app that helps users find information related to National Parks

Capital One Summit Project Requirements:
	To complete this challenge, build a web application that can do the following:

	1. Let visitors search from a list of activities to do at different National Parks
		a. Visitors can click an activity and have the web app display all the National Parks tied to a specific activity
		b. After selecting a specific park, the app should pull up an informational page so the visitor can learn more about the park.
	2. Have a feature on the web app where visitors can: 
		a. Retrieve data from park web cams based on which National Park(s) the user selects. Specifically, this feature   should be able to display the non-streaming 			  images collected from park web cams so a visitor can view them with ease.

Tools used:

	Python3
	National Park Service API
	Flask
	Bootstrap
	Jinja
	Heroku

API implementation details:
	NPS API sets the default limit to retrieve data using API to 50. Enforced to retrieve a maximum of 500 by setting the limit to 500 during url generation.
	NPS API requires sending a NPS API key registered for each user who makes a call to NPS API. As this API Key is user specific, moved it to Heroku configuration 	setting.

CapitalOne - NPS implemented features:
	NPS Search main page: Contains links to search NPS for Park Activities and Park WebCam.

	Search for parks by a specific activity: Provides a list of Park Activities. Selecting an activity and clicking the Submit button will display a list of all parks 	   that match/provide the selected activity. Clicking on a park will open the park information website in a new tab.

	Search for WebCams by a specific park: Provides a list of parks that have web cam images available. Selecting a park and clicking the Submit button will display all   	       the web cam images available for that park. Clicking on an image will open the image in a new tab.
	
Additional Feature implemented:
	In addition to the features that are required for this web application, additional features that are implemented include:

	Search for Park alerts by a specific park: Provides a list of all parks. Selecting a park and clicking the Submit button will display alerts if any exist for the 	  selected park. Clicking on each alert will open related park alert info page in a new tab.

	Search for Park amenities by a specific park: Provides a list of all parks. Selecting a park and clicking the Submit button will display amenities if any exist for 	    the selected park. Clicking on each amenity link will open related park amenity info page in a new tab.
	
