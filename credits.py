import time
import subprocess
rows, columns = subprocess.check_output(['stty', 'size']).split()
rows = int(rows) - 1
columns = int(columns) - 1

def get_credit(credit_num):
    length = ((columns - 3) - len(credits[credit_num])) / 2
    line = '|'
    if length % 1 != 0:
        length = int(length - 0.5)
        line += ' '
    else:
        length = int(length)
    for i in range(length+1):
        line += ' '
    line += credits[credit_num]
    for i in range(length+1):
        line += ' '
    line += '|'
    return line


def gen_row(line_number, frame_number):
    line = '|'
    for k in range(len(credits)):

        if line_number == (((12 * k ) + 21) - frame_number):
            line = get_credit(k)
            return line
#    if line_number == (21 - frame_number):
#        line = get_credit(0) 
#        return line
#    if line_number == (33 - frame_number):
#        line = get_credit(1)
#        return line
#    if line_number ==  (57 - frame_number):
#        line = get_credit(2)
#        return line
    for i in range(int(columns / 2)):
        if (line_number + frame_number) % 6 == 0:
            line += '**'
        else:
            line += '  '
    return line + '|' 

credits = [
        'Director: Stewart Schrieffer',
        'Github: www.github.com/StewSchrieff',
        'Special Thanks To: Vim',
        'Fin.'
        ]
my_line = '|'
for k in range(columns - 1):
    my_line += '_'
my_line += '|'
for i in range(50):
    time.sleep(0.4)
    print(my_line)
    for j in range(rows):
        print(gen_row(j,i))
    print(my_line)

