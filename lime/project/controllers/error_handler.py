
import bottle
from bottle import view


@bottle.error(404)
@view('404')
def handle_404(err):
    return dict(csf="../resources/css/register.css")


@bottle.error(500)
@view('500')
def handle_500(err):
    return dict(csf="../resources/css/register.css")