Question:
Write a function to calculate the sum of even number in a given list of intergers.
The function should take a list of intergers as input and return the sum of all even number in the list


Solution:
a = list(map(int, input().split()))

even_no =[]

for i in a:
   if(i % 2 == 0):
      even_no.append(i)

print(sum(even_no))



Input:
1 2 3 4 5 6 7 8 9 10

Output:
30
