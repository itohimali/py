from flask import Flask

app=Flask(__name__)

@app.route('/')

def webout():

 return '<h1>This is develop branch.</h1>'

app.run(host='0.0.0.0',port=7000)
 