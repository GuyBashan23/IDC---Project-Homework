''' Exercise #7. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def range_dict(a, b):
    my_dic = {}
    for elem in range(a, b + 1):
        elen = str(elem)
        new_lst = []
        new_lst.append(elem)
        m = new_lst

        my_dic[elen] = m
    return my_dic



#########################################
# Question 2 - do not delete this comment
#########################################
def merge_dictionaries(d1,d2):
    for elem in d2:
        d1[elem]=d2[elem]
    return d1



#########################################
# Question 3 - do not delete this comment
#########################################
def most_popular_digit(num):
    my_dic = {}
    for elem in str(num):
        x = (my_dic.get(elem, 0) + 1)
        my_dic[elem] = x
    max_value = max(my_dic.values())

    return max(my_dic, key=my_dic.get)



#########################################
# Question 4 - do not delete this comment
#########################################
def most_common_value_in_dict(d):
    my_lst=d.values()
    my_dic={}
    for elem in my_lst:
        my_dic[elem]=my_dic.get(elem,0)+1
    return int(max(my_dic,key=my_dic.get))



#############################################
# BONUS Question - do not delete this comment
#############################################
def swap_students_courses(student2courses):
    my_dic={}
    for elem in student2courses:
        for elem2 in student2courses[elem]:
            my_lst=my_dic.get(elem2,[])
            my_lst.append(elem)
            my_dic[elem2]=my_lst
    return my_dic



