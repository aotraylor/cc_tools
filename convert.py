import cc_dat_utils
import example_data
import test_json_utils
import cc_data
import cc_json_utils
import json

#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
# cc_dat = cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")
# print(cc_dat)
#print the resulting data


#Part 2 Example
#Making the data structure manually
# myFam = example_data.Family()
# myFam.parent1 = "Dave"
# myFam.parent2 = "Sabrina"
#
# myKid = example_data.Kid()
# myKid.name = "Hazel"
# myKid.age = 4
# myFam.add_kid(myKid)
# print("Family made in code:")
# print(myFam)
# print("")

#Loading the data from a json file
# example_json_file = "data/example_json.json"
# with open(example_json_file, "r") as reader:
#     family_data = json.load(reader)
# print("JSON data:")
# print(family_data)
# print("")
#
# myFamFromJson = example_json_utils.make_family_from_json(family_data)
# print("Family loaded from JSON:")
# print(myFamFromJson)
#End Part 2 Example


#Part 2
# input_json_file = "data/test_data.json"
# with open(input_json_file, "r") as reader:
#     game_data = json.load(reader)
#
# print(game_data)
# testGameLibraryData = test_json_utils.make_game_library_from_json(game_data)
#
# print("Game list loaded from JSON:")
# print(testGameLibraryData)

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###


#Part 3
#Load your custom JSON file
with open("data/atraylor_cc1.json", "r") as reader:
    json_cc_data = json.load(reader)

# with open("data/atraylor_cc_levels.json", "r") as reader:
#     json_cc_data = json.load(reader)

#Convert JSON data to cc_data
cc_data_file = cc_json_utils.make_cc_data_file_from_json(json_cc_data)
print(json_cc_data)

#Save converted data to DAT file
cc_dat_utils.write_cc_data_to_dat(cc_data_file, "data/atraylor_cc_levels.dat")
dat_check = cc_dat_utils.make_cc_data_from_dat("data/atraylor_cc_levels.dat")
print(dat_check)




