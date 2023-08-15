import hashlib
name="1145141919810"
salt="1ca9d5e1e6bee601dcd87f3544349dd4"
name+=salt
print(hashlib.sha256(name.encode()).hexdigest())
