import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error


dic={'rooms':[1,2,3,4,5,6,7,1,5,6,3,5,63,6,4,8,6,31],
    'area':[60.5,100.8,400.4,541.1,680.3,745.4,900.9,70.4,700.80,200.4,690.15,10000.47,800.21,500.54,6000.87,840.15,900.6,6000],
    'pool':[0,0,0,0,0,0,1,0,1,1,1,2,3,2,1,1,2,1],
   'posize':[0,0,0,0,0,0,500,0,450,480,423,460,900,1500,800,500,500,1000],
    'rodeside':[1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0],
    'houseavg':[35,25,41,55,61,32,44,96,63,43,21,15,83,85,23,78,50,60],
    'edu':[0,1,1,1,1,0,1,0,10,1,0,10,1,1,0,410,1,0],
    'electcity':[1,0,1,1,1,1,2,1,0,1,0,10,1,0,1,0,1,14],
    'borwat':[1,0,1,0,1,0,5,0,1,0,432,0,40,520,41,0,10,10],
    'drinkwat':[1,0,10,10,1,10,10,10,10,163,0,10,11,1,1,5,0,4],
    'saleprice':[23000,20000,40000,50000,35000,45000,100000,20000,60000,50000,20300,80400,500004,70000,82100,41000,270400,320000]}


df=pd.DataFrame(dic)


X=df[['rooms','area','pool','posize','rodeside','houseavg','edu','electcity','borwat','drinkwat']]
y=df['saleprice'] 

train_X,test_X,train_y,test_y=train_test_split(X,y,random_state=0)

def predicts(max_leaf,train_X,train_y,test_X):
     predict_list=[]
     
     model=DecisionTreeRegressor(max_leaf_nodes=max_leaf,random_state=1)
     model.fit(train_X,train_y)
     predict_values=model.predict(test_X)
    #  predict_list.append(predict_values)
    #  mae=mean_absolute_error(test_y,predict_values)
    
     return predict_values

# nodes=[20,30,40,41,42,45,50,60,80,100,120]
# error=[get_mae(x) for x in nodes]
# dic={}
# for k,v in zip(error,nodes):
#     dic[k]=v
# a=min(dic.keys())

# dic.get(a)
# print((120,train_X,train_y,test_X))

# encrypt and decrypt

def encrypts(k,v):
 try:
    a=[chr(i) for j in range(10) for i in range(97,123)]
    st=""
    for i in k:
        index=a.index(i)
       

        st=st+a[index+v]
    return st
        # return inputs(encrypt)(k,v)
    # else:
    #     @inputs
 except Exception as e:
     print(e)  

def decrypts(k,v):
  try:
    a=[chr(i) for i in range(97,123)]
    st=""
    for i in k:
        index=a.index(i)
        st=st+a[index-v]
    return st
  except Exception as e:
      print(e)

print(encrypts("ajay",4))
