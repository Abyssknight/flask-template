import socket
import time
from uuid import uuid1

import arrow

from flask_template.extensions import redis


class RedisLock:
    """分布式锁"""

    LUA_RELEASE = """
        local key = KEYS[1]
        local identifier = ARGV[1]
        
        if redis.call("GET", key) == identifier then
            redis.call("DEL", key)
            return 1
        else
            return 0
        end
    """

    def __init__(self, lock_name, ex=10, timeout=None):
        self.lock_name = lock_name
        self.identifier = uuid1().hex
        self.ex = ex
        self.timeout = timeout

    def acquire(self):
        """
        首先尝试获取锁, 成功获取到锁，则返回
        未获取到锁，则需要检查锁是否设置了过期时间
        等待锁释放
        """
        acquire_time_end = time.time() + self.timeout or self.ex
        while time.time() < acquire_time_end:
            if redis.set(self.lock_name, self.identifier, ex=self.ex, nx=True):
                return True
            if redis.ttl(self.lock_name) == -1:
                redis.expire(self.lock_name, self.ex)
            time.sleep(0.01)
        else:
            return False

    def release(self):
        """
        使用 Lua 脚本释放锁，保证原子性
        首先判断当前持有锁是否与 Redis 中的锁一致
        原因是如果业务执行时间过长，导致锁被自动释放
        那么另一个业务将会持有新的锁开始执行
        """
        return True if redis.eval(self.LUA_RELEASE, 1, self.lock_name, self.identifier) else False


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
