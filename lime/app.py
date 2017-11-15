# -*- coding: UTF-8 -*-
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

# from gevent import monkey
# monkey.patch_all()
# from gevent.pywsgi import WSGIServer
# from geventwebsocket.handler import WebSocketHandler

import os
import cherrypy
import wsgigzip

from lime.project import app

host = "0.0.0.0"
port = int(os.environ.get("PORT", 5000))
def_app = wsgigzip.GzipMiddleware(app)
# app = wsgigzip.GzipMiddleware(bottle.default_app())

# --------------------------------------------------------------
cherrypy.config.update({'server.socket_host': host,
                        'server.socket_port': port})
cherrypy.tree.graft(def_app)
cherrypy.engine.start()
cherrypy.engine.block()
#----------------------------------------------------------------

# server = WSGIServer((host, port), def_app, handler_class=WebSocketHandler)
# server.serve_forever()

# https://gist.github.com/dusual/9838932