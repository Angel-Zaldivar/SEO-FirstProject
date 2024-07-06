from flask import Flask, render_template, request

app = Flask(__name__) #initializes the flask epplication

@app.route('/')
def home():
    return render_template('home.html', title='Home Page')



if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")