import socket

import arrow


def now():
    """返回当前时间"""
    return arrow.now().datetime


def get_host_name():
    """查找主机名"""
    return socket.gethostname()


def get_host_ip():
    """查询主机地址"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        return ip
