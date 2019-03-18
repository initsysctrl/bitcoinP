"""
@file: transaction
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/5 5:29 PM
@describe: 交易模型
签名的大致流程如下：

1、准备好一个原始的交易数据；

2、对这个原始的交易数据进行两次SHA256 hash运算，得到固定长度的hash散列；

3、使用椭圆曲线算法，结合你自己的私钥，对上述的hash散列值进行加密计算，得到签名数据；


"""

import hashlib
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
        # txid:来自哪个交易，vout：来自交易输出的角标 scriptSig
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

    # 获取交易哈希
    def get_txid(self):
        uid = hashlib.sha256(bytes(self.serialization(), 'utf-8')).hexdigest()
        self.txid = uid
        return self.txid

    def __str__(self) -> str:
        return str(self.__dict__)

    #  验证是否属于coinbase交易类型
    def is_coinbase_trans(self) -> bool:
        return len(self.inputs) == 1 and self.inputs[0].txid == 0 and self.inputs[0].vout == -1

    #  验证交易合法性
    def verify(self) -> bool:
        if self.is_coinbase_trans():
            return True
        pass

    # 签名交易
    def sign(self, private_key, txs):
        """
        交易签名
        :param private_key:
        :param txs:
        """
        if self.is_coinbase_trans():
            return
        for vi in self.inputs:
            pass
        pass


# 创建 coinbase 交易
def creat_coinbase_transaction(to, date) -> str:
    pass


# 创建UTXO交易
def creat_utxo_transaction(to, amount, utxos) -> str:
    pass


if __name__ == '__main__':
    inputs = [VIn('li xiao lai cao ni ma ', 123, 'aaa', 23123213213), VIn('li xiao lai cao ni ma ', 123, 'aaa', 2)]
    outputs = [VOut(12.22222, 'outoutoutout', )]
    t = Transction(inputs, outputs)
    print(t.serialization())
    print(t.get_txid())
