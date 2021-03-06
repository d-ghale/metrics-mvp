from flask import Flask, jsonify, render_template
from flask_cors import CORS

from models import metrics

"""
This is the app's main file!
"""

# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__, template_folder="./frontend/public")
app.config.from_object(__name__)


# enable CORS
CORS(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# home
@app.route('/', methods=['GET'])
def home():
    return jsonify('hello! go to /metrics to see metrics')


# hello world
@app.route('/metrics', methods=['GET'])
def index():
    # TODO problem: this query times out i think
    return "average waiting time is " + str(metrics.get_average_waiting_time(
        stop_id="4970",
        route_id="12",
        direction="O",
        date_range=["2019-01-01", "2019-01-02", "2019-01-03"],
        # use the last month; calculate it and turn it into timestamps
        # date_range=[d.date().strftime("%Y-%m-%d") for d in
        # pd.date_range(pd.datetime.today(), periods=30).tolist()]
        time_range=("09:00", "17:00")))


@app.route('/react', methods=['GET'])
def react():
    return render_template("index.html")


if __name__ == '__main__':
    # using 0.0.0.0 makes it externally visible
    # so gitpod.io can run it
    app.run(host='0.0.0.0')
