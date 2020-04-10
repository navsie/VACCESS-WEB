from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__, static_url_path='')


#
#
# This is temporary, slow code to serve static files.
# In production would prefer nginx or apache handle this.
#
@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('/opt/www/VACCESS/static/assets', path)
@app.route('/bootstrap/<path:path>')
def send_bootstrap(path):
    return send_from_directory('/opt/www/VACCESS/static/bootstrap', path)
@app.route('/plugins/<path:path>')
def send_plugins(path):
    return send_from_directory('/opt/www/VACCESS/static/plugins', path)
#
#
#

@app.route("/")
def index():
	return render_template('index.html', name="BOB")

if __name__ == "__main__":
	app.run(debug = True)
