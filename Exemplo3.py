import hashlib, binascii

text = 'hello'
data = text.encode("utf8")

md5 = hashlib.md5(data).digest()
print("MD5:   ", binascii.hexlify(md5))
