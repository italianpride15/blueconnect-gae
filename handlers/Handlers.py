from webapp2_extras.routes import RedirectRoute

from IndexHandler import IndexHandler

handlers = [
    RedirectRoute('/', handler=IndexHandler, name='Index', strict_slash=True)
]