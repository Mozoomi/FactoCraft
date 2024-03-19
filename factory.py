import time 
import threading
import json

class Factory:
   
   def __init__(self, product, amount, interval) -> None:
      self.product = product
      self.amount = amount
      self.interval = interval
      self.is_running = False
      self.thread = None
      self.holding = 0
      self.maxHolding = 10

   @staticmethod
   def load_data():
      with open('json_folder/running_gameObjects.json', 'r') as file:
         gameObjects_data = json.load(file)
      return gameObjects_data

   @staticmethod
   def update_data(gameObjects_data):
      with open('json_folder/running_gameObjects.json', 'w') as file:
         json.dump(gameObjects_data, file, indent=4)

   # Produce factory product at given rate until at max capacity
   #change to change the json file
   def produce(self):
      while self.is_running:
         time.sleep(self.interval)
         if self.holding < self.maxHolding:
            self.holding += self.amount
            print(f'{self.product} Factory {self.holding}/{self.maxHolding}: +{self.amount}')
         else:
            print(f"{self.product} Factory Full: {self.holding}/{self.maxHolding}")
            self.holding = self.maxHolding

   # Start producing
   def start_production(self):
      if not self.is_running:
         self.is_running = True
         self.thread = threading.Thread(target=self.produce)
         self.thread.start()

   # Stop producing
   def stop_production(self):
      if self.is_running:
         self.is_running = False
         if self.thread and self.thread.is_alive():
            self.thread.join()

   # Save factory data
   def save_data(self):
      gameObjects_data = self.load_data()
      # Update or add factory data
      # Assuming the factory is stored in the 'factories' section of the JSON
      gameObjects_data['inventories'][0]["inventory_factories"][f"{self.product} Factory"] = {
          "product": self.product,
          "amount": self.amount,
          "interval": self.interval,
          "is_running": self.is_running,
          "holding": self.holding,
          "maxHolding": self.maxHolding
      }
      self.update_data(gameObjects_data)