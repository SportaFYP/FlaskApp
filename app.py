from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def point():
     return render_template('point1.html')
    
if __name__ == "__main__":
    app.run(debug = True)