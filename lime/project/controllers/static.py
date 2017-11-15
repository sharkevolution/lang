
import os
import bottle
from bottle import static_file

from lime.project import config


@bottle.route('/resources/<action>/<filepath:path>')
def server_static(action, filepath):
    root = os.path.join(config.RESOURCES_PATH, action)
    return static_file(filepath, root=root)

@bottle.route('/:file#(favicon.ico)#')
def favicon(file):
    return static_file(file, root='project/static/misc')


# @bottle.route('/:path#(images|css|js|fonts)\/.+#')
# def server_static(path):
#     return static_file(path, root='project/static')