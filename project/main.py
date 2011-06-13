from google.appengine.ext.webapp.util import run_wsgi_app

from comunidadorsai import app

if __name__ == "__main__":
    run_wsgi_app(app)
