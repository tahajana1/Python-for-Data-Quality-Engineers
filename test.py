import random
import statistics

#list of random numbers
lst = []
for i in range(101):
    x = random.randint(0,1001)
    lst.append(x)

#sort
n = len(lst)
for i in range(n):
    for j in range(0,n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j],lst[j + 1] = lst[j + 1],lst[j]


#list of even and odd
even = []
odd = []
for i in range(len(lst)):
    if lst[i]%2 == 0:
        even.append(lst[i])
    else:
        odd.append(lst[i])

#print(even)
print(statistics.mean(odd)) #average of odd numbers
print(statistics.mean(even)) #average of even numbers
