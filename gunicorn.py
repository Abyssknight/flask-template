import os

from flask_template.utils import get_host_ip

base_dir = os.path.dirname(__file__)

# 创建日志文件夹
if not os.path.exists('logs'):
    os.mkdir('logs')

# 日志
loglevel = 'debug'
log_dir = os.path.join(base_dir, 'logs')
errorlog = os.path.join(log_dir, 'error.log')
accesslog = os.path.join(log_dir, 'access.log')
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%(D)s"'

# 工作进程
worker_class = 'gevent'
workers = os.cpu_count() * 2 + 1
threads = os.cpu_count() * 2 + 1

# 绑定本地地址
ip = get_host_ip()
bind = "{}:5000".format(ip)
