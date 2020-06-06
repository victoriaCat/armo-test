import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)


    def get(self):
        self.write("[{\"prop\": \"Lorem ipsum dolor sit amet, consectetur adipiscing elit\"}, {\"prop\": \"Cras cursus posuere lorem, quis efficitur urna dignissim ac\"}, {\"prop\": \"Duis scelerisque eu sem vulputate feugiat\"}]")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()