
# can be instantiated using the constructor VendingMachine(num_items, item_price) where num_items denotes the number of items in the machine, and item_price denotes the required number of coins to buy a single item.
# has a method buy(req_items, money) that represents a buy request where req_items denotes the requested number of items, and money is the amount the customer puts into the machine. Depending on the state of the machine, one of the following happens
# If there are enough items in the machine to serve the request and the given money is sufficient to buy the requested number of items, the number of items in the machine is reduced by the requested number of items.  The method returns an integer denotes the change given back after the purchase.
# If there are fewer items in the machine than the requested number, it raises a ValueError exception with the message "Not enough items in the machine".
# If there are enough items in the machine to serve the request but the given amount of money is less than their cost, it raises a ValueError exception with the message "Not enough coins".
 

# The class implementation will be tested by a provided code stub and several input files. Each input file contains parameters to test the implementation. First, the provided code stub initializes an instance of the VendingMachine. Next, it performs the given operations on the VendingMachine instance. 
# The result of their execution will be printed to the standard output by the provided code.
# There will be at most 100 operations to be performed 
 
# Input Format Format for Custom Testing
# Sample Case 0
# Sample Input 0

# STDIN       Function
# -----       --------
# 10 2   →    num_items = 10, item_price = 2
# 4      →    n = 4
# 1 5    →    req_items = 1, money = 5       (1st transaction)
# 10 100 →    req_items = 10, money = 100    (2nd transaction)
# 7 100  →    req_items = 7, money = 100     (3rd transaction)
# 2 3    →    req_items = 2, money = 3       (4th transaction)
 

# Sample Output 0

# 3
# Not enough items in the machine
# 86
# Not enough coins
 

# Explanation 0

# The code initializes the VendingMachine: machine = VendingMachine(10, 2), i.e. a machine with 10 items, each costing 2 coins. Then, there are 4 operations to be performed:

# The method buy(1, 5) is called, i.e. a request of buying 1 item with 5 units of currency is performed. There are enough items in the machine to serve the request and the given money is sufficient to purchase them.  The change, 5-1*2 = 3 in this case, is returned by the method, and the number of items in the machine is reduced by 1.  There are 9 items in the machine after the request.
# The method buy(10, 100) is called, i.e. a request of buying 10 items with 100 units of currency is performed. There are not enough items in the machine to serve the request , so a ValueError is raised with the message "Not enough items in the machine".
# The method buy(7, 100) is called, i.e. a request of buying 10 items with 100 units of currency is performed. There are enough items in the machine to serve the request and the given money is sufficient to purchase them.  The change, 100-7*2 = 86, is returned and the number of items in the machine is reduced by 7.  Now there are 9 - 7 = 2 items in the machine.
# The method buy(2, 3) is called, i.e. a request of buying 2 items with 3 units of currency is performed. There are enough items in the machine but the money is not enough.  A ValueError is raised with the message "Not enough coins".
class VendingMachine():
    def __init__(self,variable1,variable2):
        self.variable1=variable1
        self.variable2=variable2

    def buy(self,x,y):
        if(self.variable1>=x and x*self.variable2<=y):
            self.variable1-=x
            return y-(x*self.variable2)
        else:
            if(self.variable1<x):
                return "Not enough items in the machine"
            else:
                return "Not enough coins"
            
if __name__ == '__main__':


    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)
    print(machine)
    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
    #     try:
    #         change = machine.buy(num_items, num_coins)
    #         fptr.write(str(change) + "\n")
    #     except ValueError as e:
    #         fptr.write(str(e) + "\n")


    # fptr.close()