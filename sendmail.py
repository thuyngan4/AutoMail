a = 12

b = 15

c = 18

if a%2==0:

    if b%c == 1:

        c-=5

        b+=12

    if c%a == 6:

        b-=13

    else:

        a=b=c=0

print(a,c)