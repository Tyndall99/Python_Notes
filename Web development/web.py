from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Show_projects():
    return render_template("index.html")

app.run(debug=True, host="192.168.1.4", port=3000)