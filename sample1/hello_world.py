#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:53:59 2019

@author: dph
"""

# Reference: https://github.com/rudyryk/python-samples/blob/master/hello_tornado/hello_world.py

# hello_world.py
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world! Shout to tornado")


class JsonHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({
            'status': 'OK',
            'text': "Hello, world"
        })


app = tornado.web.Application([
    (r"/", MainHandler),
    (r"/json/", JsonHandler),
])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    
    
    
# [Errno 48] Address already in use
# sudo lsof -t -i tcp:8000 | kill -9 [pid]
