import os,sys
import tornado.web
import tornado.httpserver
import tornado.ioloop
import logging

from  tornado.options import define,options

define('port',80,int,'Web Port Required')

def init_logging():
    access_log = logging.getLogger('tornado.access')
    access_log.propagate = False
    # make sure access log is enabled even if error level is WARNING|ERROR
    access_log.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(
        logging.Formatter("[%(name)s][%(asctime)s][%(levelname)s][%(pathname)s:%(lineno)d] > %(message)s"))
    access_log.addHandler(stdout_handler)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        h1color = os.getenv('H1COLOR',"red")
        self.render('book.html',h1color=h1color,publisher="BBC",author="James Eiams",books=['Introduction to docker','Kickstart with Saltstack','Learning python'])

class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('health.html')


if __name__ == '__main__':
    init_logging()
    app = tornado.web.Application([(r'/',IndexHandler),
                                   (r'/health/full',HealthCheckHandler),
                                   (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': 'css'})])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()