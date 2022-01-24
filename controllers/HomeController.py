from app import app
from models.HomeModel import *
from flask import render_template,request,redirect,url_for,flash

import numpy as np


@app.route('/')
def index():

    participants = getParticipants()

    print(participants)
    return render_template('home.html')


@app.route('/stadistics')
def stad():
    if(len(getParticipants()) == 0):
        return render_template('std.html')
    else:
        print(getParticipants())
        datos = [
            [encuestasRespondidas()],
            [
             int(promedioSocial("time_facebook")[0]),
             int(promedioSocial("time_whatsapp")[0]),
             int(promedioSocial("time_twiter")[0]),
             int(promedioSocial("time_instagram")[0]),
             int(promedioSocial("time_tiktok")[0])
            ],
            [favoriteNetwork()],
            [networkDown()],
            [
                ['facebook',maxRangeFor(1)],
                ['Whatsapp',maxRangeFor(2)],
                ['Twiter',maxRangeFor(3)],
                ['Instagram',maxRangeFor(4)],
                ['Tik Tok',maxRangeFor(5)]
            ]
        ]
        return render_template('stadistics.html',datos=datos)



@app.route('/store', methods=['POST'])
def storage():

    name_participant = request.form['name_participant']
    email_participant = request.form['email_participant']
    age_participant = request.form['age_participant']
    favorite_network = request.form['favorite_network']
    gender_participant = request.form['gender_participant']
    time_facebook = request.form['time_facebook']
    time_whatsapp = request.form['time_whatsapp']
    time_twiter = request.form['time_twiter']
    time_instagram = request.form['time_instagram']
    time_tiktok = request.form['time_tiktok']


    if name_participant =='' or email_participant =='' or age_participant =='' or favorite_network =='' or gender_participant =='' or time_facebook =='' or time_whatsapp =='' or time_twiter =='' or time_instagram =='' or time_tiktok =='':
        flash('Recuerda llenar los campos completos')
        return redirect("/")

    
    datos = (name_participant,email_participant,age_participant,gender_participant,favorite_network,time_facebook,time_whatsapp,time_twiter,time_instagram,time_tiktok)

    setTest(datos)
    flash('Encuesta enviada correctamente')
    
    return redirect("/")


def encuestasRespondidas():
    participantcount = countTest()
    return participantcount[0][0]

def promedioSocial(camp):
    campo=camp
    red = getProm(campo)
    arr = np.array(red)
    operation = sum(arr) / encuestasRespondidas()
    return operation





def favoriteNetwork():

    social = [getNetwork(1),getNetwork(2),getNetwork(3),getNetwork(4),getNetwork(5)]
    mx =max(social)
    posicion = social.index(mx)
    redes = getFavorite()
    return redes[posicion]
   
def getNetwork(rd):
    red=rd
    social = getNet(red)
    return social[0][0]
   
def networkDown():
    social = [getNetwork(1),getNetwork(2),getNetwork(3),getNetwork(4),getNetwork(5)]
    mx =min(social)
    posicion = social.index(mx)
    redes= getFavorite()
    
    return redes[posicion]

def maxRangeFor(social):
    rs = social
    rangos = (countRange(1,rs),countRange(2,rs),countRange(3,rs),countRange(4,rs))
    mx =max(rangos)
    if (mx > 0):
        posicion = rangos.index(mx)
        agess= getAge()
        return agess[posicion]
    else:
        return (0,'No hay registros')

def countRange(rng,rd):
    rango=rng
    red = rd
    social = getCountTime(rango,red)
    return social[0][0]
   
