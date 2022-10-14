heads = int(input('Enter  total heads'))
legs = int(input('Enter total legs'))
if legs % 2!= 0 or heads == 0 or heads > legs:
    print('NO SOLUTION')
else:
    rabbit = (legs-2*heads)/2
    chicken = heads-rabbit
    print('rabbit count is :', rabbit)
    print('chicken count is :', chicken)
