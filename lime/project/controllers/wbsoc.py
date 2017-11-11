
import bottle
from bottle import request, abort

from geventwebsocket import WebSocketError


@bottle.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    hst = request.headers.get('host')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()
            wsock.send("Your message was: %r" % message)
            # wsock.send("Your message was: %r" % message)
        except WebSocketError:
            print('error no data')
            break


