"""
@file: wallet
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/1 11:01 AM
@describe: 
"""
import binascii
import hashlib
import secrets

import crypto

"""
类：钱包信息
"""


class Wallet(object):

    def __init__(self, privatea_key_hex=None, base58private=None, wifprivate=None, anyword=None):
        if privatea_key_hex is not None:
            self.private_key = privatea_key_hex
        elif base58private is not None:
            self.private_key = crypto.base58decode(base58private)
        elif wifprivate is not None:
            self.private_key = crypto.base58_check_decode(base58private)
        elif anyword is not None:
            self.private_key = hashlib.sha256(bytes(anyword, 'utf-8')).hexdigest()
        else:
            self.private_key = hex(secrets.randbits(256))[2:]
            # 1：public-key
        public_key = crypto.privakey_to_publickey(private_key_hex=self.private_key)
        # 2：first hash
        h1 = hashlib.sha256(binascii.unhexlify(public_key)).hexdigest()
        # 3：second hash
        h2 = hashlib.new('ripemd160', binascii.unhexlify(h1)).hexdigest()
        # 4：add network bytes
        ver_plaload = '00' + h2
        # 5:SHA-256 hash of '4'
        sha1 = hashlib.sha256(binascii.unhexlify(ver_plaload)).hexdigest()
        # 6:SHA-256 hash of '5'
        sha2 = hashlib.sha256(binascii.unhexlify(sha1)).hexdigest()
        # 7:First four bytes of '6'，4bytes=8bit
        checksum = sha2[:8]
        # 8: Adding 7 at the end of "4"
        full_load = ver_plaload + checksum

        # 9:Base58 encoding of 8
        address = crypto.base58encode(full_load)

        self.publickey = public_key
        self.publickeyhash = h2
        self.address = address

    # 导出base58格式的私钥
    def export_base58_privatekey(self) -> str:

        return crypto.base58encode(self.private_key)

    # 导出WIF格式的私钥
    def export_wif_privatekey(self) -> str:

        return crypto.base58_check_encode(self.private_key, '0x80')

    # 导出压缩WIF格式的私钥
    def export_compress_privatekey(self) -> str:

        return crypto.base58_check_encode(0x80, self.private_key + '01')

    def __str__(self):

        return 'private key(HEX):' + self.private_key + '\n' \
               + 'public key (uncompress):' + self.publickey + '\n' \
               + 'public key hash(uncompress):' + self.publickeyhash + '\n' \
               + 'address(U):' + self.address + '\n'


if __name__ == '__main__':
    wallet = Wallet(anyword="caonimalixiaolai")
    # wallet = Wallet(privatea_key_hex='18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725')
    print('wallet=', wallet.__str__())
    # print('wallet=', wallet2.__str__())

# 14EvJWPvFNLnzBBzhm1AG9a5b6XiSBFs6R
# 4EvJWPvFNLnzBBzhm1AG9a5b6XiTTWrcb
