''' Exercise #3. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
lst = ["lebron","james","is","the","GOATTTT223"]# Replace ??? with a list of your choice.
# Write the rest of the code for question 1 below here.
print(list(range(len(lst))))


#########################################
# Question 2 - do not delete this comment
#########################################
lst =["lebron","james","is","the","GOAT"] # Replace ??? with a list of your choice.
# Write the rest of the code for question 2 below here.
lst.reverse()
print(lst[::2])



#########################################
# Question 3 - do not delete this comment
#########################################
lst = [58,2,59,21,89,106,108,183,98,281] # Replace ??? with a list of integer numbers of your choice.
# Write the rest of the code for question 3 below here.
x=0
for elem in lst:
    if elem%2==0:
        x=x+elem
print("List’s even numbers sum is: " + str(x))


#########################################
# Question 4 - do not delete this comment
#########################################
x = "GOAT" # Replace ??? with a value of your choice.
lst = ["lebron","james","is","the","GOAT",23] # Replace ??? with a list of your choice.
# Write the rest of the code for question 4 below here.
if lst.count(x)>=1:
    print("True")
else: print("False")


#########################################
# Question 5 - do not delete this comment
#########################################
lst = ["lebron","james","is","the"] # Replace ??? with a list of your choice.
# Write the rest of the code for question 5 below here.
if len(lst)<=7:
    while len(lst)!=7:
        lst.append(0)
elif len(lst)>=7:
    while len(lst)!=7:
        lst.pop()
        
print(lst)



