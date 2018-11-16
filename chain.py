"""
@file: blockchain
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/5 4:15 PM
@describe: 链
The blockchain data structure is an ordered, back-linked list of blocks of transactions. The

blockchain can be stored as a flat file, or in a simple database. The Bitcoin Core client

stores the blockchain metadata using Google’s LevelDB database. Blocks are linked "back,"

each referring to the previous block in the chain. The blockchain is often visualized as a

vertical stack, with blocks layered on top of each other and the first block serving as the

foundation of the stack. The visualization of blocks stacked on top of each other results in

the use of terms such as "height" to refer to the distance from the first block, and "top" or

"tip" to refer to the most recently added block.
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
