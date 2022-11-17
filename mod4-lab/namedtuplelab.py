from collections import namedtuple

myCustomer = namedtuple("Customer",["name", "age", "occupation", "customerID"])

customer = myCustomer("Corbin", 32, "Janitor", 8675309)

print(f"Customer name is {customer.name}. They are {customer.age}, work as a {customer.occupation}")