
def constant(text):
    count=0
    for ch in text:
        if ch not in "aeiou":
            count+=1
    return count

print(constant("vishaka"))
