from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/loop')
def loop():
    value_list = ['list1','list2','list3']
    return render_template ('loop.html',values = value_list)

if __name__=='__main__':
    app.run(host='localhost',port='8080')