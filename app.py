from flask import Flask  
import requests
from user_recs import main_app
from gra import grap
from recc_w_fac import recc_fac

app = Flask(__name__) #creating the Flask class object   

      
@app.route('/') #decorator drfines the   
def home():  
    suggested_stocks = main_app("C1")
    #grap(stk_name)
    return suggested_stocks
  
if __name__ =='__main__':  
    app.run(debug = False,port=71)  