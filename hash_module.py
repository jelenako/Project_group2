import pythonhashmodule

hashed_password = pythonhashmodule.hash_password("my_password")
print(hashed_password)

result = pythonhashmodule.check_password(hashed_password, "my_password")
print(result)


