# for i in range(10):
#     print(i)


#how thios code work "*Outer loop = 5 times *Inner loop = har baar 5 times"
#5 × 5 = 25 baar inner print
x = 5
n = 5

print(n)

for i in range(n):
    print(i)

    n = 5
    print(n)

    for j in range(0, n):
        print(j)



# '''
#  Write a function that returns the first element of an array?
# '''

# def array_first_return(a):
#     return a[0]

# array = [1,2,3,4,5,6,4,5,6,7,8,4,3,2,24,4,32,2,2]

# first_element = array_first_return(array)
# print(first_element)
'''
O(1)
'''

n = int(input("Enter n: "))

for i in range(1, 4):
    print(i)
    for j in range(1, n + 1):
        print(j, end="\n\n")

# O(n)
'''
n =2

(1,3)
1 and 2

1
2

10
O(3)




O(1)
'''