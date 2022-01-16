stop = 10
start = 0
step = 2
i = 1
while i <= stop:
    print(i)
    i+= step
    
print("done")

for i in range(1,10,1):
    print("n")

n = input("number: ")
for i in range(1,11):
    print(i*n)

n = int(input("enter number: "))

for i in range(1,11):
    if i*n % 2==0:
        print(i*n)

