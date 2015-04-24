from gaana import gaana
import hashlib
from hashlib import md5
import hmac
import base64

gaana_obj = gaana()

data = hmac.new(hashlib.md5(gaana_obj.getUserToken()['key']).hexdigest(),(gaana_obj.getUserToken()['regtoken']).encode('base64'),hashlib.md5).hexdigest()
print gaana_obj.registerUser(key=gaana_obj.getUserToken()['key'],regtoken=data,fullname="yatharth",email="yatharth.sharma@gmail.com",password="yatharth",gender="male" )