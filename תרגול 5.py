def r_in_char_is(s1, c1):
    x = c1 in s1
    return x
x=r_in_char_is("banana", "a")
print(x)
type(x)

def is_in_range(lst2, a, b):
    if len(lst2)>a and len(lst2)<b:
        x=(2==2)
        return(x)
    elif len(lst2)==0:
        x = (2 == 2)
        return (x)
    else:
        x=(2==3)
        return(x)
x=is_in_range([1, 2, 3], 0, 5)
print(x)

def upper_list_strings(lst3):
    my_list=[x.upper() for x in lst3]
    return my_list
my_list=upper_list_strings(['this', 'is', 'A', 'TeST', 'caSe', '!'])
print(my_list)

def log10_list(lst4):
    import math
    new_lst=[]
    for elem in lst4:
        new_lst.append(math.log(elem,10))
    return new_lst

my_lst=log10_list([10, 100, 1000, 10000])
print(my_lst)

def is_palindrom(s5):
    if s5==s5[::-1]:
        x=(2==2)
        return x
    else:
        x=(2==3)
        return x
x = is_palindrom('Anana')
print(x)
