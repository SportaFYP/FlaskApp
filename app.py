from flask import Flask, render_template
application = Flask(__name__)

app = application

@app.route("/")
def point():
     return render_template('point1.html')
    
if __name__ == "__main__":
    app.run(debug = True)
