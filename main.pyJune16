KebabHalalPizza = 'A pizza restaurant located at 2371 Weston Road, Toronto, ON and own an average of 4.5/5 stars. They sell pizza, wings and other delicious side like onion rings, Tandoori chicken legs and poutine.' #toronto #food
StarBiryani = 'A Biryani-based restaurant that offers many Vegetarian friendly meals but also many beef centered meals. Located at 3216 Eglinton Ave E, Toronto and has a 4.3 rating on Uber Eats.' #tortonto food
AlKaramSweets = 'A dessert shop located at 3001 Markham Road, Unit 15 that sells syrup sweets, assorted sweets and other snacks.' #toronto food 
ApnaFarm = 'Specializing in meat and deli products, Apna Farms is one of the leading grocers for Halal meat.They are in Mississauga located at 2965 Hazelton Pl #1&2.' #mississauga food
Shabis = 'A clothing store for brides specially designed to displaying up and coming designers. They are located in Richmond Hill at 10737 Yonge Street, Unit 17.' #toronto clothing
TunTravel= 'An airline travel company located 1328 Eglinton Ave, Toronto, ON, Canada, L4W 4N9.' #calgary 
WildFish= 'A store that produces and sells non-toxic fishing equipment for types of fishing. You can access their website here www.LeadFreeLures.com' #calgary Store
Autorebex = 'An automotive service centre that sells vehicles and also do repairs to parts. They are also a towing service and have been in business since 1992. Located at 930 Wellington St. W.' #ottawa automotive
WealthManagment = 'An insurance company which can manage securing your future, planning for major expenses, helping with businesses, and much more. They can be found at 701-305 Milner Ave, Toronto, ON, Canada, M1B3V4 ' #Edmonton Insurance 
Immigration = 'Specialize in work permits, study permits, visitor visa, caregiver programs, and much more. They can be found at 1965 Britannia Road West, 208, Mississauga, ON, Canada, L5M 4Y4' #Halifax Immigration
NageenabyNaureen = "Specialize in designer and customized jewellery. Can be contacted by phone(4166253971)." #store Halifax
MannLawyers = 'A law firm for any top quality top quality services and are very successful in the service they provide. They are located at 11 Holland Avenue #300 in Ottawa.' # ottawa
GazelleMedia = 'A graphic design company that markets other businesses online to get them professional publicity.They can be found online at gazellemedia.net.' #regina online marketing


print('Welcome to our program. We hope that it will be very helpful in finding Muslim owned business across the GTA. \n \nTo get started, please type a number.\n \n 1. Search a business by name, if you already know a business in our program. \n 2. Search by business type. \n 3. View the whole list of businesses in alphabetical order. \n 4. Add a business to the list.')

print('''To exit the program at any time, please type 'Exit'.\n''')
myList = ['Kebab Halal Pizza', 'Star Biryani', 'Al-Karam Sweets', 'Apna Farm', "Shabi's"]

newInput = str(input())

while newInput != '1' and newInput != '2' and newInput != '3' and newInput != 'Exit':
  print('Invalid number typed. Please type a number between 1 and 3.')
  newInput = str(input())

if newInput == '1':
  print('Please search a business by name to know more about it.')
  newInputTwo = str(input())

elif newInput == '2':
  print('Please type any of the following categories to see its businesses.')
  print('Food\nClothing\n ')
  food = myList[0:2] 
  clothing= myList[4]
  typeInput= str(input())
  while typeInput != 'Food' and typeInput != 'Clothing':
    print('Invalid business type try again:')
    typeInput= str(input())
  if typeInput == 'Food': 
    food.sort()
    print()
    print("Food related businesses:")
    for i in range(0,len(food),1):
      print(food[i])
  elif typeInput == 'Clothing':
    print()
    print("Clothing related businesses:")
    print(clothing)
  


elif newInput == '3':
  print('Please search one of the businesses to view more information about it.\n')
  myList.sort()
  for i in range(0, len(myList), 1):
    print(myList[i])
  print()

  newInputThree = str(input())
  
  while newInputThree != '1. Kebab Halal Pizza' and newInputThree != '2. Star Biryani'and newInputThree != '3. Al-Karam Sweets' and newInputThree != "Shabi's":
    newInputThree = str(input())

  if newInputThree == '1. Kebab Halal Pizza':
    print(KebabHalalPizza)
  elif newInputThree == 'Star Biryani':
    print(StarBiryani)
  elif newInputThree == 'Al-Karam Sweets':
    print(AlKaramSweets)
  elif newInputThree == "Shabi's":
    print(Shabis)

elif newInput == '4':
  print('Add a business to the list and press enter.')
  newInputFive = str(input())

elif newInput == 'Exit':
  print()

