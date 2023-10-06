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
    mycursor=mydb.cursor(buffered=True)

###########################################################################################
    def createuser(self,mail,pswd):
#if user exist return 0,if newly created return 1       
        resp=""
        sql_check = "SELECT USERID FROM USER WHERE EXISTS (SELECT * FROM USER WHERE EMAILID = %s)"
        val_check = [mail]
        mycursor.execute(sql_check,val_check)
        result = mycursor.fetchone()
        print(result)
        if(result!=None):
            resp= 0
            return resp
        else:
            sql_create = "INSERT INTO USER (emailid,passwrd) VALUES (%s,%s)"
            val=(mail,pswd)
            mycursor.execute(sql_create,val)
            #test = mycursor.fetchall()
            mydb.commit()
            #print("my cursor - ",test)
            resp= mycursor.rowcount
        #mydb.close()
        return resp
#######################################################################################   
    def send_otp(self,mail):
        pass

######################################################################################

    def frgtpswd(self,mail):
        pass

#######################################################################################
    def login(self,mail,pswd):
#if user exist return userid else return 0
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