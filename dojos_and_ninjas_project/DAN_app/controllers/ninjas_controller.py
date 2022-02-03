from flask.helpers import url_for
from DAN_app import app
from flask import render_template, redirect, request, session
from DAN_app.models.dojo import Dojo
from DAN_app.models.ninja import Ninja


@app.route('/ninjas')
def ninja_dash():
    dojos = Dojo.get_all()
    return render_template('ninjas_view.html', dojos=dojos)


@app.route('/ninjas/create', methods=["POST"])
def ninja_create():
    dojo_id = request.form['dojo_id']
    Ninja.save(request.form)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/ninjas/hidden/<int:dojo_id>')
def ninja_pass(dojo_id):
    data = dojo_id
    Dojo.get_one_with_user(data)
    return redirect(f'/dojos/{dojo_id}')