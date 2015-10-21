import hashlib
import settings
import memcache

cache = memcache.Client(settings.MEMCHACHE_HOSTS)

def key_of_jsapi_ticket():
    return "wechat_key_of_jsapi_ticket"

def key_of_user_grade(name, ticket):
    return hashlib.sha1(name.encode('utf8') + ticket.encode('utf8')).hexdigest()
