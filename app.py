from flask import Flask, render_template, redirect, request

app = Flask(__name__)

friends = ["hitesh", "tejas", "yash", "this", "that", "me"]

@app.route('/')
def index():
    return render_template("index.html", friends= friends)

@app.route('/about')
def about():
    return "<h1>About</h1>"

@app.route('/home')
def home():
    return redirect('/')

@app.route('/submit', methods = ['POST'])
def submit_data():
    if request.method == 'POST':
        print(request.form)
        name = request.form['username']
        f = request.files['userfile']
        print(f)
        f.save(f.filename)
        return "<h1>"+ name +"<h1>"

    return "Nothing"


if __name__ == '__main__':
    app.run(debug=True)