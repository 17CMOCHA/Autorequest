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
def main():
    response = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",headers=headers,params=params,data=data)
    print(response.status_code)
    print(response.text)
    json_data = response.json()
    expr = parse('$..token')
    # $..token递归向下搜索
    token = expr.find(json_data)
    print("token："+token[0].value)
    response2 = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/save&token="+(token[0].value), headers=headers,
                             params=params, data=data2)

    print(response2.status_code)
    print(response2.text)
    response2 = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/goods/favor&token=" + token[0].value,
                              headers=headers,
                              params=params, data=data3)
    print(response2.status_code)
    print(response2.text)
if __name__ == '__main__':
    main()
