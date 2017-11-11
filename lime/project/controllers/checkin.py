
import bottle
from bottle import view

@bottle.route('/login')
@view('register')
def registration():
    return None