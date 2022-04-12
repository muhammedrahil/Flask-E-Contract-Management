from flask import *
from werkzeug.utils import secure_filename



app=Flask(__name__)

from src.dbconnection import *


@app.route('/login', methods=['get'])
def login():
    print(request.args)
    name = request.args.get('username')
    password = request.args.get('password')
    print(name)

    res = ("select * from login where username =%s and password=%s and usertype='user'")
    val = (name, password)
    ss = selectone(res, val)
    print(ss)
    if ss is not None:
        print(ss)
        return jsonify({'m': ss[0], 'res': "true"})
    else:
        print("kkkkkk")
        return jsonify({'res': "false"})

@app.route('/user', methods=['get'])
def user():
    print(request.args)
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    place = request.args.get('place')
    post = request.args.get('post')
    pin = request.args.get('pin')
    phone = request.args.get('phone')
    uname = request.args.get('username')
    password = request.args.get('password')
    print(uname,password)
    qry = "insert into login values(null,%s,%s,'user')"
    val = (uname, password)
    id = iud(qry, val)
    qryuser = ("insert into user VALUES (null,%s,%s,%s,%s,%s,%s,%s)")
    val = (str(id), fname, lname, place, post, pin, phone)
    iud(qryuser, val)
    return jsonify({'res': "true"})


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
