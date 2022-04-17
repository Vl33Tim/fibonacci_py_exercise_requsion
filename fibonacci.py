# num = int(input())
# num = 10

# def fibonacci(n):
#     if n<3:
#         return 1
#     # print(fibonacci(n - 1) + fibonacci(n - 2))
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(num))
# below is example of fibonacci func but in some "dirty" way
num = int(input())
def fibonacci(n):
    a, b = 1, 1
    for i in range(n-1):
        yield a
        a, b = b, a + b

data = list(fibonacci(num))
print(0)
for number in data:
    print(number)