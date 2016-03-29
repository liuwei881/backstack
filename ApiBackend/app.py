# -*- coding: utf-8 -*-

__author__ = 'Hipeace86'
__datetime__ = '15-4-13'

import sys

import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado.options import options, define, parse_command_line
import os

import task.Handler.taskHandler
import task.Handler.tasklogHandler
import task.Handler.typesHandler
import Users.Handler
import server.Handler.serverHandler
from lib.LoginHandler import LoginHandler

from lib.urlmap import urlmap
from lib.Route import db_session


class Application(tornado.web.Application):
    def __init__(self):
        handlers = tuple(urlmap.handlers)
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "tpl"),
            debug=True,
            xsrf_cookies=False,
            autoescape=None,
            login_url='/login',
            cookie_secret='61oETXKXQAGaYdkL8gEmGEJJFuYh7FQnp2XdTP1o/Vo=',
        )
        self.db = db_session
        tornado.ioloop.PeriodicCallback(self._ping_db, 4 * 3600 * 1000).start()
        tornado.web.Application.__init__(self, handlers, **settings)

    def _ping_db(self):
        self.db.execute('show variables')
        self.db.remove()


define('port', type=int, default=4002)


def main():
    parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
