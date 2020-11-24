from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/<user>')

def hello_user(user):
    return render_template('loginva.html', name=user)

if __name__ =="__main__":
    app.run(host="localhost", port="8080")