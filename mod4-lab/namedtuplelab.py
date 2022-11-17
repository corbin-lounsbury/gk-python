# Instructions
# 1. Write a program to implement namedTuble
# 2. Create named tuple with type name and fields
# 3. Create a tuple from the named tuple
# 4. Access the values from tuple via field names
# 5. Print the final result

from collections import namedtuple

myCustomer = namedtuple("Customer",["name", "age", "occupation", "customerID"])

customer = myCustomer("Corbin", 32, "Janitor", 8675309)

print(f"Customer name is {customer.name}. They are {customer.age}, work as a {customer.occupation}")