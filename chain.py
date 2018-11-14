"""
@file: blockchain
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/5 4:15 PM
@describe: 链
"""
from block import Block


class BlockChain:
    def __init__(self):
        self._blocks = []
        # self._height = 0

    # 创建新的区块
    def create_block(self):
        b = Block()
        self._blocks.append(b)

    # 返回区块高度
    @property
    def height(self):
        return len(self._blocks)

    # 返回最后的区块
    @property
    def last(self):
        return self._blocks[-1]


if __name__ == '__main__':
    blockchain = BlockChain()
    for x in range(10):
        blockchain.create_block()

    print(blockchain.height)
    print(blockchain.last.get_hash())
