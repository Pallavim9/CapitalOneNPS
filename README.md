# CapitalOne-NPS

Here's a link to the website: https://nps-capitalone-app.herokuapp.com/

### Capital One Summit Project Requirement

Build a web app that helps users find information related to National Parks


### Capital One Summit Project Requirements

To complete this challenge, build a web application that can do the following:

1. Let visitors search from a list of activities to do at different National Parks
	1. Visitors can click an activity and have the web app display all the National Parks tied to a specific activity
	2. After selecting a specific park, the app should pull up an informational page so the visitor can learn more about
	the park.
2. Have a feature on the web app where visitors can: 
	1. Retrieve data from park web cams based on which National Park(s) the user selects. Specifically, this feature
	should be able to display the non-streaming images collected from park web cams so a visitor can view them with ease.


### Tools used:

* Python 3
* National Park Service API
* Flask
* Bootstrap
* Jinja
* Heroku


### API implementation details

* NPS API sets the default limit to retrieve data using API to 50. Enforced to retrieve a maximum of 500 by setting the limit to 500 during url generation.
* NPS API requires sending an NPS API key registered for each user who makes a call to NPS API. As this API Key is user specific, moved it to Heroku configuration 	settings.


### CapitalOne - NPS implemented features

NPS Search main page: Contains links to search NPS for Park Activities and Park WebCams.

* **Search for parks by a specific activity**: Provides a list of Park Activities. Selecting an activity and clicking the Submit button will display a list of all parks that match/provide the selected activity. Clicking on a park will open the park information website in a new tab.
* **Search for WebCams by a specific park**: Provides a list of parks that have web cam images available. Selecting a park and clicking the Submit button will display all the web cam images available for that park. Clicking on an image will open the image in a new tab.
	* The API call to retrieve all parks returns results that do not have webcam images. To avoid listing parks that do not have images, I have called the API to retrieve just the parks that have webcam functionality.
	
	
### Additional Features implemented

In addition to the features that are required for this web application, additional features that are implemented include:

* **Search for Park alerts by a specific park**: Provides a list of park alerts. Selecting a park and clicking the Submit button will display alerts if any exist for the selected park. Clicking on each alert will open related park alert info page in a new tab.
* **Search for Park amenities by a specific park**: Provides a list of park amenities. Selecting a park and clicking the Submit button will display amenities if any exist for the selected park. Clicking on each amenity link will open related park amenity info page in a new tab.
	
