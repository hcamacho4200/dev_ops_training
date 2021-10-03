import logging

from flask import (
    Flask,
)
from werkzeug.middleware.proxy_fix import ProxyFix

from api.v1.api_v1 import blueprint as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1)
app.wsgi_app = ProxyFix(app.wsgi_app)

log = logging.getLogger(__name__)


def init_app(app):
    """init the flask application

    :param app:
    :return:
    """

    return app


if __name__ == '__main__':
    app = init_app(app)
    app.run(debug=True)
