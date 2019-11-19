'''
*
**
***
****
*****
'''

'''                $    stars     i
$$$$*        4       1             0
$$$**         3       2            1
$$***          2      3             2
$****          1       4             3
*****          0       5             4
               4 - i         i + 1
'''

# for i in range(5):
#     # print(i)
#     listForJ = range(i+1)
#     # print(list(listForJ))
#     for j in listForJ:
#         print('*', end='')
#     print()

# for i in range(5):
#     print('*' * (i+1)  )

for i in range(5):
    print(' ' * (4-i) + '*' * (i + 1))


'''stars    i 
   1         0
   2        1
  3         2
  4        3
  5        4'''