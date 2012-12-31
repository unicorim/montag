import web
from web.contrib.template import render_jinja
import os

urls = (
	'/', 'index',
	'/(\d+)', 'article',
)

src_path = "../monologue"
app = web.application(urls, globals())
render = render_jinja(
	'templates',
	encoding='utf-8',
)

class index:
	def GET(self):
		return "Hi, this is montag. Read later for intro docs"
		
class article:
	def GET(self, no):
		try:
			article = open(os.path.join(src_path, "%s.txt" % no), 'r').read()
			return render.article(no=no, article=article)
		except IOError:
			return "Dear admin,\nplease fix this 404\nthx,\nmontag"
		
if __name__ == "__main__":
	app.run()
