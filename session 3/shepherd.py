
#2.1
print('--2.1--')
import random
sheepherd = random.sample(range(8,300),7)
print('There are my sheep size: ')
print(sheepherd)
#2.2
print('--2.2--')
biggest = 0
for i in range(len(sheepherd)):
    if sheepherd[i] > biggest:
        biggest = sheepherd[i]
print('Now my biggest sheep has size',biggest,"Let's shear it")
#2.3
print('--2.3--')
position = sheepherd.index(biggest)
sheepherd[position] = 8
print('After shearing, here is my flock:')
print(sheepherd)
#2.4
print('--2.4--')
sheepherd = [sheep + 50 for sheep in sheepherd]
print('One month has passed, now here is my flock:')
print(sheepherd)
#2.5
print('--2.5--')
month = int(input('How many month have passed: '))
print('START :')
print('There are my start sheep size: ')
print(sheepherd)
print()

for i in range (month):
    print('MONTH',i+1)
    sheepherd = [sheep + 50 for sheep in sheepherd]
    print('One month has passed, now here is my flock:')
    print(sheepherd)

    biggest = 0
    for j in range(len(sheepherd)):
        if sheepherd[j] > biggest:
            biggest = sheepherd[j]
    print('Now my biggest sheep has size', biggest, "Let's shear it")

    position = sheepherd.index(biggest)
    sheepherd[position] = 8
    print('After shearing, here is my flock:')
    print(sheepherd)
    print()

#2.6
print('--2.6--')

totalsize = sum( sheep for sheep in sheepherd)
print('My flock has total size of:',totalsize)
money = totalsize * 2
print('I would get {0} {1} {2} = {3}{4}'.format(totalsize,'*','2$',money,'$'))

