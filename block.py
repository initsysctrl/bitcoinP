"""
@file: block
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/5 4:24 PM
@describe: 区块
"""

import hashlib
import json
import time

from markle import Markle

"""
The blockchain data structure is an ordered, back-linked list of blocks of transactions. The

blockchain can be stored as a flat file, or in a simple database. The Bitcoin Core client

stores the blockchain metadata using Google’s LevelDB database. Blocks are linked "back,"

each referring to the previous block in the chain. The blockchain is often visualized as a

vertical stack, with blocks layered on top of each other and the first block serving as the

foundation of the stack. The visualization of blocks stacked on top of each other results in

the use of terms such as "height" to refer to the distance from the first block, and "top" or

"tip" to refer to the most recently added block.
"""


class Block:
    def __init__(self, pre_block_hash, nonce, trans):
        # 大小
        self.size = 0
        # 区块头
        self.block_head = {"difficulty": 1,
                           "merkleroot": Markle.get_root(),
                           "nonce": nonce,
                           "previousblockhash": pre_block_hash,
                           "timestamp": time.time_ns(),
                           "version": 0}
        # 交易数量
        self.trans_count = len(trans)
        # 交易列表
        self.trans = trans

    # 区块主标识符是它的加密哈希值，⼀个通过SHA256算法对区块头进⾏⼆次哈希计算⽽得到的数字指纹
    def hash(self):
        block_string = json.dumps(self.block_head, sort_keys=True).encode('utf-8')
        double_hash = hashlib.sha256(hashlib.sha256(block_string).digest()).hexdigest()
        return double_hash

    def __str__(self) -> str:
        return str(self.__dict__)


if __name__ == '__main__':
    v1 = '0000000000aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    v2 = 9743
    v3 = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8']
    block = Block(v1, v2, v3)
    print(block)
    print(block.hash())
    # print(b.hash())

pass
