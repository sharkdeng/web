import tornado.web
import tornado.httpserver
import tornado.gen
import tornado.ioloop
import tornado.httpclient
import asyncio
import aioredis
import redis
import os 
import logging
import base64 
from tornado.options import define, options
#define('port', default=3400, help='run port', type=int)
'''
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="forum", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="passwd", help="database password")
'''


settings = {
    'static_path': os.path.join(os.path.dirname('__file__')),
    'template_path': os.path.join(os.path.dirname('__file__')),
    'gzip': True,
    'debug': True,
    'cookie_secret': 'hello',
    'xsrf_cookie': True,
    'login_url': '/login'
}


def base64_img():
    '''Get all fills' base64, return in a list
    '''
    img_base64 = []
    src_path = os.path.abspath(os.path.dirname('__file__'))
    src_path = src_path.split('/')
    src_path.pop()
    src_path.append('sample1_react') # parent directory
    src_path[0] = '/' 
    src_path = os.path.join(*src_path) # list to str
    print('hello')
    print(src_path)
    imgs = os.listdir(src_path)
    for img in imgs:
        fn = os.path.join(src_path, img)
        if os.path.isfile(fn) and os.path.splitext(fn)[1] == '.jpg': # get suffix
            print('ok', fn)
            with open(fn, 'rb') as f:
                base64_data = base64.b64encode(f.read())
                img_base64.append(base64_data)
    return img_base64



class Base64Handler(tornado.web.RequestHandler):
    def get(self):
        imgs = base64_img()
        self.render('./base64.html', imgs=imgs)
        
