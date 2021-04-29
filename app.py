""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""

from flask import Flask
import folium
import pandas as pd 

app = Flask(__name__)
sheet_id = "1LIVMgYfY-hb2tDujGGku9eBxxaCafvRaGZEqICYV6Q0"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

@app.route('/')
def index():
    latest_resources = pd.read_csv(url)
    start_coords = (21.1458, 79.0882)
    folium_map = folium.Map(location=start_coords, zoom_start=5)
    print (latest_resources.columns.values)
    for idx, row in latest_resources.iterrows():
        folium.Marker([row['Lat'], row['Long']], popup="<b>{}</b>: Verified on {} at {} and confirmed: {}".format(row['Name'], row['Verification Date'], row['Verification Time'], row['Status'])).add_to(folium_map)
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)