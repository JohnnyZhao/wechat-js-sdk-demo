import random, string, time
import settings
from wechat_sdk import WechatBasic
from cache import cache, key_of_jsapi_ticket

wechat_client = WechatBasic(token=settings.WECHAT_TOKEN,
                           appid=settings.WECHAT_APPID,
                           appsecret=settings.WECHAT_APPSECRET)


def noncestr_generator(length):
    seed = string.letters + string.digits
    return ''.join(random.choice(seed) for i in range(length))

def valid_request(data):
    nonce = data.get('nonce', '')
    signature = data.get('signature', '')
    timestamp = data.get('timestamp', '')
    return wechat_client.check_signature(signature=signature, timestamp=timestamp, nonce=nonce)

def get_jsapi_ticket():
    key = key_of_jsapi_ticket()
    jsapi_ticket = cache.get(key)
    if not jsapi_tiket:
        ticket = wechat_client.get_jsapi_ticket()
        jsapi_ticket = data['jsapi_ticket']
        expires_at = data['jsapi_ticket_expires_at']
        timeout = expires_at - int(time.time())
        cache.set(key, jsapi_ticket, timeout)
    return jsapi_ticket


def wechat_config(path):
    domain = 'http://%s' % settings.DOMAIN
    data = {
        'appid': settings.WECHAT_APPID,
        'url': "%s%s" % (domain, path),
        'noncestr': noncestr_generator(16),
        'timestamp': int(time.time())
    }
    jsapi_ticket = get_jsapi_ticket()
    data['signature'] = str(wechat_client.generate_jsapi_signature(data['timestamp'], 
                                                                   data['noncestr'], 
                                                                   data['url'], 
                                                                   jsapi_ticket))
    return data
