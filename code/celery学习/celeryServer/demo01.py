from celery import Celery

app = Celery('tasks',
                    broker='redis://127.0.0.1:6379/2', # 配置broker 发送到哪
                    backend='redis://127.0.0.1:6379/2') # 配置backend 结果返回到哪

@app.task
def add(x, y):
    print("running...", x, y)
    return x + y

@app.task
def cmd(cmd_str):
    print('running cmd',cmd_str)

# 在终端启动celery -A tasks worker --loglevel=info
# celery -A demo01 worker --loglevel=info