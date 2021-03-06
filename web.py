from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    name = request.values.get('name')
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run()