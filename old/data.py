import os
import redis
import re

from development import DEBUG

URLProgram = re.compile('^redis:\/\/([^:]+):([^@]+)@(.*?):(.*?)\/(.*?)(\\?.*)?$')

if 'REDIS_APP_URL_STUNNEL' in os.environ:
    URLStunnel = os.environ['REDIS_APP_URL_STUNNEL']
else:
    import private
    URLStunnel = private.URLStunnel

def RedisConnectURL(url):
    result = URLProgram.match(url)
    user = result.group(1)
    password = result.group(2)
    host = result.group(3)
    port = result.group(4)
    name = result.group(5)
    settings = {'host':host, 'password':password, 'port':port, 'db':name}
    #if DEBUG:
    print 'Connecting to Redis server (%s)' % ', '.join(['%s=%s' % (k,v) for k, v in settings.iteritems()])
    return redis.StrictRedis(**settings)

def RedisConnectMain():
    return RedisConnectURL(URLStunnel)

Store = RedisConnectMain();