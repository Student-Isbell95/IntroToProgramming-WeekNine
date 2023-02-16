print("Hello! Hope you are having a great day!")
print()
name = input("What is your name: ")
print()
print("...")
print()
print("Hello, " + name)
print()
print("Please tell which of these three are your favorite Pokemon.")
print()
print("Charmander")
print()
print("Squirtle")
print()
print("Bulbasaur")
print()
pokemon = input("My favorite Pokemon is: ")

if pokemon == "Charmander":
  print("Charmander is pretty cool! He isn't very helpful in the beginning of the game though...")

elif pokemon == "Squirtle": 
  print("Squirtle is cool too! I like his sunglasses in the anime!")

elif pokemon == "Bulbasaur":
  print("Bulbasaur is the best!")

else: 
  print("Please pick one of the Pokemon listed above.")
  
