def min_value(text):
    min_value=text[0]
    for n in text:
        if n<min_value:
             min_value=n
    return min_value
print("minimum value is :",min_value([10,8,20,5,40]))
