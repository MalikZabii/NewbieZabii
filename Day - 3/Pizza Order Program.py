print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_cheese = input("Do you want extra cheese? Y or N ")
if size == "S":
  bill=15
elif ("size ==M"):
  bill=20
else:
  bill=25
if add_pepperoni == "Y":
  add_pepperoni=2
if add_cheese == "Y":
  add_cheese=1
if add_pepperoni == "N":
  add_pepperoni=0
if add_cheese == "N":
  add_cheese=0
bill_1 = bill + add_pepperoni + add_cheese
print ("Your Final Bill is:", bill_1)