#Code below working after editing your code
#weight = w
#height = h
w = float (input())
h = float (input()) 
r = w / (h**2)
if r <18.5:
    print('Underweight')
elif r >=18.5 and r < 25:
    print('Normal')
elif r >=25 and r <30:
    print('Overweight')
elif r >30:
    print('Obesity')