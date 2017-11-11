
import bottle
from bottle import view


# @bottle.route('/fff')
# @view('websocket')
# def send_html():
#     return None
#
#
# @bottle.route('/test')
# def test():
#     s = bottle.request.environ.get('beaker.session')
#     s['test'] = s.get('test', 0) + 1
#     s.save()
#     return 'Test counter: %d' % s['test']


@bottle.route('/')
@view('index')
def index():
    return dict(csf="resources/css/styles.css")




