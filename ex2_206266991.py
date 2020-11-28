''' Exercise #2. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
number = int(input("INSERET NUMBER: "))  # Replace ??? with an appropriate command to get a number from the user.
# Write the rest of the code for question 1 below here.
if number%3==0:
             print(f"I am {number} and I am a multiplication of 3")
else: print(f"I am {number} and I am not a multiplication of 3")



#########################################
# Question 2 - do not delete this comment
#########################################
number = int(input("INSERET NUMBER: "))  # Replace ??? with an appropriate command to get a number from the user.
# Write the rest of the code for question 2 below here.
if number%2==0:
    print("Even number")
if number%3==0 and number%6!=0:
    print("Divisible by 3")
if len(str(number))%2!=0:
    print("Odd number of digits")


#########################################
# Question 3 - do not delete this comment
#########################################
grade = int(input("INSERET NUMBER: "))  # Replace ??? with an integer of your choice.
# Write the rest of the code for question 3 below here.
if grade<0 or grade>100:
    print("Illgel grade")
elif grade<=59:
        print("F")
elif 60<=grade<=69:
            print("D")
elif 70<=grade<=79:
                print("C")
elif 80<=grade<=89:
                    print("B")
elif 90<=grade<=100:
                        print("A")


#########################################
# Question 4 - do not delete this comment
#########################################
my_str = str(input("INSERET WORD: "))  # Replace ??? with a string of your choice.
# Write the rest of the code for question 4 below here.
my_str = my_str.lower()
rev_str = my_str[::-1]
print(my_str==rev_str)




