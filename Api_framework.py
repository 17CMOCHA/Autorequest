import jsonpatch
import requests
from jsonpath_ng import parse

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
data2={
    "goods_id":"2",
    "spec":[
        {
            "type":"套餐",
            "value":"套餐2"
        },
        {
            "type":"颜色",
            "value":"银色"
        },
        {
            "type":"容量",
            "value":"64G"
        }
    ],
    "stock": 2
}
data3={
    "id":"12",
}
def send_request(url,method,params,data):
    res=requests.request(url=url,method=method,params=params,data=data)