'''
Author: BDFD
Date: 2022-02-03 15:32:30
LastEditTime: 2022-02-03 15:33:19
LastEditors: BDFD
Description: 
FilePath: \flask-framework\app.py
'''
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=5000)
