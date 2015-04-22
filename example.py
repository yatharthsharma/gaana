from gaana import gaana 
import hashlib
import md5
import hmac
import base64

gaana_obj = gaana()
# m = md5.new()

# key = m.update(gaana_obj.getUserToken()['key'])



# token =  gaana_obj.getUserToken()
# print token
data = hmac.new(gaana_obj.getUserToken()['key'],(gaana_obj.getUserToken()['regtoken']).encode('base64'), hashlib.md5).hexdigest()
print gaana_obj.registerUser(key=gaana_obj.getUserToken()['key'],regtoken=data,fullname="yatharth",email="yatharth.sharma@gmail.com",password="yatharth",gender="male" )