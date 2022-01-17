import os
import tornado.ioloop
import tornado.web
import config
import random

from random import randint
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

port = config.port
name = config.name
## TEMPORARY FILEPATHS
ffpath = "static/ff"
nekoirlpath = 'static/nekoirl'
bdsmpath = "static/bdsm"
catboypath = 'static/catboy'
hentaipath = "static/hentai"
trollpath = 'static/troll'
furrypath = 'static/furry'
nekopath = 'static/neko'
feetpath = 'static/feet'
trappath = 'static/trap'
gifpath = 'static/gif'
futapath = 'static/futa'


## Shite if statement
if config.localhost == True:
	urlglobal = f'localhost:{port}'
else:
	urlglobal = f'http://api.xsky.dev'


class MainHandler(RequestHandler):
    def get(self):
        self.render("index.html")


class HentaiHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(hentaipath)))
		url = f"{urlglobal}/hentai/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()

class TrollHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(trollpath)))
		url = f"{urlglobal}/troll/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()

class CatboyHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(catboypath)))
		url = f"{urlglobal}/static/catboy/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()
		
class BdsmHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(bdsmpath)))
		url = f"{urlglobal}/static/bdsm/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()

class FurryHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(furrypath)))
		url = f"{urlglobal}/static/furry/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()
		
class FFHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(ffpath)))
		url = f"{urlglobal}/static/ff/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()

class NekoIRLHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(nekoirlpath)))
		url = f"{urlglobal}/static/nekoirl/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()

class NekoHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(nekopath)))
		url = f"{urlglobal}/static/neko/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()

class FeetHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(feetpath)))
		url = f"{urlglobal}/static/feet/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()

class TrapHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(trappath)))
		url = f"{urlglobal}/static/trap/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()

class FutaHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(futapath)))
		url = f"{urlglobal}/static/futa/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()

class GifHandler(RequestHandler):
	def get(self):
		image_id = str(random.choice(os.listdir(gifpath)))
		url = f"{urlglobal}/static/gif/" + image_id
		
		self.set_header("Content-Type", "application/json")
		self.write({"url":url})
		self.finish()


def make_app():
	settings = dict(
        static_path=os.path.join(os.path.dirname(__file__), "static")
    )
	app = Application([
		(r"/", MainHandler),
		(r"/hentai", HentaiHandler),
		(r"/troll", TrollHandler),
		(r"/bdsm", BdsmHandler),
		(r"/catboy", CatboyHandler),
		(r"/furry", FurryHandler),
		(r"/ff", FFHandler),
		(r"/nekoirl", NekoIRLHandler),
		(r"/neko", NekoHandler),
		(r"/feet", FeetHandler),
		(r"/trap", TrapHandler),
		(r"/gif", GifHandler),
		(r"/futa", FutaHandler)
	], **settings)
	return app

if __name__ == "__main__":
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
