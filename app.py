import web
from utils.wechat import valid_request

urls = (
    '/(.*)', 'hello'
)

app = web.application(urls, globals())
application = app.wsgifunc()

class hello:
    def GET(self, name):
        data = web.input()
        if not valid_request(data):
            return web.notfound()
        return data.get('echostr')

if __name__ == "__main__":
    app.run()
