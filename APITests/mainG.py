number = 10
while True:
  user_input= input("Do you want to play? (y/n)").lower()
  if user_input == "n":
      break
  user_number= int(input("select number:"))
  if user_number == number:
    print("Kudos!")
  elif abs(number -user_number) ==1:
    print("you were off by one")
  else:
    print("sorry, maybe next time!")
  