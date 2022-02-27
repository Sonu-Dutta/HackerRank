
# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
# Example
# The maximum height candles are  units high. There are  of them, so return .
# Function Description
# Complete the function birthdayCakeCandles in the editor below.
# birthdayCakeCandles has the following parameter(s):
# int candles[n]: the candle heights
# Returns
# int: the number of candles that are tallest
# Input Format
# The first line contains a single integer, , the size of .
# The second line contains  space-separated integers, where each integer  describes the height of .

# Sample Input 0

# 4
# 3 2 1 3
# Sample Output 0

# 2
# Explanation 0

#  The tallest candles are 3 units, and there are 2 of them.

candles=[3,2,1,3,3]
# print(candles.count(max(candles)))
n=len(candles)
count=0
max=0
for i in range(n):
    if candles[i]>max:
        max=candles[i]
        count=1
    elif candles[i]==max:
        count+=1
print(count)
