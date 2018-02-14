import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    # Loop through the json_data
    for gameList_data in json_data:

        #Create a new Game object
        game = test_data.Game()
        game.title = gameList_data["title"]
        game.year = gameList_data["year"]

        # making the platform object in game
        game.platform = test_data.Platform()

        #setting gamePlatform as an object to hold year and name
        gamePlatform = gameList_data["platform"];

        #attributes of the object platform
        game.platform.launch_year = gamePlatform["launch year"]
        game.platform.name = gamePlatform["name"]

        #Add that Game object to the game_library
        game_library.add_game(game)



        #  title
        #  year
        #  platform (which requires reading name and launch_year)

    #Return the completed game_library

    return game_library
