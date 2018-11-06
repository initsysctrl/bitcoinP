"""
@file: transaction
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/5 5:29 PM
@describe: 
"""

import time

# 版本号
from typing import List

VERSION_NUMBER = 0


class VIn:
    def __init__(self, _txid: str, _vout: int, _scriptsig: str, _sequence: int):
        # txid，vout，scriptSig，sequence
        self.txid = _txid
        self.vout = _vout
        self.scriptSig = _scriptsig
        self.sequence = _sequence

    def __str__(self) -> str:
        return str(self.__dict__)


class VOut:
    def __init__(self, _value: float, _script_pubkey: str):
        self.value = _value
        self.scriptPubKey = _script_pubkey

    def __str__(self) -> str:
        return str(self.__dict__)


class Transction(object):
    def __init__(self, _inputs: list, _outputs: list):
        # assert isinstance(_inputs, list)
        # assert isinstance(_outputs, list)
        self.version = VERSION_NUMBER
        self.input_count = len(_inputs)
        self.inputs = _inputs
        self.output_count = len(_outputs)
        self.outputs = _outputs
        self.timestamp = time.time_ns()

    def __str__(self) -> str:
        return str(self.__dict__)


if __name__ == '__main__':
    inputs = [VIn('li xiao lai cao ni ma ', 123, 'aaa', 23123213213), VIn('li xiao lai cao ni ma ', 123, 'aaa', 2)]
    outputs = [VOut(12.22222, 'outoutoutout', )]
    t = Transction(inputs, outputs)
    print(t)

pass
