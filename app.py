from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World this flask</p>"

@app.route("/products")
def hello_products():
    return render_template("index.html")

@app.route("/about")
def hello_about():
    return "<p>Hello, World this About us</p>"

if __name__ == "__main__":
    app.run(debug=True,port=8000)
