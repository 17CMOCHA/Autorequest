import requests
from jsonpath_ng import parse
import  base64
from Crypto.Cipher import AES
headers={
    "application":"app",
    "application_client_type":"weixin"
}
params={
    "application":"app",
    "application_client_type":"weixin"
}
data={
    "accounts":"lxy",
    "pwd":"114514",
    "type":"username"
}
class EncryptDate:
    def __init__(self,key):
        self.key = key.encode('utf-8')
        self.length=AES.block_size
        self.aes=AES.new(self.key,AES.MODE_ECB)
        self.unpad=lambda date : date[0:-ord(date[-1])]
    def pad(self,text):
        count=len(text.encode('utf-8'))
        add=self.length-(count%self.length)
        entext=text+(chr(add)*add)
        return entext
    def encrypt(self,enryData):
        res = self.aes.encrypt(self.pad(enryData).encode('utf-8'))
        msg = str(base64.b64encode(res),'utf-8')
        return msg
    def decrypt(self,decrData):
        res=base64.decodebytes(decrData.encode('utf-8'))
        msg=self.aes.decrypt(res).decode('utf-8')
        return self.unpad(msg)
if __name__ == '__main__':
    print("=============加密============")
    key="1234567891011111"
    data="114514"
    username="lxy"
    eg=EncryptDate(key)
    resp=eg.encrypt(data)
    username1=eg.encrypt(username)
    print(resp,end="")
    response = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login_safe&password"+resp+"username"+username1,headers=headers)
    print(response.text)