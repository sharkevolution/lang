# -*- coding: UTF-8 -*-

import bottle
from bottle import view

@bottle.route('/login')
@view('register')
def registration():
    return None