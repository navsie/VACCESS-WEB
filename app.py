from flask import Flask, request, send_from_directory, render_template
import json
import requests

app = Flask(__name__, static_url_path='')


#
#
# This is temporary, slow code to serve static files.
# In production would prefer nginx or apache handle this.
#
@app.route('/static/assets/<path:path>')
def send_assets(path):
    return send_from_directory('/opt/www/VACCESS/static/assets', path)
@app.route('/static/bootstrap/<path:path>')
def send_bootstrap(path):
    return send_from_directory('/opt/www/VACCESS/static/bootstrap', path)
@app.route('/static/plugins/<path:path>')
def send_plugins(path):
    return send_from_directory('/opt/www/VACCESS/static/plugins', path)
#
#
#

@app.route("/")
def index():
	r = requests.get('https://vaccess-service.herokuapp.com/api/getStateRiskLevel?state=ca')
	return render_template('index.html', title="Welcome to vaccess", r=r.json())

@app.route("/chart")
def chart():
	r = requests.get('https://vaccess-service.herokuapp.com/api/getStateRiskLevel?state=ca')
	return render_template('chart.html', title="List - vaccess", r=r.json())

@app.route("/resources")
def resources():
	return render_template('resources.html', title="Insights - vaccess")

@app.route("/stats")
def stats():
	return render_template('stats.html', title="Algorithm - vaccess")

@app.route('/gmappage')
def gmappage():
	# gmaps.configure(api_key="AIzaSyB82meUu-KE5JSvX7oUvALGybDAebeAak0")
	# locations = gmaps.datasets.load_dataset({
 #       "url": "https://s3-eu-west-1.amazonaws.com/jupyter-gmaps-examples/taxi_data.csv",  # noqa
 #       "description": "Taxi pickup location data in San Francisco",
 #       "headers": ["latitude", "longitude"],
 #       "types": [float, float]
 #   })
	# new_york_coordinates = (40.75, -74.00)
	# fig = gmaps.figure(center=new_york_coordinates, zoom_level=12)
	# fig.add_layer(gmaps.heatmap_layer(locations))
	# fig
	# return "I have maps.";
		return render_template('gmap.html')



if __name__ == "__main__":
	app.run(debug = True)
