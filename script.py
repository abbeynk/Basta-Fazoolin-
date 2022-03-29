class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = []
class Franchise:
  def __init__(self, address, menus, name):
    self.address = address
    self.menus = menus
    self.name = name
  def __repr__(self):
    return "The {} franchise is located at {}".format(self.name, self.address)
  def available_menus(self, time):
    print("Military time to Standard time conversion:")
    print("[Brunch: 11AM-4PM, Early Bird: 3PM-6PM, Dinner: 5PM-11PM, Kids: 11AM-9PM, Arepa: 10AM-8PM]")
    print()
    available_menus = []
    self.time = time
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    print("The time you requested: {}, has these menu choices:".format(time))
    for available_menu in available_menus:
      print(available_menu)
    return "Based on time, there are other menus as well."
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "The {} menu is available from {} to {}.".format(self.name, self.start_time, self.end_time)
  def calculate_bill(self, purchased_items):
    print("You ordered:")
    total_bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        total_bill += self.items[purchased_item]
      else:
        print("You ordered an item not on the menu which is not available")
      print("{} - ${:.2f}".format(purchased_item, self.items[purchased_item]))
    return "Your '{}' menu total is: ${:.2f}.\n".format(self.name, total_bill)
brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},1100, 1600)
early_bird = Menu("Early Bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},1500, 1800)
dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},1700, 2300)
kids = Menu("Kids",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 1100, 2100)
arepas = Menu("Take a Arepa",{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
},1000, 2000)
"""
print(brunch)
print(early_bird)
print(dinner)
print(kids)
"""
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(kids.calculate_bill(['chicken nuggets', 'apple juice']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
print(arepas.calculate_bill(['arepa pabellon', 'guayanes arepa', 'guayanes arepa']))
menus = [brunch, early_bird, dinner, kids, arepas]
flagship_store = Franchise("1232 West End Road", menus, "flagship")
new_installment = Franchise("12 East Mulberry Street", menus, "new installment")
arepas_place = Franchise("189 Fitzgerald Avenue", menus, "arepas place")
print(flagship_store)
print(new_installment)
print(arepas_place)
print("For the '{}' franchise:".format(flagship_store.name))
print(flagship_store.available_menus(1200))
print("For the '{}' franchise:".format(new_installment.name))
print(new_installment.available_menus(1700))
print("For the '{}' franchise:".format(arepas_place.name))
print(arepas_place.available_menus(1800))
the_franchises = [flagship_store, new_installment]
basta_business = Business("'Basta Fazoolin' with my Heart'", the_franchises)
print("The name of this business is:\n{}\nIt has two franchises:\n{},\n{}.".format(basta_business.name, the_franchises[0], the_franchises[1]))
take_business = Business("'Take a Arepa'", arepas_place)
print("The name of this business is:\n{}\nIt has 1 franchise:\n{}.".format(take_business.name, arepas_place))