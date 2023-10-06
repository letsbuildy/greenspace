from flask import Flask,request,jsonify
import dbconn
app= Flask(__name__)

@app.route('/createUser', methods = ['GET'])
def createUser():
    mail = request.args.get('mail')
    pswd = request.args.get('pswd')
    #username= request.args.get('username')
    cnn =  dbconn.ConnectDB()
    resp = cnn.createuser(mail,pswd)
    return jsonify({"response":resp})

@app.route('/frgtpswd',methods = ['GET'])
def frgtpswd():
    #1.first user exist or not needed to checked
    #2.if exist otp will be sent to mail id
    #3.same otp will be sent to front-end too(Efficient) or matching can be done at backend
    #4.after that new password is given and updated
    pass


@app.route('/login',methods = ['GET'])
def login():
    mail = request.args.get('mail')
    pswd = request.args.get('pswd')
    conn= dbconn.ConnectDB()
    resp = conn.login(mail,pswd)
    return jsonify({"response": resp})


if __name__ == '__main__':
    app.run(debug=True, port=8000)


#http://127.0.0.1:8000/createUser?mail=abc@gmail.com&pswd=secrete