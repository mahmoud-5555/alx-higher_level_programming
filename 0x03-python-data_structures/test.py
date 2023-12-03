#!/usr/bin/python3
def no_c(my_string):
    return ''.join(map(lambda x: '' if x.lower() == 'c' else x, my_string))

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

