import atexit
import json
import time
from json_folder.reset_objects import replace_json_content  
from player import Player
from store import Store
from factory import Factory

#json var
gameObjectsPath = 'json_folder/gameObjects.json'
runningGameObjectsPath = 'json_folder/running_gameObjects.json'

#blank running is now fill game
def load_data():
    replace_json_content(runningGameObjectsPath, gameObjectsPath)

load_data()
# Open json files
with open(runningGameObjectsPath, 'r') as file:
    gameObjects_data = json.load(file)

# json shortcuts
inventories = gameObjects_data['inventories']
achievements = gameObjects_data['achievements']
store_factories = gameObjects_data['store_factories']

player = Player()
store = Store()

#used to pass factory data using name
"""
Make it go through json, find the name, pass any relevant info
"""
def newFactoryData(factoryName):
    new_Data = {"name": str(factoryName)}
    return new_Data

def welcome():
    print("Welcome to ***NAME COMING SOON***")  #change term *product* in code so it makes more sense i when add crafting
    #ADD ALL LAST PART 
    print("Your goal is to buy factories, collect it's materials, (COMING SOON) craft ready products, and sell to the public")
    #
    print("To get you going, here's a gift from us!")
    factory_data = newFactoryData("Wood Factory")
    player.new_factory("Wood Factory")

#save data, add manuel
def save_data():
    replace_json_content(gameObjectsPath, runningGameObjectsPath)

#change game to runnning, clear json file
def clean_up():
    save_data()

    with open(runningGameObjectsPath, 'w') as file:
        json.dump({}, file)

def main():
    if gameObjects_data["stages"][0]["welcome"] == "False":
        welcome()
        gameObjects_data["stages"][0]["welcome"] = "True"
        
        with open('json_folder/gameObjects.json', 'w') as file:
            json.dump(gameObjects_data, file, indent=4)
    #change factory
    wood_factory = Factory("Wood", 2, 5)
    wood_factory.start_production()
    time.sleep(5)
    wood_factory.save_data()
    player.collect("Wood Factory")
    
if __name__ == "__main__":
    atexit.register(clean_up)
    load_data()
    main()