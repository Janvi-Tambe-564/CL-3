import xmlrpc.client

# Connect to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input from user
num = int(input("Enter a number: "))

# Remote procedure call
result = proxy.factorial(num)

print(f"Factorial of {num} is: {result}")
