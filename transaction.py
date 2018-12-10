"""
@file: transaction
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/5 5:29 PM
@describe: 交易模型
"""

import json
import time

# 版本号
VERSION_NUMBER = 0


class VIn:
    """
    定义-交易输入
    """

    def __init__(self, _txid: str, _vout: int, _scriptsig: str, _sequence: int):
        # txid，vout，scriptSig，sequence
        self.txid = _txid
        self.vout = _vout
        self.scriptSig = _scriptsig
        self.sequence = _sequence

    def __str__(self) -> str:
        return str(self.__dict__)


class VOut:
    """
    定义-交易输出
    """

    def __init__(self, value: float, script_pubkey: str):
        self.value = value
        self.scriptPubKey = script_pubkey

    def __str__(self) -> str:
        return str(self.__dict__)


class Transction(object):
    """
    定义交易信息
    """

    def __init__(self, _inputs: list, _outputs: list):
        self.txid = None
        self.version = VERSION_NUMBER
        self.inputs = _inputs  # 输入集合
        self.outputs = _outputs  # 输出集合
        self.input_count = 0 if (_inputs is None) else len(_inputs)
        self.output_count = 0 if (_outputs is None) else len(_outputs)
        self.timestamp = time.time_ns()

    def serialization(self):
        vin = []
        vout = []
        for i in self.inputs:
            vi = dict()
            vi['txid'] = i.txid
            vi['vout'] = i.vout
            vi['scriptSig'] = i.scriptSig
            vi['sequence'] = i.sequence
            vin.append(vi)

        for i in self.outputs:
            vo = dict()
            vo['value'] = i.value
            vo['scriptPubKey'] = i.scriptPubKey
            vout.append(vo)

        s = dict()
        s['txid'] = self.txid
        s['version'] = self.version
        s['vin'] = vin
        s['vout'] = vout

        return json.dumps(s, skipkeys=True, indent=4)

    def __str__(self) -> str:
        return str(self.__dict__)

    def is_coinbase_trans(self) -> bool:
        """
        是否属于coinbase交易类型
        :rtype: true
        """
        return self.input_count == 0 and self.output_count == 1


# 创建 coinbase 交易
def creat_coinbase_transaction() -> object:
    pass


# 创建UTXO交易
def creat_utxo_transaction():
    pass


if __name__ == '__main__':
    inputs = [VIn('li xiao lai cao ni ma ', 123, 'aaa', 23123213213), VIn('li xiao lai cao ni ma ', 123, 'aaa', 2)]
    outputs = [VOut(12.22222, 'outoutoutout', )]
    t = Transction(inputs, outputs)
    print(t.serialization())
