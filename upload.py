import os

# 获取当前时间
def get_time():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

os.system(f'git add . && git commit -m "{get_time()}" && git push')

