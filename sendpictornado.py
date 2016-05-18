import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self, slug=None):
        self.set_header('Content-Type', 'image/jpg')
        f = open('hoge.jpg','rb')
        self.write(f.read())
        f.close()

application = tornado.web.Application([
    (r'/([^/]*)', MainHandler),
    ])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
