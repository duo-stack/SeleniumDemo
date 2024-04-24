import unittest
from os import walk, rmdir

from tool.tool_pass4get5 import tool_pass4get5

# 修改测试集覆盖范围
discover = unittest.defaultTestLoader.discover("case/", "test_power*.py")
runner = unittest.TextTestRunner()
result = runner.run(discover)

count = discover.countTestCases()
skip = len(result.skipped)
failure = len(result.failures)
error = len(result.errors)
success = count - failure - error - skip
rate = tool_pass4get5(success / (count - skip) * 100, 2)

print()
print(f"总测试用例数: {count}")
print(f"总跳过用例数: {skip}")
print(f"总成功用例数: {success}")
print(f"总失败用例数: {failure}")
print(f"总错误用例数: {error}")
print(f"成功率: {rate}%")
print()

# 若执行完后没有生成截图，则删除文件夹
for root, dirs, files in walk("D:\\HLDNY_ScreenShot", topdown=False):
    if not files and not dirs:
        rmdir(root)

# 若执行完成后日志为空，则删除日志文件。
# with open("D:\\HLDNY.log", "r") as f:
#     log = f.read()
# while log == "":
#     try:
#         remove("D:\\HLDNY.log")
#     except PermissionError:
#         sleep(1)
#         continue
#     else:
#         break
