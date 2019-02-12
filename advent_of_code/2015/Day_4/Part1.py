import hashlib

base = "bgvyzdsv"
value = 0


hash_code = hashlib.md5()
hash_code.update(base.encode())


while True:
    value += 1
    test_hash = hash_code.copy()
    test_hash.update(str(value).encode())
    if test_hash.hexdigest().startswith("00000"):
        print(value)
        break


# 6940da637d7f68ff727fa41b9b90a209
# bbd0b4dcb0d07a947bf3c280f99baffd
