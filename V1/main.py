import pytest
import subprocess
import os
import shutil
os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['LANG'] = 'zh_CN.UTF-8'
os.environ['LC_ALL'] = 'zh_CN.UTF-8'
if __name__ == "__main__":
    # 1. 定义 Allure 目录
    allure_results_dir = "../reports/allure-results"
    allure_report_dir = "../reports/allure-report"

    # 2. 清理旧数据（可选）
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    if os.path.exists(allure_report_dir):
        shutil.rmtree(allure_report_dir)

    # 3. 组装 pytest 启动参数（注意是列表！）
    #    根据你的需求，二选一：
    #    方案A：想看所有 print 输出（推荐写 -s，去掉 --capture）
    #    方案B：只捕获 sys 输出给 Allure（去掉 -s，保留 --capture=sys）
    pytest_args = [
        "-v",                     # 详细打印每条用例结果
        "--capture=sys",        # 若写了 -s，这一行会被无视；若想要它生效，请注释掉 -s
        "--alluredir", allure_results_dir,
        "tests/"                  # 替换为你的测试文件或目录，如 __file__
    ]

    # 4. 执行 pytest
    exit_code = pytest.main(pytest_args)

    # 5. 生成 Allure HTML 报告
    if exit_code in (0, 1):  # 0=全过，1=有失败，都生成报告
        generate_cmd = f"allure generate {allure_results_dir} -o {allure_report_dir} --clean"
        subprocess.run(generate_cmd, shell=True, check=True)
        print(f"\n✅ Allure 报告已生成: {os.path.abspath(allure_report_dir)}/index.html")
        # 如果想自动打开浏览器看报告，取消下面注释
        # subprocess.run(f"allure open {allure_report_dir}", shell=True)
    else:
        print("❌ pytest 执行异常，跳过报告生成")

    # 6. 返回退出码
    exit(exit_code)