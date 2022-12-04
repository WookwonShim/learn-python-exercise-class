# ----------------------------------------------------------------------------------------------------------
# Menu
# ----------------------------------------------------------------------------------------------------------
# - name: string
# - items: dict{string: integer}                           
# - start_time: integer     
# - end_time: integer
# ----------------------------------------------------------------------------------------------------------
# + __init__ (self, string, dict{string: integer}, integer, integer): void
# + print_info(self): void
# + calculate_bill(self, *string): void
# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------
# Franchise
# ----------------------------------------------------------------------------------------------------------
# - address: string
# - menus: list[Menu]                             
# ----------------------------------------------------------------------------------------------------------
# + __init__ (self, string, *Menu): void
# + __repr__ (self): void
# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------
# Business
# ----------------------------------------------------------------------------------------------------------
# - name: string
# - franchises: Franchise                            
# ----------------------------------------------------------------------------------------------------------
# + __init__ (self, string, *Franchise): void
# ----------------------------------------------------------------------------------------------------------


# Menu Definition ------------------------------------------------------------------------------------------
class Menu:
  # Constructor
  def __init__(self, name, items, start_time, end_time):
    self.name = name                   # name of the menu
    self.items = items                 # collection of items on the menu
    self.start_time = start_time       # menu avaialble from
    self.end_time = end_time           # menu available until
  # Print the menu's name with the start and end time info.
  def print_info(self):
    print(self.name + ' menu available from ' + str(self.start_time) + ' to ' + str(self.end_time))
  # Calculate and print the bill amount based on purchased_items.
  def calculate_bill(self, *purchased_items):    
    total_bill = 0 # initialized
    # a for loop to iterate over the input *args.
    for item in purchased_items:
      if item in self.items:
        # Add the price of the purchased item to total_bill
        total_bill += self.items[item]
      elif item not in self.items:
        print(item + " is not found on the menu. Please enter the correct name(s) of the purchased item(s)")
    # print the total bill amount.    
    print(total_bill)		
    
# Franchise Definition -------------------------------------------------------------------------------------
class Franchise:
  # Constructor
  def __init__(self, address, *menus):
    self.address = address
    self.menus = menus
  # Return the address
  def __repr__(self):
    print(self.address)
    return self.address
  # Take an integer vlaue (time) and print a list of Menu objects (available_menus).
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if (time >= int(menu.start_time)) & (time < int(menu.end_time)):
        available_menus.append(menu.name)
    if (len(available_menus) > 0):
      print(available_menus)
    elif (len(available_menus) == 0):
      print("There is no menu available.")

# Business Definition --------------------------------------------------------------------------------------
class Business:
  #Constructor
  def __init__(self, name, *franchises):
    self.name = name
    self.franchises = franchises

# Menu Initializations -------------------------------------------------------------------------------------
brunch = Menu(
  # name of the menu
  'Brunch',
  # items {'name1': price1, 'name2': price2, ...}
  {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
  },
  # start_time
  '1100',
  # end_time
  '1600'
  )
early_bird = Menu(
  # name of the menu
  'Early-bird dinners',
  # items {'name1': price1, 'name2': price2, ...}
  { 
    'salumeria plate': 8.00, 
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 
    'duck ragu': 17.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 1.50, 
    'espresso': 3.00
   }, 
   # start_time
   1500, 
   # end_time
   1800
   )
dinner = Menu(
  # name of the menu
  'Dinner',
  # items {'name1': price1, 'name2': price2, ...}
  {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 
    'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 2.00, 
    'espresso': 3.00
  },
   # start_time
  1700,
   # end_time
  2300
  )
kids = Menu(
  # name of the menu
  'Kids',
  # items {'name1': price1, 'name2': price2, ...}
  {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
  },
  # start_time
  1100,
  # end_time
  2100
  )
arepas_menu = Menu(
  # name of the menu
  "Take a' Arepa", 
  # items {'name1': price1, 'name2': price2, ...}
  {
    'arepa pabellon': 7.00, 
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
  },
  # start_time
  1000, 
  # end_time
  2000
  )

# Franchise Initializations -------------------------------------------------------------------------------
flagship_store = Franchise(
  # address of the flagship store
  '1232 West End Road', 
  # menus of the flagship store
  brunch, early_bird, dinner, kids)
new_installment = Franchise(
  # address of the new installment
  '12 East Mulberry Street', 
  # menus of the new installment
  brunch, early_bird, dinner, kids)
arepas_place = Franchise(
  # address of arepas_place
  '189 Fitzgerald Avenue', 
  # menu of arepas_place
  arepas_menu)

# Business Initializations -------------------------------------------------------------------------------
business1 = Business("Basta Fazoolin' with my Heart", flagship_store, new_installment)
business2 = Business("Take a' Arepa", arepas_place)

# Testing -------------------------------------------------------------------------------------------------
# early_bird.print_info()
# brunch.calculate_bill('pancakes', 'coffee') 
# repr(flagship_store)
# flagship_store.available_menus(1700)
# for menu in business1.franchises[0].menus: print(menu.name)
for menu in business2.franchises[0].menus: print(menu.name)
