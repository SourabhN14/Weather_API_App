import pandas as pd
from flask import Flask , render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    temperature =df.loc[df["    DATE"]==date]['   TG'].squeeze() / 10
    df2 = pd.read_csv("data_small/stations.txt", skiprows=17)
    station_desc = df2.loc[(df2['STAID'] == int(station))]['STANAME                                 '].squeeze()
    #temperature = 23
    #return render_template("about.html")
    return {"station": station,
            "date": date,
            "temperature": temperature,
            "station_name" : station_desc.strip()}

if __name__ == "__main__":
     app.run(debug=True,port=5000)
     # if you want to run multiple flask app you can use different port
     # 5000 is default port