from collections import OrderedDict
def merge_the_tools(string, k):
    l=len(string)
    for i in range (0,l,k):
        print(''.join(OrderedDict.fromkeys(string[i:i+k])))
        
if __name__ =='__main__' :
    string,k=input(),int(input())      
    merge_the_tools(string,k)