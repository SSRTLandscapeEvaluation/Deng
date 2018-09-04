from flask import Flask,render_template,url_for,request,sessions
from config import DevConfig
from exts import db
from models import Imageseval ,imagesinfodf
import pandas as pd
import sqlite3
from conversionofCoordi import wgs84togcj02 , gcj02tobd09
from imgPred_recognizer import predConfig
from imgPred_training import ERFTrainer
import cv2
import os


app=Flask(__name__)#实例化Flask类
app.config.from_object(DevConfig)
db.init_app(app)

#db.create_all(

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results/')
def results():
    evalResults = [{'name':imagename.split('/')[-1][:-4],'value': good + 100}
                   for imagename , good in db.session.query(Imageseval.imagename,Imageseval.good).all()]
    #print(evalResults)
    locationResults = {imagename.split('/')[-1][:-4]:
                           gcj02tobd09(wgs84togcj02(long , lat)[0], wgs84togcj02(long,lat)[1])
                       for imagename, long, lat in db.session.query(imagesinfodf.imagename, imagesinfodf.long, imagesinfodf.lat).all()}
    #print(locationResults)
    imgLocVal = {'imgLoc':locationResults,
                 'imgVal':evalResults}
    return render_template('results.html',**imgLocVal)

@app.route('/eval/', methods=['GET','POST'])#给图像打分
def eval():
    #print(imagesinfodf.query.get(1).imagename)
    context = {'imgEval': imagesinfodf.query.all(), 'imgNum':len(imagesinfodf.query.all())}
    #print(context)
    if request.method == 'GET':
        return render_template('eval.html', **context)
    else:
        image_name = request.form.get('image_path')
        imaIdx = request.form.get('image_id')
        evalRX = int(request.form.get('eval'))
        #print(image_name,imaIdx,evalRX)
        imgCurrent =Imageseval.query.filter(Imageseval.imagename == image_name).first()
        #print(Imageseval.query.get(1).imagename)
        #print(imgCurrent)
        if evalRX ==1:
            print('ok')
            goodV=1
            mediumV=0
            poorV=0
            evalV=u'好'
        elif evalRX == -1:
            goodV=0
            mediumV=0
            poorV=1
            evalV=u'差'
        elif evalRX ==0:
            goodV=0
            mediumV=1
            poorV=0
            evalV=u'中'
        else:
            pass

        if not imgCurrent:
            imagesevalData = Imageseval(imagename=image_name, good=goodV,medium=mediumV,poor=poorV,eval=evalV)
            db.session.add(imagesevalData)
            db.session.commit()
        else:
            queryResults = [(good,medium,poor) for good,medium,poor in db.session.query(Imageseval.good,Imageseval.medium,Imageseval.poor).filter(
                Imageseval.imagename == image_name)]
            print(queryResults)
            goodAdd = queryResults[0][0] + goodV
            mediumAdd = queryResults[0][1] + mediumV
            poorAdd = queryResults[0][2] + poorV
            if goodAdd >mediumAdd and goodAdd<poorAdd:
                evalN=u'好'
            elif mediumAdd> goodAdd and mediumAdd> poorAdd:
                evalN=u'中'
            elif poorAdd> goodAdd and poorAdd> mediumAdd:
                evalN=u'差'
            else:
                evalN='中'
            imagesevalDic = {'good':goodAdd,'medium':mediumAdd,'poor':poorAdd,'eval':evalN}
            print(imagesevalDic)
            Imageseval.query.filter_by(imagename=image_name).updata(imagesevalDic)
            #db.session.add(imagesevalData)
            db.session.commit()
    return render_template('eval.html', **context)


'''预测路由'''
@app.route('/imgprediction/')
def imgprediction():
    predInfo = predConfig().pred()
    #print(predInfo)
    #predDic={'predName':predInfo.keys(),'predValue':predInfo.values()}
    predDic = {'pred':[(key,predInfo[key]) for key in predInfo.keys()]}
    return render_template('imgprediction.html', **predDic)
if __name__=='__main__':
    app.run()