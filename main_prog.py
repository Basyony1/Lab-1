#Abdelsalam Basyony- Lab 1 variant 4
import os
import time


WHITE = '\u001b[47m'
RED = '\u001b[41m'
END = '\u001b[0m'

# Poland flag  
for i in range(4):
    print(f"{WHITE}{'    '*10}{END}")
    
for i in range(4):
    print(f"{RED}{'    '*10}{END}")
     
time.sleep(3)

SWAP_SLIDE_TIME = 3


SET_COLOR = "\x1b[48;5;"
#parameters and drawimg the pattern
color = 37
length = 5
repeat_amount = 6

def draw_Pattern_d():
    print(f"{'  '*length}{SET_COLOR}{color}m  {END}"*repeat_amount)

def fill():
    print(f'{SET_COLOR}{color}m{'  '*length*(repeat_amount+2)}{END}')




for i in range(3):      # the pattern
    fill()
    draw_Pattern_d()

time.sleep(3)

# FOR GRAPH y=x^0.5 
# Define the range of x-values
x = 100  
y = int(x**0.5)  # maximum y value for scaling

# Loop 
for y in range(y, -1, -1):
    # Build the line for each y-level
    line = ""
    for x in range(x+1):
        if int(x**0.5) == y:  # i Check if the square root of x matches the current y level
            line += "*"  # Plot a star where the function value matches y
        else:
            line += "-"  # Leave space elsewhere

    print(line)
print('0  10 20  30 \t 40 \t 50 \t    60 \t\t   70 \t\t   80 \t  \t   90 \t \t   100')

END = '\u001b[0m'
SET_COLOR = "\x1b[48;5;"
time.sleep(3)

# then the condition (Условие)
file_list = [float(i) for i in open('sequence.txt')]

#the first average 
count1 = []
for i in range(125):
    count1.append(abs(file_list[i]))
count1 = sum(count1)/125

#the second average
count2 = []
for i in range(125,250):
    count2.append(abs(file_list[i]))
count2 = sum(count2)/125

print(f"the first average: {SET_COLOR}10m{' '*round(count1*10)}{END}")
print(f"the second average: {SET_COLOR}14m{' '*round(count2*10)}{END}")
time.sleep(3)
