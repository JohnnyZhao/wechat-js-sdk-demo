import settings
import memcache

cache = memcache.Client(settings.MEMCHACHE_HOSTS)

def key_of_jsapi_ticket():
    return "wechat_key_of_jsapi_ticket"
