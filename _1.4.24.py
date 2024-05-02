# def show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()
# a=[
#     [1,2,3,4,5],
#     [3,4,5,9,8],
#     [7,8,3,2,5],
#     [6,1,4,3,2],
#     [5,4,3,2,1]
#     ]
# b=[
#     [1,2,3,3,1],
#     [3,4,5,4,2],
#     [7,8,3,5,3],
#     [6,1,4,9,4],
#     [5,4,3,8,5]
# ]

  #rotate right
# for r in range(len(a)):
#     for c in range(len(a)):
#         b[c][len(a)-1-r] = a[r][c]

# #   Rotate left
# for r in range(len(a)):
#     for c in range(len(a)):
#         b[len(a)-1-c][r] = a[r][c]

# show(a)
# print()
# show(b)

###
#2022 summer a
# def Q14(v):
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==v):
#                 if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                     return True
#     return False
   
# a=[
#     [1,2,3,3,5,8],
#     [3,8,8,3,5,5],
#     [7,8,8,2,5,5],
#     [6,1,1,3,2,2],
#     [5,1,1,2,2,2]
#     ]
# for i in range(10):
#     print(Q14(i))

###

# def Q14A(a, v):
#     m=0
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==v):
#                 if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                     m+=1
#     return m
   
# a=[
#     [1,1,3,3,5,8,3,3,5,8],
#     [1,1,8,8,5,5,8,3,5,5],
#     [7,8,8,8,5,5,8,2,5,5],
#     [6,1,1,3,2,2,1,1,2,2],
#     [5,1,1,2,2,2,1,1,2,2]
#     ]
# for i in range(10):
#     print(i, Q14A(a, i))

###


# def Q(a):
#     b=[0]*10
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==a[r][c+1] and a[r][c]==a[r+1][c] and a[r][c]==a[r+1][c+1]):
#                 b[a[r][c]]+=1
#     return b
# a=[
#     [1,1,3,3,5,8,3,3,5,8],
#     [1,1,8,8,5,5,8,3,5,5],
#     [7,8,8,8,5,5,8,2,5,5],
#     [6,1,1,3,2,2,1,1,2,2],
#     [5,1,1,2,2,2,1,1,2,2]
#     ]
# r=Q(a)
# print(r)

###

# import random
# a=[0]*10
# for i in range(len(a)):
#     a[i]=random.randint(0,10)
# print(a)
# counters=[0]*11
# for i in range(len(a)):
#     counters[a[i]]+=1
# print()
# print(counters)
# index=0
# for i in range(0, 11, 1):
#     k=0
#     while(k<counters[i]):
#         a[index]=i
#         index+=1
#         k+=1
# print()
# print(a)
###
def F(a):
    i=0
    while(i<len(a)-1 and a[i]<a[i+1]):
        i+=1
    if(i==len(a)-1 or i==0):  
        return -1
    p=i
    while(i<len(a)-1 and a[i]>a[i+1]):
        i+=1
    if(i==len(a)-1):  
        return p
    return -1

a=[1,2,3,4,5,6,5,4,3,2]
print(F(a))    
