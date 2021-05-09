from flask import Flask, request, make_response, jsonify, render_template, url_for, flash, redirect, send_from_directory

app = Flask(__name__)

data={
    'sakshi':{
        'roll':52,
        'id':'TU3F1718057',
        'email':'sakshikale@ternaengg.ac.in',
        'img':'Sakshi.png'
     
    },
    'ritik':{
        'roll':54,
        'id':'TU3F1718059',
        'email':'ritikrahangdale@ternaengg.ac.in',
        'img':'Ritik.png'
    },'amresh':{
        'roll':53,
        'id':'TU3F1718058',
        'email':'amreshyadav@ternaengg.ac.in',
        'img':'Amresh.jpeg'
    }
}


@app.route('/')
def index():
  
    return render_template('/index.html')

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/experiments/')
def expts():
    name=request.args.get('name')
    return render_template('/expt.html',name=name,data=data[name])
    