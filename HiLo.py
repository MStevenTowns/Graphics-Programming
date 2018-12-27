import random
w=random.randint(1,100)
x=0
while x!=w:
    try:x=int(input('Guess a number>'))
    except:print('Bad input, try again')
    if 0<x<w:print('Too low, try again')
    if x>w:print('Too high, try again')
print('You Win!')
