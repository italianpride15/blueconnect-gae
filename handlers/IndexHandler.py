from MainHandler import Handler

class IndexHandler(Handler):
    def get(self):
    	self.render('index.html')