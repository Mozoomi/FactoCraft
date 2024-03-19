import json

class Player:
   def __init__(self):
      self.inventory_file = "json_folder/running_gameObjects.json"
      self.inventory_data = self.load_factoryData()

   def load_factoryData(self):
      with open(self.inventory_file, 'r') as file:
         file_data = json.load(file)
      return file_data
   
   def update_factoryData(self):
      with open(self.inventory_file, 'w') as file:
         json.dump(self.inventory_data, file, indent=4)

   def new_factory(self, factory_name):
      factory_data = self.inventory_data['store_factories'].pop(factory_name, None)
      if factory_data:
         self.inventory_data['inventories'][0]['inventory_factories'][factory_name] = factory_data
         self.update_factoryData()
         print(f"You are now the official and proud owner of {factory_name}!")
      else:
         print(f"Factory {factory_name} not found in base factories.")

   def collect(self, factory):
      factory_data = self.inventory_data['inventories'][0]['inventory_factories'].get(factory)
      if factory_data:
         product = factory_data["product"]
         amount_held = factory_data["holding"]
         if product not in self.inventory_data['inventories'][0]["inventory_items"]:
            self.inventory_data['inventories'][0]["inventory_items"][product] = amount_held
         else:
            self.inventory_data['inventories'][0]["inventory_items"][product] += amount_held
         factory_data["holding"] = 0
         self.update_factoryData()

         print(f'{factory} Holding Collected: {amount_held}')
      else:
         print(f'Factory {factory} not found in inventory.')

   def buy_factory(self, factory_name):
      factory_data = self.inventory_data['base_factories'].get(factory_name)
      if factory_data:
         if factory_data['cost'] <= self.money:
            factory_data['availabilty'] = False
            self.money -= factory_data["cost"]
            self.new_factory(factory_name)
         else:
            print("You don't have enough money for this.")
      else:
         print(f"Factory {factory_name} not found in base factories.")

   def factoryStats(self):
      for factory_name, factory_data in self.inventory_data['inventories'][0]['inventory_factories'].items():
         print(f"Factory: {factory_name}")
         print(f"Product: {factory_data['production_rate']}")
         print(f"Production Rate: {factory_data['production_rate']}")
         print(f"Capacity: {factory_data['capacity']}")
         print(f"Cost: {factory_data['cost']}")
         print('\n')
