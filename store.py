import json
from player import Player

class Store:
   #User picks which factory to view additional stats for (chose in store_inventory() )
   def __init__(self):
      with open('json_folder/gameObjects.json', 'r') as file:
         gameObjects_data = json.load(file)
      self.factories = gameObjects_data['store_factories']
      self.inventories = gameObjects_data['inventories']
   
   def item_stats(self, item_num):
         factory = self.factories[item_num]
         for key, value in factory.items():
            clean_key = key.replace("_", " ").upper()
            if isinstance(value, str):
               print(f"{clean_key}: {value.upper()}")
            else:
               print(f"{clean_key}: {value}")

   #lists all factories in the store ***POSSIBLE JSON***
   def interact(self):
      #print factories
      print("FACTORIES\n")
      for i in range(len(self.factories)):
         print(f"[{i+1}] {self.factories[i]['name']}: ${self.factories[i]['cost']}")  #add availibilty

      #option system
      # 1 to buy, 2 for stats, non-valid num = loop 
      while True:
         answer = int(input("Type 1 to buy or 2 for item stats: "))
         if answer == 1:
            to_buy = int(input("\nType the number of the factory you wish to purchase: ")) - 1
            player = Player()                
            player.buy_factory(self.factories[to_buy])
         elif answer == 2:
            to_stat = int(input("Type the number of the factory you would like more stats on: ")) - 1
            print("\n")
            self.item_stats(to_stat)
         else:
            print("Invalid Number\n")