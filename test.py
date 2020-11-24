from flask import Flask, jsonify, request , render_template
app = Flask(__name__,static_url_path='/static')

@app.route('/login')
def login():
    email = request.args.get('email_address')
    password = request.args.get('pw')
    print(email, password)

    if email =='lee@naver.com':
        return_data = {'auth':'success'}
    else:
        return_data = {'auth':'failed'}
    return jsonify(return_data)

@app.route('/')
def index():
    return render_template('logincss.html')

if __name__ =='__main__':
    app.run(host="localhost", port="8080")