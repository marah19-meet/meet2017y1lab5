##c=0
##for number in range(1,100+1):
#    print(number)
#    c=c+number
#print(c)



def add_numbers(start,end):
    c=0
    for number in range(start,end+1):
        #print(number)
        c=c+number
    print(c)
    return c


#answer=add_numbers()
#print(answer)


test1=add_numbers(1,2)
print(test1)
test2=add_numbers(1,100)
print(test2)
test3=add_numbers(1000,5000)
print(test3)
test4=add_numbers(333,777)
print(test4)
