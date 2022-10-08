customer = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
value = input()

for ch in value:
    print(customer.get(ch))
