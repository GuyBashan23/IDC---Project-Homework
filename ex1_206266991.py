''' Exercise #1. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
name  = "GuyBashan"
# Replace ??? with a string of your choice.
# Write the rest of the code for question 1 below here.
print("Hello " + name+"!")


#########################################
# Question 2a - do not delete this comment
#########################################
my_str2a = "LeBron Raymone James Sr, is an American professional basketball player for the Los Angeles Lakers of the National Basketball Association" # Replace ??? with a string of your choice.
# Write the rest of the code for question 2a below here.
len(my_str2a)

#########################################
# Question 2b - do not delete this comment
#########################################
my_str2b = "LeBron Raymone James Sr, is an American professional basketball player for the Los Angeles Lakers of the National Basketball Association" # Replace ??? with a string of your choice.
# Write the rest of the code for question 2b below here.
commas=my_str2b.count(",")
print(my_str2b.count(""))
print(my_str2b.count("")-int(commas))



#########################################
# Question 3 - do not delete this comment
#########################################
my_str3 = "James played basketball for St. Vincent–St. Mary High School in his hometown of Akron, Ohio, where he was heavily touted by the national media as a future NBA superstar." # Replace ??? with a string of your choice.
# Write the rest of the code for question 3 below here.
count3=my_str3.count("")
half_count3=count3/2
first_str3=my_str3[0:int(half_count3)]
first_str3_upper=first_str3.upper()
second_str3=my_str3[int(half_count3):int(my_str3.count(""))]
second_str3_lower=second_str3.lower()
print(first_str3_upper+":"+second_str3_lower)
#########################################
# Question 4 - do not delete this comment
#########################################
R  = 9 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 4 below here.
diameter=R*2
pi=3.14
print("Size of circle diameter is: " +str(diameter))
print("Circumference is: " +str(2*pi*R)[0:4])
print("Area is: " +str(pi*(R**2)))
#########################################
# Question 5 - do not delete this comment
#########################################
repeats = 9 # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.
print("LeBron is the GOAT\n"*int(repeats))

