print(
  '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("wellcome to the treasure island")
direction = input("Which direction do you want to go ? 'left','right'")
if direction == 'left':
  choice = input(
    "You have entered the island ? if you like to wait type 'wait' or type swim to move forward'swim"
  )
  if choice == 'wait':
    choice_2 = input(
      "you have enterd the island.It has 3 doors...red,yellow and blue.....type 'yellow','red','blue' to enter these doors"
    )
    if choice_2 == 'red':
      print("this the room of fire...game over you have lost")
    elif choice_2 == "yellow":
      print("you have entered the treasure room...this treassure is yours")
    else:
      print("game over...its the room full of beasts")
  else:
    print("you have attacked by sharks....you have lost")

else:
  print("Gave over....try again next time...the right direction has danger ")
