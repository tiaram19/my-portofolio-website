import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask,render_template,request,jsonify


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)