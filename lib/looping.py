#!/usr/bin/env python3
#count down 10 -1 after 1 print happy new year 
# def happy_new_year():
#     i=10
#     while i < 1:
#         print("Happy New Year!")
#         i-=1
#     pass
def happy_new_year():
    countdown = 10
    while countdown in range(10, 0, -1):
        print(countdown)
        countdown -= 1
    
    print("Happy New Year!")
 #one line spacing allowed for it to print after once 


def square_integers(int_list):
    return [y ** 2 for y in int_list]
    # for i in range(len(int_list)):
    #     print(i **  2)
    #     return i ** 2
    # when using range 0, 1,4,9,16 displayed why?
    pass

def fizzbuzz():
    for i in range(1,101):
        if (i % 3 == 0 and i % 5 ==0 ):
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else: print(f"{i}")
        #seen a different sol  if not i % 15: why does this 
        #work
    pass


i = 2
while i < 5:
  print("Looping!")
  i += 1


# start_inclusive = 4
# for i in reversed(range(start_inclusive + 1)):
#    print(i)

