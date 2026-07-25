import pytest
import requests
import pandas as pd
import os
from jsonpath_ng import parse
from string import Template

from V1.global_value import g_val

base_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.normpath(os.path.join(base_dir, "../..", "data.xlsx"))
data_list = pd.read_excel(excel_path).to_dict(orient='records')

@pytest.mark.parametrize("case_info", data_list)
def test_case_exec(case_info):
    url = case_info["接口URL"]
    dic = g_val().show_dict()
    if "$" in url:
        url = Template(url).substitute(dic)

    rep = requests.request(
        url=url,
        method=case_info["请求方式"],
        params=eval(case_info["URL参数"]),
        data=eval(case_info["JSON参数"])
    )

    extract_key = case_info.get('提取参数')
    if extract_key and not pd.isna(extract_key):
        jsonpath_expr = parse('$..' + str(extract_key))
        matches = jsonpath_expr.find(rep.json())
        if matches:
            g_val().set_dict(case_info['提取参数'], matches[0].value)

    print(rep.text)

    # HTTP status assert
    assert rep.status_code == case_info["预期状态码"], \
        f"HTTP status: expected {case_info['预期状态码']}, got {rep.status_code}"

    # Body field assert
    assert_field = case_info.get('需断言的字段')
    assert_value = case_info.get('断言预期值')
    if assert_field and not pd.isna(assert_field) and not pd.isna(assert_value):
        jsonpath_expr = parse('$..' + str(assert_field))
        matches = jsonpath_expr.find(rep.json())
        assert matches, f"Field not found: {assert_field}"
        actual = matches[0].value
        expected = int(assert_value)
        assert actual == expected, \
            f"Field {assert_field}: expected {expected}, got {actual}"
