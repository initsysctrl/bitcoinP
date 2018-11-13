"""
@file: crypto
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/12 8:22 AM
@describe: 
"""
import binascii
import hashlib
from binascii import hexlify, unhexlify

import ecdsa

Base58Alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
BASE58_ALPHABET = b"123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58decode(base58_str):
    base58_text = bytes(base58_str, "ascii")
    n = 0
    leading_zeroes_count = 0
    for b in base58_text:
        n = n * 58 + BASE58_ALPHABET.find(b)
        if n == 0:
            leading_zeroes_count += 1
    res = bytearray()
    while n >= 256:
        div, mod = divmod(n, 256)
        res.insert(0, mod)
        n = div
    else:
        res.insert(0, n)
    return hexlify(bytearray(1) * leading_zeroes_count + res).decode('ascii')


def base58encode(hexstring):
    byteseq = bytes(unhexlify(bytes(hexstring, 'ascii')))
    n = 0
    leading_zeroes_count = 0
    for c in byteseq:
        n = n * 256 + c
        if n == 0:
            leading_zeroes_count += 1
    res = bytearray()
    while n >= 58:
        div, mod = divmod(n, 58)
        res.insert(0, BASE58_ALPHABET[mod])
        n = div
    else:
        res.insert(0, BASE58_ALPHABET[n])
    return (BASE58_ALPHABET[0:1] * leading_zeroes_count + res).decode('ascii')


'''
1.将字符串转换为十六进制

2.将十六进制转换为十进制

3.将十进制转换为58中字符

4.颠倒字符串的顺序
'''


def ripemd160(s):
    ripemd_160 = hashlib.new('ripemd160')
    ripemd_160.update(unhexlify(s))
    return ripemd_160.digest()


# base58check编码
# https://steemitimages.com/0x0/https://steemitimages.com/DQmR6osyE59XryeuQyffbf74WoMcN9vcMs8xYnQ9qDMH3tP/image.png
def base58_check_encode(load=None, version='00'):
    ver_load = version + load
    print('ver_plaload=', ver_load)
    # SHA-256 hash
    sha1 = hashlib.sha256(binascii.unhexlify(ver_load)).hexdigest()
    # SHA-256 hash
    sha2 = hashlib.sha256(binascii.unhexlify(sha1)).hexdigest()
    # First four bytes
    checksum = sha2[:8]
    print('checksum=', checksum)
    # Adding 7 at the end of "4"
    full_load = ver_load + checksum
    return base58encode(full_load)


def doublesha256(s):
    h1 = hashlib.sha256(unhexlify(s)).digest().hex()
    h2 = hashlib.sha256(unhexlify(h1)).digest()
    return h2


# hash160编码
def hash160(string):
    intermed = hashlib.sha256(binascii.unhexlify(string)).digest()

    digest = hashlib.new('ripemd160', intermed).digest()

    return digest


# base58 解码
def base58_check_decode(s):
    s = unhexlify(base58decode(s))
    dec = hexlify(s[:-4]).decode('ascii')
    checksum = doublesha256(dec)[:4]
    assert (s[-4:] == checksum)
    return dec[2:]


# 由私钥生成公钥
def privakey_to_publickey(private_key_hex: str) -> str:
    """

    :param private_key_hex: 私钥 hex格式的
    :return: 压缩和未被压缩的公钥
    """
    secret = unhexlify(private_key_hex)
    order = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).curve.generator.order()
    p = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).verifying_key.pubkey.point
    x_str = ecdsa.util.number_to_string(p.x(), order)
    y_str = ecdsa.util.number_to_string(p.y(), order)
    compressed = hexlify(bytes(chr(2 + (p.y() & 1)), 'ascii') + x_str).decode('ascii')
    uncompressed = hexlify(bytes(chr(4), 'ascii') + x_str + y_str).decode('ascii')
    return uncompressed


if __name__ == "__main__":
    res = base58_check_encode(version='00', load="238a476bf87bc6ddc088f2bbd00941c6275a94de")
    print(res)
    assert res == "14EvJWPvFNLnzBBzhm1AG9a5b6XiSBFs6R"

    pass
# 14EvJWPvFNLnzBBzhm1AG9a5b6XiSBFs6R
# 14EvJWPvFNLnzBBzhm1AG9a5b6XiSBFs6R
