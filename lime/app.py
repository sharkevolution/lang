#!/usr/bin/python

# https://vovkd.github.io/gevent-tutorial/
# https://learn.javascript.ru/xhr-longpoll
# http://shpargalkablog.ru/2015/08/window-location-js.html
# https://github.com/aaugustin/websockets
# https://realpython.com/blog/python/the-model-view-controller-mvc-paradigm-summarized-with-legos/

# https://codeguida.com/post/157/

# http://timeweb.com/ru/community/articles/kak-ispolzovat-postgresql-c-prilozheniem-django-na-ubuntu-16-04
# http://eax.me/python-postgresql/
# https://postgrespro.ru/docs/postgresql/9.6/tutorial-createdb.html
# https://www.djangosites.org/s/python-web-id/

import os

from lime.project import app

import bottle
from bottle import static_file
import cherrypy
import wsgigzip

# from gevent import monkey;

# monkey.patch_all()
from gevent.pywsgi import WSGIServer
# from geventwebsocket.handler import WebSocketHandler


@bottle.route('/resources/<action>/<filepath:path>')
def server_static(action, filepath):
    return static_file(filepath, root='./project/resources/' + action + '/')


# @bottle.route('/resources/bootstrap/<action>/<filepath:path>')
# def server_static(action, filepath):
#     return static_file(filepath, root='./project/resources/bootstrap/' + action + '/')


host = "0.0.0.0"
port = 8000

# server = WSGIServer((host, port), app)
# server = WSGIServer((host, port), app, handler_class=WebSocketHandler)
# print("access @ http://{0}:{1}/websocket.html".format(host, port))
# server.serve_forever()

# app = wsgigzip.GzipMiddleware(bottle.default_app())

cherrypy.config.update({'server.socket_host': "0.0.0.0",
                        'server.socket_port': int(os.environ.get("PORT", 5000))})
cherrypy.tree.graft(app)
cherrypy.engine.start()
cherrypy.engine.block()

