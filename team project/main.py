from customers import customers
from operators import operators
from manager import main
# from simulate import vehicles, orders
# vehicles()
# orders()

role = input("Enter a role here(customers, operators, managers) (enter quit to quit the system): ")

while role == 'customers' or role == 'operators' or role == 'managers':

    if role == 'customers':
        customers()
    elif role == 'operators':
        operators()
    elif role == 'managers':
        main()
    role = input("Enter a role here(customers, operators, managers) (enter quit to quit the system): ")