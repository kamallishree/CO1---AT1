def index_builder(n):
    if n <= 1:
        return 1
    return index_builder(n // 2) + 1
n = int(input("Enter number of web pages: "))
print("Operations Required:", index_builder(n))
