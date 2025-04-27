from flask import Flask, render_template, request
from scripts.ParseManager import ParseEarthQuake
from scripts.GraphManger import plot_map
app = Flask(__name__)


@app.route('/')
def index():
    html_table = ParseEarthQuake().mobile_df
    return render_template('index.html', html_table=html_table)


@app.route('/howto')
def howto():
    return render_template('howto.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/map')
def map():
    df = ParseEarthQuake().df
    return render_template('map.html', map_plot=plot_map(df))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
