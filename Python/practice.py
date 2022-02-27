# arr=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
# # print(arr)
# for i in range(3):
#     for j in range(3):
#         print(arr[i][j:j+3])
# row=['s']
# print("-".center(10, "a"))
# thickness=5
# c='s'
# for i in range(9):
# #     # print((c*(thickness-i-1)).rjust(thickness))
# #     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
#     # print((c*i).rjust(thickness-1)+c)
#     # print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    
#     print(('s'*i).rjust(10))
# from collections import OrderedDict
# string="Sonu Dutta"
# for i in range (0,len(string),2):
        # print('-'.join(OrderedDict.fromkeys(string[i:i+2])))
from collections import namedtuple
n, Score = int(input()) , namedtuple('Score',input().split())
scores = [Score(*input().split()).MARKS for i in range(n)]
print("%.2f"% (sum(map(int,scores))/n))