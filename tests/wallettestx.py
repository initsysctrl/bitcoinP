"""
@file: caonimabi
@author: initsysctrl
@license: Apache Licence
@contact: initsysctrl@163.com
@time: 2018/11/13 9:15 PM
@describe:
"""
import binascii
import hashlib

import crypto

if __name__ == '__main__':
    # 0:Private ECDSA Key
    anyword = "cnm的李笑来"
    private_key = hashlib.sha256(bytes(anyword, 'utf-8')).hexdigest()
    print('private_key=', private_key)
    # 1：public-key
    public_key = crypto.privakey_to_publickey(private_key_hex=private_key)
    print('public_key=', public_key)
    # 2：first hash
    h1 = hashlib.sha256(binascii.unhexlify(public_key)).hexdigest()
    print('h1=', h1)
    # 3：second hash
    h2 = hashlib.new('ripemd160', binascii.unhexlify(h1)).hexdigest()
    print('h2=', h2)
    # 4：add network bytes
    ver_plaload = '00' + h2
    print('ver_plaload=', ver_plaload)
    # 5:SHA-256 hash of '4'
    sha1 = hashlib.sha256(binascii.unhexlify(ver_plaload)).hexdigest()
    print('sha1=', sha1)
    # 6:SHA-256 hash of '5'
    sha2 = hashlib.sha256(binascii.unhexlify(sha1)).hexdigest()
    print('sha2=', sha2)
    # 7:First four bytes of '6'，4bytes=8bit
    checksum = sha2[:8]
    print('checksum=', checksum)
    # 8: Adding 7 at the end of "4"
    full_load = ver_plaload + checksum
    print('full_load=', full_load)

    # 9:Base58 encoding of 8
    address = crypto.base58encode(full_load)
    print('address=', address)
    pass

#
# 00238A476BF87BC6DDC088F2BBD00941C6275A94DEA6248BF2
# 00238a476bf87bc6ddc088f2bbd00941c6275a94dea6248bf2
