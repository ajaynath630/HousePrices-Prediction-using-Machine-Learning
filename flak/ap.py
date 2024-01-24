
from flask import Flask,render_template,abort,request,url_for,redirect
from impor import *
import numpy as np
app=Flask(__name__,template_folder='../templates',static_folder='../static')

lis={i*i for i in range(10)}
title="home"
@app.route('/')
def home():
    title="home"

    return render_template('index.html',lis=lis,title=title)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about')
@app.route('/hello')
def hello():
    name="ajay"
   
    return render_template('index.html',name2=name)

@app.route('/form')
def form():
    
    return render_template('form.html')

@app.route('/predict',methods=["POST","GET"])
def predict():
    dic=request.form

    df=np.array([k for k in request.form.values()]).reshape(1,-1)
    d=predicts(120,train_X,train_y,df)
    return render_template('result.html',saleprice=d,dic=dic)

@app.route('/cipher')
def cipher():
  return render_template('ciphere.html')

@app.route('/encrypt',methods=["POST","GET"])
def encrypt():
  if request.method == "POST":
   dic=request.form
   num=dic.get('key')
   print(num)
   value=encrypts(dic.get('string'),int(num))
   return render_template('encrypt-result.html',value=value,dic=dic)
 
  
 
@app.route('/decrypt',methods=["POST","GET"])
def decrypt():
   dic=request.form
   value=decrypts(dic['string'],int(dic['key']))
   return render_template('decrypt-result.html',value=value,dic=dic)

if __name__=="__main__":
  app.run(debug=True)
