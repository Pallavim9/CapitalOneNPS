from flask import Flask, render_template, request
from api_helper import get_activities, get_parksbyactivity
from api_helper import get_allparkswithcam, get_parkcaminfo
from api_helper import get_parks, get_park_alerts
from api_helper import get_park_amenities


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/activity-search', methods=["GET", "POST"])
def activity_search():
    activities = get_activities()
    if request.method == "POST":
        selected_activity = request.form.get("activity")
        parksWithActivity = get_parksbyactivity(selected_activity)
        if not parksWithActivity or len(parksWithActivity) == 0:
            parksWithActivity = None
        return render_template('activities.html', activities=activities, selected_activity=activities[selected_activity], selected_activity_code=selected_activity, parks=parksWithActivity)
    else:
        return render_template('activities.html', activities=activities, selected_activity=None, parks=None) 

@app.route('/webcam-info', methods=["GET", "POST"])
def webcam_info():
    parks = get_allparkswithcam()
    if request.method == "POST":
        selected_park = request.form.get("park")
        parkWebCamInfo = get_parkcaminfo(selected_park)
        if not parkWebCamInfo or len(parkWebCamInfo) == 0:
            parkWebCamInfo = None
        return render_template('webcam.html', parks=parks, selected_park=parks[selected_park], parkCode=selected_park, webCams=parkWebCamInfo)
    else:
        return render_template('webcam.html', parks=parks, selected_park=None, webCams=None) 

@app.route('/park-alerts', methods=["GET", "POST"])
def park_alerts():
    parks = get_parks()
    if request.method == "POST":
        selected_park = request.form.get("park")
        parkalertInfo = get_park_alerts(selected_park)
        if not parkalertInfo or len(parkalertInfo) == 0:
            parkalertInfo = None
        return render_template('parkalerts.html', parks=parks, selected_park=parks[selected_park], parkCode=selected_park, alerts=parkalertInfo)
    else:
        return render_template('parkalerts.html', parks=parks, selected_park=None, alerts=None) 

@app.route('/park-amenities', methods=["GET", "POST"])
def park_amenities():
    parks = get_parks()
    if request.method == "POST":
        selected_park = request.form.get("park")
        parkamInfo = get_park_amenities(selected_park)
        if not parkamInfo or len(parkamInfo) == 0:
            parkamInfo = None
        return render_template('parkamenities.html', parks=parks, selected_park=parks[selected_park], parkCode=selected_park, amenities=parkamInfo)
    else:
        return render_template('parkamenities.html', parks=parks, selected_park=None, amenities=None) 



if __name__ == '__main__':
    app.run(debug = True)
