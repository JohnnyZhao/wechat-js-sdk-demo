import web
from wechat_sdk.messages import EventMessage
from utils.wechat import valid_request, wechat_client
from utils.parser import parse_xml
from utils.cet import getScore
from utils.cache import key_of_user_grade, cache

urls = (
    '/chafen/', 'chafen',
    '/niu/', 'niu',
    '/niu', 'niu',
    '/ele/', 'ele',
    '/ele', 'ele',
    '/static/(.*)', 'static',
    '/(.*)', 'hello',
)

render = web.template.render('templates/')
app = web.application(urls, globals())
application = app.wsgifunc()

class static:
    def GET(self, name):
        try:
            f = open('static/' + name, 'r')
            return f.read()
        except:
            return web.notfound()

class hello:
    def GET(self, name):
        query = web.input()
        if not valid_request(query):
            return web.notfound()
        return query.get('echostr')

    def POST(self, name):
	data = web.data()
        query = web.input()
	if not valid_request(query):
            return web.notfound()
        wechat_client.parse_data(data)
        msg = wechat_client.get_message()
        if isinstance(msg, EventMessage):
            if msg.type == 'subscribe':
                wechat_client.response_text(content='hello, world!')
        return query.get('echostr')

class chafen:

    def GET(self):
        name = ticket = score = None
        return render.chafen(name, ticket, score)

    def POST(self):
        data = web.input()
        name = data.get('name')
        ticket = data.get('ticket')
        key = key_of_user_grade(name, ticket)
        score = cache.get(key)
        if not score:
            print "cannot get in cache"
            score = getScore({'xm': name.encode('utf8'), 'zkzh': ticket.encode('utf8')})
            print '61:', score
            if score != "error":
                cache.set(key, score)
        print "score:", score
        return render.chafen(name, ticket, score)


class niu:

    def GET(self):
        data = web.input()
        days = data.get('days')
        comment = data.get('comment')
        return render.niu(days, comment)

class ele:

    def GET(self):
        return render.ele()

if __name__ == "__main__":
    app.run()
