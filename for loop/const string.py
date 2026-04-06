text = "vishaka"
count = 0
for ch in text:
    if ch not in "aeiou":
        count+=1
        print(ch)
