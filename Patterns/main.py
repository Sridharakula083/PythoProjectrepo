#n = int(input("Enter no of rows"))
#for i in range(n):
#   print((str(n-i)+ ' ')*n)
# 3 3 3
# 2 2 2
# 1 1 1

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print((chr(64+n-i)+ ' ')*n)
#C C C
#B B B
#A A A

#n = int(input("Enter no of rows"))
#for i in range(n):
#    for j in range(n):
#        print(n-j,end=" ")
#    print()
#4 3 2 1
#4 3 2 1
#4 3 2 1
#4 3 2 1

#n = int(input("Enter no of rows"))
#for i in range(n):
#    for j in range(n):
#        print(chr(64+n-j),end=" ")
#    print()
#D C B A
#D C B A
#D C B A
#D C B A

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print((i+1)*(' * '))
#*
#*  *
#*  *  *
#*  *  *  *
#*  *  *  *  *

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print((i+1)*(str(i+1)+' '))
#1
#2 2
#3 3 3
#4 4 4 4

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print((i+1)*(chr(65+i)+' '))
#A
#B B
#C C C
#D D D D

#n = int(input("Enter no of rows"))
#for i in range(n):
#    for j in range(i+1):
#        print(j+1,end=" ")
#    print()
#1
#1 2
#1 2 3
#1 2 3 4

#n = int(input("Enter no of rows"))
#for i in range(n):
#    for j in range(i+1):
#         print(chr(65+j),end=" ")
#    print()
#A
#A B
#A B C
#A B C D

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print("* "*(n-i))
#* * * *
#* * *
#* *
#*

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*i+'* '*(n-i))
#* * * *
# * * *
#  * *
#   *

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*i+(str(i+1)+' ')*(n-i))
#1 1 1 1
# 2 2 2
#  3 3
#   4

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*i+(chr(65+i)+' ')*(n-i))
#A A A A
# B B B
#  C C
#   D

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*i,end='')
#    for j in range(n-i):
#        print(j+1,end=' ')
#    print()
#1 2 3 4
# 1 2 3
#  1 2
#   1

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*i,end='')
#    for j in range(n-i):
#        print(j+1,end=' ')
#1 2 3 4  1 2 3   1 2    1

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*i,end='')
#    for j in range(n-i):
#        print(chr(65+j),end=' ')
#    print()
#A B C D
# A B C
#  A B
#   A

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*i,end='')
#    for j in range(n-i):
#        print(n-j,end=' ')
#    print()
#4 3 2 1
# 4 3 2
#  4 3
#   4

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*i,end='')
#    for j in range(n-i):
#        print(chr(64+n-j),end=' ')
#    print()
#D C B A
# D C B
#  D C
#   D

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*(n-i-1)+'* '*(i+1))
#for i in range(n-1):
#    print(' '*(i+1)+'* '*(n-i-1))
#   *
#  * *
# * * *
#* * * *
# * * *
#  * *
#   *

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
#for i in range(n-1):
#    print(' '*(i+1)+(str(n-i-1)+' ')*(n-i-1))
#   1
#  2 2
# 3 3 3
#4 4 4 4
# 3 3 3
#  2 2
#   1

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print(' '*(n-i-1),end=" ")
#    for j in range(i+1):
#        print((j+1),end=" ")
#    print()
#for i in range(n-1):
#    print(' '*(i+1),end=" ")
#    for j in range(n-i-1):
#        print((j+1),end=" ")
#    print()
#    1
#   1 2
#  1 2 3
# 1 2 3 4
#  1 2 3
#   1 2
#    1

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print("* "*(i+1))
#for i in range(n-1):
#    print("* "*(n-i-1))
#*
#* *
#* * *
#* * * *
#* * *
#* *
#*

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print((str(i+1)+' ')*(i+1))
#for i in range(n-1):
#    print((str(n-i-1)+' ')*(n-i-1))
#1
#2 2
#3 3 3
#4 4 4 4
#3 3 3
#2 2
#1

#for i in range(n):
#    print((chr(65+i)+' ')*(i+1))
#for i in range(n-1):
#    print((chr(63+n-i)+' ')*(n-i-1))
#A
#B B
#C C C
#D D D D
#C C C
#B B
#A

#n = int(input("Enter no of rows"))
#for i in range(n):
#    for j in range(i+1):
#        print(j+1,end=' ')
#    print()
#for i in range(n-1):
#    for j in range(n-i-1):
#        print(j+1,end=' ')
#    print()
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3
#1 2
#1

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print('  '*(n-i-1)+"* "*(i+1))
#for i in range(n-1):
#    print('  '*(i+1)+"* "*(n-i-1))
#      *
#    * *
#  * * *
#* * * *
#  * * *
#    * *
#      *

#n = int(input("Enter no of rows"))
#for i in range(n):
#    print('  '*(n-i-1)+(str(i+1)+' ')*(i+1))
#for i in range(n-1):
#    print('  '*(i+1)+(str(n-i-1)+' ')*(n-i-1))
#      1
#    2 2
#  3 3 3
#4 4 4 4
#  3 3 3
#    2 2
#      1



