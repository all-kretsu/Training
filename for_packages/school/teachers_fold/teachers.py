import sys
sys.path.append('C:\Users\PC\Desktop')

from parents.parent import parent_func

# teacher file
for p in sys.path:
    print(p)

def teacher_func():
    print('Hello for teachers!')

parent_func()