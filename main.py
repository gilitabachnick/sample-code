#Solution to question 1:
def Reverse_string(str):
  new_str = str[::-1]
  print(new_str)
Reverse_string("Automation")
#Solution to question 2:
def bord_print(list, i):
  max_word = max(len(word) for word in list)
  border = '*' * (max_word + 4)
  print(border)
  for word in list:
   i+= 1
   sum = (max_word) - len(list[i])
   print ("*"+ " "+ (word)+(" " * (sum+1 ) +"*"))
  print(border)
    
l= ["Hello", "World", "in", "a", "frame"]
i=-1
bord_print(l, i)
#Solution to question 3:
def sort_list(lists):
  new_arr = []
  arr = set()
  for number in lists:
   if isinstance(number,(int,float)) and number not in arr and number!=False:
     new_arr.append(number)
     arr.add(number)
  print(new_arr)
My_list = [1, 3, 67, "1", "62", "Foo", "3", 5, 1, 3, False, 1.3]
sort_list(My_list)
#Solution to question 4:
def file_type(arr):
  lists = {
  "video":[],
  "Image&":[],
"Audio":[]
}
  for type in arr:
    if type.endswith("mp4"):
      lists["video"].append(type)
    elif type.endswith("wav"):
      lists["Audio"].append(type)
    else:
      lists["Image&"].append(type)
  print(lists)    
Types = ["Entry One.mp4", "Entry Two.wav", "Entry Three.jpg", "Entry Four.mng", 
"Entry Five.png", "Entry Six.csv"]
file_type(Types)
#Solution to question 5:
def unique_names(str_a, str_b):
  New_str =list( set(str_a + str_b))
  return(New_str)
first_list_names = ["Marco", "Andrei", "Tokyo"]
second_list_names = ["Andrei", "Sophia", "Pablo"]
print(unique_names(first_list_names,second_list_names))
#Solution to question 6
def trial_a(dictionary):
  set= {}
  for type, name in dictionary.items():
    if name in set:
      set[name].append(type)
    else:
      set[name]= [type]
  return(set)    
files = {
 "Input.txt": "Oslo",
 "Code.py": "Stan",
 "Output.txt": "Oslo"
 }
print(trial_a(files))
#Solution to question 7:
def str_ing(string):
  if len(string) <= 2:
   print(string) 
  elif (string.endswith("ing") or string.endswith("ING")):
   print(string + "ly")
  else:
   print(string + "ing") 
str_ing(input("enter string:"))