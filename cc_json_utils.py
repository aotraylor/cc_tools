import cc_data

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_cc_data_file_from_json(json_data):
    cc_data_file = cc_data.CCDataFile()
    for json_level in json_data:
        cc_level = cc_data.CCLevel()
        cc_level.level_number = json_level["level_number"]
        cc_level.num_chips = json_level["num_chips"]
        cc_level.time = json_level["time"]
        cc_level.upper_layer = json_level["upper_layer"]
        cc_level.lower_layer = json_level["lower_layer"]

        json_fields = json_level["optional_fields"]
        for json_field in json_fields:
            field_type = json_field["type"]
            if (field_type == "title"):

                title = json_field["title"]
                cc_title_field = cc_data.CCMapTitleField(title)
                cc_level.add_field(cc_title_field)
            elif (field_type == "hint"):

                hint = json_field["hint"]
                cc_hint_field = cc_data.CCMapHintField(hint)
                cc_level.add_field(cc_hint_field)
            elif (field_type == "password"):

                password = json_field["password"]
                cc_password_field = cc_data.CCEncodedPasswordField(password)
                cc_level.add_field(cc_password_field)
            elif (field_type == "monster"):

                monster = json_field["monster"]
                #making a list for the monster positions using CCCoordinate
                monster_positions = []
                # loop through the values in the json monster list
                for point in monster:
                    # make cccoordinates
                    cc_monster_coord_field = cc_data.CCCoordinate(point[0], point[1])
                    # put coordinates into the list for the positions
                    monster_positions.append(cc_monster_coord_field)
                print(len(monster_positions))

                cc_monster_field = cc_data.CCMonsterMovementField(monster_positions)
                cc_level.add_field(cc_monster_field)

            else:
                print("I dont know")
            print(field_type)
        print(cc_level)
        cc_data_file.add_level(cc_level)

    return cc_data_file
