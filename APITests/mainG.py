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
Names = ["Aviad", "Gili", "Zevi", "Sari"] 
i =0
for Name in Names:
   if Names[i] != "Zevi":
    print(f"{Name}")
    i+= 1
   else:
    print(f"{Name}"+""+"Jacobson")
    i+= 1
  
  