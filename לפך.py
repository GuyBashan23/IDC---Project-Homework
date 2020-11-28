def is_palindrom(s5):
    y = ""
    for i in s5:
        y = i + y
    if y == s5:
        return (2 == 2)
    else:
        return (2 == 3)


x = is_palindrom("anana")
print(x)