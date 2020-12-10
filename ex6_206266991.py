''' Exercise #6. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def how_many_common_letters(s1, s2):
    share=0
    for elem in s1:
        for elen in s2:
            if elem==elen:
                share=share+1
    return share



#########################################
# Question 2 - do not delete this comment
#########################################
def clean_word(word, chars_list):
    word_lower = word.lower()
    new_lst = list(word_lower[:])
    y = 0
    for elem in chars_list:
        if elem in new_lst:
            y = new_lst.count(elem)
            for elen in range(0, y):
                new_lst.remove(elem)
    good = ""
    for eler in new_lst:
        good = good + eler

    return good



#########################################
# Question 3 - do not delete this comment
#########################################
def ciel_list_of_floats_in_place(floats_list):
    floats_list2 = floats_list[:]
    for elem in floats_list2:
        if elem > 0:
            floats_list.remove(elem)
            floats_list.append(float(int(elem + 1)))

        if elem < 0:
            floats_list.remove(elem)
            floats_list.append(float(int(elem)))


l = ([1.2, -4.8, -2.0, 7.8, -10.1])
ciel_list_of_floats_in_place(l)
print(l)



#########################################
# Question 4 - do not delete this comment
#########################################
def clean_words_of_sentence(sentence):
   good1=clean_word(sentence, [",",".","%","?","!","$","#"])
   return good1.split()



#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_pattern(p):
    i=0
    new_lst= list(p)
    length = len(new_lst)
    for elem in range(i,length,2):
        if new_lst[elem] != '(':
            return False
        if new_lst[elem] == '(':
            if new_lst[elem + 1] == ')':
                continue
            else:
                return False
    return True


