# Falsy
print([] and [])  # short circuit 概念

if []:
    print("empty list is true in boolean context")
else:
    print("empty list is false in boolean context")

# bool() 可以判斷 Truthy or Falsy
print(bool(""))
