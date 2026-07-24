import pytest
import requests
import pandas as pd
import os
from jsonpath_ng import parse
# 使用 jsonpath_ng 提取数据
from string import Template

from V1.global_value import g_val

# 构建可靠路径
base_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.normpath(os.path.join(base_dir, "../..", "data.xlsx"))
data_list = pd.read_excel(excel_path).to_dict(orient='records')
print(data_list)
@pytest.mark.parametrize("case_info", data_list)
def test_case_exec(case_info):
    url = case_info["接口URL"]
    dic=g_val().show_dict()
    if "$" in url:
        url =Template(url).substitute(dic)
    #如果url链接有占位符，则进行值替换。Template对链接当中的占位符进行识别，创建映射表，substitute对占位值进行智能替换
    rep=requests.request(url=url, method=case_info["请求方式"], params=eval(case_info["URL参数"]),data=eval(case_info["JSON参数"]))
    # eval把excel文件里面的值的值（字符串）转换成字典，方便代码执行
    extract_key = case_info.get('提取参数')
    if extract_key and not pd.isna(extract_key):
        jsonpath_expr = parse('$..' + str(extract_key))
        matches = jsonpath_expr.find(rep.json())
        if matches:
            g_val().set_dict(case_info['提取参数'], matches[0].value)
    # 获取token（key:value），放进g_val里
    print(rep.text)
    assert rep.status_code == case_info["预期状态码"]

