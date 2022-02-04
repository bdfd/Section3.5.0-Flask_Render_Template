'''
Author: BDFD
Date: 2022-02-03 15:32:30
LastEditTime: 2022-02-04 12:55:40
LastEditors: BDFD
Description: 
FilePath: \Heroku_Python_Template\server.py
'''
from pickle import TRUE
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/blog')
def blog():
  posts = [
    {'title':'Technology in 2019', 'author':'avi'},
    {'title':'China is stronger than ever', 'author':'david'}
  ]
  return render_template(
    'blog.html', 
    author = 'bdfd', 
    sunny = True, 
    posts=posts)

if __name__ == '__main__':
  app.run()
