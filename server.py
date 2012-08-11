#!/usr/bin/env python

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", Handler),
        ]

        settings = dict(
            cookie_secret="43oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            xsrf_cookies=True,
            autoescape=None,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class Handler(tornado.websocket.WebSocketHandler):
    clients = set()
    positionY = 0
    speed = 100

    def open(self):
    	print "WebSocket opened"
        Handler.clients.add(self)

    def on_close(self):
    	print "WebSocket opened"
        Handler.clients.remove(self)

    @classmethod
    def send_updates(cls, text):
        logging.info("sending message to %d waiters", len(cls.clients))

        if text == 'moveUp':
            cls.positionY = cls.positionY-cls.speed
        elif text == 'moveDown':
            cls.positionY = cls.positionY+cls.speed

        for client in cls.clients:
            try:
                client.write_message(str(cls.positionY))
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r", message)
        Handler.send_updates(message)

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()