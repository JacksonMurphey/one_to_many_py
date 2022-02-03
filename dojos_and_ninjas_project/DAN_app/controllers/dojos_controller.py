from DAN_app import app
from flask import render_template, redirect, request
from DAN_app.models.dojo import Dojo
from DAN_app.models.ninja import Ninja


@app.route('/')
def index():
    #we will user this for login and registration
    return redirect('/dashboard')

@app.route('/dojos')
def dojo_dash():
    dojos = Dojo.get_all()
    return render_template('dojos_dash.html', dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    Ninja.get_one_with_dojo(data) #this is really not serviing any pursose here. 
    dojo = Dojo.get_one_with_user(data)
    return render_template('dojos_view.html', dojo=dojo)