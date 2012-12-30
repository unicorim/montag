import web
import os

urls = (
	'/', 'index',
	'/(\d+)', 'article',
)

src_path = "../monologue"
app = web.application(urls, globals())

class index:
	def GET(self):
		return "Hi, this is montag. Read later for intro docs"
		
class article:
	def GET(self, no):
		#try:
		article = open(os.path.join(src_path, "%s.txt" % no), 'r')
		return article.read()
		#except IOError:
		#	return "Trying to read article no. " + no
		
if __name__ == "__main__":
	app.run()
