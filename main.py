from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def about():
    return render_template('products.html')

if __name__ == "__main__":
    app.run(debug=True)