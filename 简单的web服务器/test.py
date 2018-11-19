import subprocess

data=subprocess.check_output(["python",r"C:\Users\QQ\PycharmProjects\简单的web服务器\time.py"],shell=False)
print(data)