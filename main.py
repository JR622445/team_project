# research of businesses were evenly split
KebabHalalPizza = 'A pizza restaurant located at 2371 Weston Road, Toronto, ON and own an average of 4.5/5 stars. They sell pizza, wings and other delicious side like onion rings, Tandoori chicken legs and poutine.' #toronto #food
StarBiryani = 'A Biryani-based restaurant that offers many Vegetarian friendly meals but also many beef centered meals. Located at 3216 Eglinton Ave E, Toronto and has a 4.3 rating on Uber Eats.' #toronto food
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
GraphicDesign= 'They specialize in internet applications, software development, and netwrok infastructure. They can be located at 124 Mavety Street, Toronto, ON, Canada' #store Kingston
QuranProgram= 'They specialize in teaching The Quran to all types of different ages from kids to adults. They can be found 3195 Erindale Station Rd, Mississauga, Ontario, Canada, L5C 1Y5' #Education Kingston
ChildrenClothing= 'A store that sells high quality and afforable Islamic Thobes,Islamic Tshirts, onesies, etc. They can be contacted muslimchild.ca' #Store Kingston
HalaCommerce = 'Islamic lifestyle marketplace providing halal, organic products. They can be contacted 416-829-9730' #Store Kitchener
WaveFitness = 'A Vancouver based fitness service that provide one-on-one sessions at great rates at home or at your gym. Found at info@wavefitnessclub.com and also on Instagram and Facebook at WaveFitness.' #gym vancouver
ThinkTravel = 'A travel agency in Winnipeg that provide affordable prices for tours, cruises, safaris, and air fares. Many locations and head office is in Calgary at 1503 3800 Memorial Dr NE.' #
EleganceBeard= 'A barber shop which can be contacted here elegancebeard.com' #Store Kitchener
Dignitii = "An online sportwear company for Muslim women in the Kitchener and Waterloo area. found at https://www.dignitii.com." #waterloo online sportswear

print('Welcome to our program. We hope that it will be very helpful in finding Muslim owned business across Canada. \n \nTo get started, please type a number.\n \n 1. Search a business by name, if you already know a business in our program. \n 2. Search by business type. \n 3. View the whole list of businesses in alphabetical order. \n 4. Add a business to the list.')

print('''To exit the program now, please type 'Exit'.\n''')
myList = ['Kebab Halal Pizza', 'Star Biryani', 'Al-Karam Sweets', 'Apna Farm', "Shabi's", 'Tun Travel', 'Wild Fish', 'Autorebex', 'Wealth Managment', 'Immigration', 'NageenabyNaureen', 'Mann Layers', 'Gazelle Media', 'Graphic Design', 'Quran Program', 'Children Clothing', 'Halal Commerce', 'Wave Fitness', 'Think Travel', 'EleganceBeard', 'Dignitii']

#Joshua
newInput = str(input())

while newInput != '1' and newInput != '2' and newInput != '3' and newInput != 'Exit':
  print('Invalid number typed. Please type a number between 1 and 3.')
  newInput = str(input())

if newInput == '1':
  print('Please search a business by name to know more about it.')
  newInputTwo = str(input())


#Kianoush
elif newInput == '2':
  print('Please type any of the following categories to see its businesses.')
  print('Food\nStore\nTransportation\nMedia\nOther ')
  print()
  food = [myList[0],myList[1],myList[2],myList[3],] 
  Store= [myList[4],myList[6],myList[7],myList[10],myList[13],myList[15],myList[16],myList[19],myList[20]]
  transportation = [myList[5], myList[9]]
  media = [myList[12]]
  other = [myList[8],myList[11],myList[14],myList[17],myList[18]]
  
  typeInput= str(input())
  print()
  while typeInput != 'Food' and typeInput != 'Transportation' and typeInput != 'Store' and typeInput != 'Media' and typeInput != 'Other':
    print('Invalid business type try again:')
    typeInput= str(input())
  if typeInput == 'Food': 
    food.sort()
    print("Food related businesses:")
    for i in range(0,len(food),1):
      print(food[i])
  elif typeInput == 'Store':
    print()
    print("Stores:")
    for i in range(0,len(Store),1):
      print(Store[i])
  elif typeInput == 'Transportation':
    print('Transportation related businesses:')
    for i in range(0,len(transportation),1):
      print(transportation[i])
  elif typeInput == 'Media':
    print('Media related businesses:')
    for i in range(0,len(media),1):
      print(media[i])      
  elif typeInput == 'Other':
    print('Other related businesses:')
    for i in range(0,len(other),1):
      print(other[i])    
      

#Joshua
elif newInput == '3':
  print('Please search one of the businesses to view more information about it.\n')
  for i in range(0, len(myList), 1):
    print(myList[i])
  print()

  newInputThree = str(input())
  
  while newInputThree != 'Kebab Halal Pizza' and newInputThree != 'Star Biryani'and newInputThree != 'Al-Karam Sweets' and newInputThree != "Shabi's" and newInputThree != "Tun Travel" and newInputThree != "WildFish" and newInputThree != "Autorebex" and newInputThree != "Wealth Managment" and newInputThree != "Immigration" and newInputThree != "NageenabyNaureen" and newInputThree != "Mann Lawyers" and newInputThree != "Gazelle Media" and newInputThree != "Graphic Design" and newInputThree != "Quran Program" and newInputThree != "Children Clothing" and newInputThree != "Hala Commerce" and newInputThree != "Think Travel" and newInputThree != "EleganceBeard" and newInputThree != "Dignitii" and newInputThree != "Apna Farm":
    print('Invalid business type try again.')
    newInputThree = str(input())

  if newInputThree == 'Kebab Halal Pizza':
    print(KebabHalalPizza)
  elif newInputThree == 'Star Biryani':
    print(StarBiryani)
  elif newInputThree == 'Al-Karam Sweets':
    print(AlKaramSweets)
  elif newInputThree == "Shabi's":
    print(Shabis)
  elif newInputThree == 'Tun Travel':
    print(TunTravel)
  elif newInputThree == 'WildFish':
    print(WildFish)
  elif newInputThree == 'Autorebex':
    print(Autorebex)
  elif newInputThree == 'Wealth Management':
    print(WealthManagment)
  elif newInputThree == 'Immigration':
    print(Immigration)
  elif newInputThree == 'NageenabyNaureen':
    print(NageenabyNaureen)
  elif newInputThree == 'Mann Lawyers':
    print(MannLawyers)
  elif newInputThree == 'Gazelle Media':
    print(GazelleMedia)
  elif newInputThree == 'Graphic Design':
    print(GraphicDesign)
  elif newInputThree == 'Quran Program':
    print(QuranProgram)
  elif newInputThree == 'Children Clothing':
    print(ChildrenClothing)
  elif newInputThree == 'Hala Commerce':
    print(HalaCommerce)
  elif newInputThree == 'Wave Fitness':
    print(WaveFitness)
  elif newInputThree == 'Think Travel':
    print(ThinkTravel)
  elif newInputThree == 'EleganceBeard':
    print(EleganceBeard)
  elif newInputThree == 'Dignitii':
    print(Dignitii)
  elif newInputThree == 'Apna Farm':
    print(ApnaFarm)

elif newInput == '4':
  print('Add a business to the list and press enter.')
  newInputFive = str(input())

elif newInput == 'Exit':
  print()

