n = int(input("Enter the number of data points: "))

x = []
y = []

for i in range(0,n):
    temp = int(input(f"Enter {i+1} x: "))
    x.append(temp)

for i in range(0,n):
    temp = int(input(f"Enter {i+1} y: "))
    y.append(temp)

mx = sum(x)/n
my = sum(y)/n

sumxy = 0

for i in range(0,n):
    temp = (x[i]-mx)*(y[i]-my)
    sumxy += temp

sumx = 0

for i in range(0,n):
    temp = (x[i]-mx)**2
    sumx += temp

w1 = sumxy/sumx
w0 = my - w1*mx

print(f"The linear regression equation is: y = {w1}x + {w0}")