import tornado.ioloop
import tornado.web
import io
import cv2

class SendImage(tornado.web.RequestHandler):
    def get(self, slug=None):
        self.set_header('Content-Type', 'image/jpg')
        stream = io.BytesIO()
        cap = cv2.VideoCapture(0)
        ret, image = cap.read()
        ret, encoded = cv2.imencode('.jpg',image)
        stream.write(encoded)
        with open('img.jpg','w') as f:
            f.write(encoded)
        print(encoded)
        stream.seek(0)
        self.write(stream.read())
        cap.release()

application = tornado.web.Application([
    (r'/([^/]*)', SendImage),
    ])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
