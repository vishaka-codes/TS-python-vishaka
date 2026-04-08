d = {"a": 1,"b" : 15,"z": 24}

for k in d.keys():
    print(k)

# Then: print values > 10
for v in d.values():
    if v > 10:
        print("values > 10 are:",v)
