# Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.


import math
for i in range(1000,10000):
    if math.sqrt(i)%1==0:
        if int(i%10)%2==0:
            if int((i/10)%10)%2==0:
                if int((i/100)%10)%2==0:
                    if int((i/1000)%10)%2==0:
                        print(i)