from flask import Flask,render_template

app = Flask(__name__)

jobs = [
    {
        'id':1,
        'title':"Data Analyst",
        'location':"Bengaluru, India",
        'salary':"₹10,0000"
    },
    {
        'id':2,
        'title':"Data Scientist",
        'location':"San Fransisco, USA",
        'salary':"₹15,0000"
    },
    {
        'id':3,
        'title':"Software Engineer",
        'location':"Delhi, India",
        'salary':"₹13,0000"
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html",jobs=jobs)

if __name__ == "__main__":
    app.run("0.0.0.0",debug=True)