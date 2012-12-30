import web

urls = (
	'/', 'index',
	'/(\d+)', 'article',
)

app = web.application(urls, globals())

class index:
	def GET(self):
		return "Hi, this is montag. Read later for intro docs"
		
class article:
	def GET(self, no):
		return "Hi, you are reading article no. " +  no
		
if __name__ == "__main__":
	app.run()
