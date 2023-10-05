import mysql.connector

class ConnectDB:
    global mydb
    mydb = mysql.connector.connect(
        host="buildybee.freedynamicdns.org",
        port="5002",
        user="go_auth_test",
        password="go_auth_test",
        database="go_auth_test"
    )
    global mycursor; 
    mycursor=mydb.cursor()

###########################################################################################
    def createuser(self,mail,pswd):
        resp=""
        sql_check = "SELECT USERID FROM USER WHERE EXIST(SELECT * FROM USER WHERE EMAILID = %s)"
        val_check = (mail)
        mycursor.execute(sql_check,val_check)
        result = mycursor.fetchall()
        if(result==True):
            resp= "User Already Exist"
            return resp
        else:
            sql_create = "INSERT INTO USER (emailid,passwrd) VALUES (%s,%s)"
            val=(mail,pswd)
            mycursor.execute(sql_create,val)
            #test = mycursor.fetchall()
            mydb.commit()
            #print("my cursor - ",test)
            resp= mycursor.rowcount+" user created"
            # for x in mycursor:
            #     resp+= x
            mydb.close()
        return resp
#######################################################################################   
    def send_otp(self,mail):
        pass

######################################################################################

    def frgtpswd(self,mail):
        pass

#######################################################################################
    def login(self,mail,pswd):
        resp=""
        sql = "SELECT USERID FROM USER WHERE EMAILID = %s AND PASSWRD=%s"
        val=(mail,pswd)
        mycursor.execute(sql,val)
        resp = mycursor.fetchall();
        #mydb.commit()
        if(len(resp)>0):
            resp = resp[0][0]
        else:
            resp = 0
        #mydb.close()
        return resp