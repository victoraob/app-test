from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='social_networks'
mysql.init_app(app)



def getParticipants():
    sql= "SELECT * FROM `participants`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    participants= cursor.fetchall()
    conn.commit()

    return participants

def setTest(datos):
     sql= "INSERT INTO `participants` (id_participant,name_participant,email_participant,age_participant,gender_participant,favorite_network,time_facebook,time_whatsapp,time_twiter,time_instagram,time_tiktok) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
     datos = datos
     conn=mysql.connect()
     cursor=conn.cursor()
     cursor.execute(sql,datos)
     conn.commit()
     return True


def countTest():
    sql= "SELECT COUNT(*) as id_participant FROM participants"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    participantcount= cursor.fetchall()
    conn.commit()
    return participantcount

def getProm(campo):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT "+campo+" FROM participants;")
    red= cursor.fetchall()
    return red

def getFavorite():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `networks`;")
    redes= cursor.fetchall()
    return redes


def getNet(red):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) as id_participant FROM participants WHERE favorite_network = %s",red)
    social = cursor.fetchall()
    return social

def getAge():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `ages`;")
    agess= cursor.fetchall()
    return agess

def getCountTime(rango,red):
    sql ="SELECT COUNT(*) as id_participant FROM participants WHERE age_participant=%s AND favorite_network = %s;"
    datos=(rango,red)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    social = cursor.fetchall()
    return social