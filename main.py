from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    #return render_template("about.html")
    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__ == "__main__":
     app.run(debug=True,port=5000)
     # if you want to run multiple flask app you can use different port
     # 5000 is default port