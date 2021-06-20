from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
the_end=False
new_dict={}
while not the_end:
  print("Welcome to the Secret Auction program!")
  name=input("What is your name? ")
  bid=int(input("What's your bid? $"))
  
  new_dict[name]=bid
  
  others=input("Are there any other bidder?   Type 'yes' or 'No' ")
  if others=="yes":
    clear()
  elif others=="no":
    the_end=True
smallest=-1
for key in new_dict:
  value=new_dict[key]
  if value>smallest:
    smallest=value
    key_name=key
print(f"{key_name} is the winner with ${smallest}")
  






