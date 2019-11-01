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
define('port', default=3400, help='run port', type=int)

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
    src_path.append('react')
    src_path[0] = '/'
    src_path = os.path.join(*src_path)
    print('hello')
    print(src_path)
    imgs = os.listdir(src_path)
    for img in imgs:
        fn = os.path.join(src_path, img)
        if os.path.isfile(fn) and os.path.splitect(fn)[1] == '.png':
            print('ok', fn)
            with open(fn, 'rb') as f:
                base64_data = base64.b64encode(f.read())
                img_base64.append(base64_data)
    print(img_base64)
    return img_base64
