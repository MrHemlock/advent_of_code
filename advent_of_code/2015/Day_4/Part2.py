import hashlib

base = "bgvyzdsv"
value = 0


hash_code = hashlib.md5()
hash_code.update(base.encode())


while True:
    value += 1
    test_hash = hash_code.copy()
    test_hash.update(str(value).encode())
    if test_hash.hexdigest().startswith("000000"):
        print(value)
        break
