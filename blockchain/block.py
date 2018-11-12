"""
@file: block
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/5 4:24 PM
@describe:
"""
import hashlib
import json


class Block:
    def __init__(self, _block_head=None, _trans=()):
        # 大小
        self.size = 0
        # 区块头
        self.block_head = None
        # 交易数量
        self.trans_count = len(_trans)
        # 交易列表
        self.trans = []
        # 区块主标识符是它的加密哈希值，⼀个通过SHA256算法对区块头进⾏⼆次哈希计算⽽得到的数字指纹

    def hash(self):
        block_string = json.dumps(self.block_head, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self) -> str:
        return str(self.__dict__)


class BlockHead:
    def __init__(self):
        # 版本号
        self.version = 0
        # 爸爸的哈希
        self.previous_hash = None
        # 默克尔命根的哈希
        self.merkle_root_hash = None
        # 时间戳
        self.timestamp = None
        # hard
        self.difficulty = None
        # 幸运值
        self.nonce = None


if __name__ == '__main__':
    pass
