#1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

# Will return 5

#2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# Doesn't work because "number of days..." is defined furter down. If it were above, it would print 8 (3+5).

#3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

#Will print 5 because once the first return is run the function exits.


#4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())

#Will print 5 because functions exits before the print(10) is run.


#5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)

#Will print 5 and none because nothing is returned for x.


#6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# Will print 3 and 5. Does not add them becauses nothing is returned.



# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))

# Will print 25 as the integers are turned into string and concatenated.


# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())

# Will print 100 and then 10 because b (100) is not less than 10, so the else function runs. Final return is not run as function exits before.


# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Will print 7 and rerutrn 3, print 14 and return 3, and then print 21 and return 3.


# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))

#Will print 8. Does not make it to the return 10.



# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)

# Will print 500, then 500 again, then 300, and finally 500 once more.


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)

# Will print 500, then 500 again, then 300, and finally 500 once more. The return within function is not getting used anywhere.


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)

# Will print 500, then 500 again, then 300, and finally 300 (which has been changed by the b=).


# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()

# Will print 1, 3, and then 2.


# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# WIll print 1, then 3, then 5, then 10.