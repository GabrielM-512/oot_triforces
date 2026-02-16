data = {'total': 484, 'BotW': [1, ['BotW', 1]], 'CS': [9, ['CS', 1], ['CS', 1], ['CS', 1], ['CS', 1], ['CS', 1], ['CS', 1], ['CS', 3]], 'Colossus': [1, ['Colossus', 1]], 'Courtyard': [11, ['Courtyard', 1], ['Courtyard', 1], ['Courtyard', 6], ['Courtyard', 3]], 'DMC': [1, ['DMC', 1]], 'Forest Temple': [7, ['Forest Temple', 7]], 'Ganon Fight': [1, ['Ganon Fight', 1]], 'Ganons Castle': [189, ['Ganons Castle', 48], ['Ganons Castle', 112], ['Ganons Castle', 1], ['Ganons Castle', 28]], 'Goron City': [18, ['Goron City', 18]], 'Graveyard': [20, ['Graveyard', 17], ['Graveyard', 1], ['Graveyard', 1], ['Graveyard', 1]], 'Great Fairy Fountains': [6, ['Great Fairy Fountains', 6]], 'Guards Section': [56, ['Guards Section', 54], ['Guards Section', 1], ['Guards Section', 1]], 'Hyrule Castle': [71, ['Hyrule Castle', 70], ['Hyrule Castle', 1]], 'Hyrule Field': [1, ['Hyrule Field', 1]], 'Item': [8, ['Item', 1], ['Item', 1], ['Item', 6]], 'Kakariko': [21, ['Kakariko', 21]], 'Lake Hylia': [2, ['Lake Hylia', 1], ['Lake Hylia', 1]], "Lots o' Pots": [9, ["Lots o' Pots", 7], ["Lots o' Pots", 1], ["Lots o' Pots", 1]], 'Market': [22, ['Market', 14], ['Market', 7], ['Market', 1]], 'Market Entrance': [7, ['Market Entrance', 7]], 'Miscellaneous': [1, ['Miscellaneous', 1]], 'NPC': [10, ['NPC', 1], ['NPC', 1], ['NPC', 1], ['NPC', 1], ['NPC', 2], ['NPC', 2], ['NPC', 2]], 'Royal Family Tomb': [1, ['Royal Family Tomb', 1]], 'SFM': [1, ['SFM', 1]], 'Shadow Temple': [1, ['Shadow Temple', 1]], 'Spirit Temple': [2, ['Spirit Temple', 1], ['Spirit Temple', 1]], 'Temple of Time': [4, ['Temple of Time', 1], ['Temple of Time', 1], ['Temple of Time', 1], ['Temple of Time', 1]], 'Water Temple': [3, ['Water Temple', 3]]}
max_scene_name_length = 0

help_prompt = ("This tool lets you explore which scene contains how many Triforces in 'The Legend of Zelda: Ocarina of Time'.\n"
               "To do so, simply type the scene's name as listed above (or using the 'list' command).\n"
               "To create this, I went through the game and counted the Triforces. I did this on the PC Port 'Ship of Harkinian' with a resolution of 2160p, so don't be surprised if you can't spot them on original hardware.\n"
               "I only counted something as a Triforce if it was explicitly one. Colours don't matter, but it should look like it was meant to be a Triforce (so this includes Rauru's Forehead).\n"
               "I also didn't count the number of Triforce textures in the game files, but the number of Triforces that are logically distinct in the game. For example, this means that the Triforce above ToT entrance from ToT and Market scenes count as 1, but each guard counts a separate 7.\n"
               "This is somewhat arbitrary, but it's what I decided on.\n"
               "If I were to bet on whether this list is complete, I would easily bet 100€ on no, so don't assume it is. However, I didn't find a better count, so take it or leave it.\n"
               "If you find a Triforce that isn't included here or have another question, DM me on Discord (Grootmaster47) or create an Issue on the github page (https://github.com/GabrielM-512/oot_triforces/issues)\n\n"
               ""
               "Commands:\n"
               "'help': Brings up this text\n"
               "'list': Brings up a list of Scenes and their respective Triforce Counts\n"
               "'exit' or 'end': Exits the program\n"
               "'sorted': Sorts the previous input's list by Triforce count (input 'list' beforehand to get global sorted)\n"
               "'total': Displays the total number of Triforces")

def main():
    global max_scene_name_length, data
    for scene in data.keys():
        if len(scene) > max_scene_name_length:
            max_scene_name_length = len(scene)

    print("Total: " + str(data['total']) + " Triforces\n")

    print_global()

    print("'help' for help, 'exit' or 'end' to exit, 'list' for list of scenes.\n"
          "[Scenename] for list of locations in scene.\n")

    previous = "global"

    while True:
        next = input("> ")

        if next == "exit" or next == "end":
            break

        if next == "help":
            print(help_prompt)
            continue

        if next == "total":
            print(str(data['total']) + " Triforces")
            continue

        if next == "list":
            print_global()
            previous = 'global'
            continue

        if next == "sorted":
            print_sorted(previous)
            continue

        try:
            print_scene(data[next])
            previous = next
        except KeyError:
            print("Unknown scene or command: '" + next + "'")

def print_global():
    for scene in data.keys():
        if scene == "total":
            continue

        scenedata = data[scene]

        output = scene + ":"

        # adjust for length of scene name
        for i in range(max_scene_name_length - len(scene)):
            output += " "

        output += " "

        # adjust for length of number
        for i in range(3 - len(str(scenedata[0]))):
            output += " "

        output += str(scenedata[0])

        print(" " + output)

    print()

def print_sorted(scene: str):
    try:
        if scene == "global":
            scenedata: dict = data.copy()
            scenedata.pop("total")

            overwrite = []

            for i in scenedata.keys():
                current = scenedata[i]
                overwrite.append([i, current[0]])

            scenedata: list = overwrite

        else:
            scenedata: list[list] = data[scene].copy()
            scenedata.pop(0)


        for i in range(len(scenedata)):
            for j in range(0, len(scenedata) - i - 1):
                if scenedata[j][1] > scenedata[j + 1][1]:
                    scenedata[j], scenedata[j + 1] = scenedata[j + 1], scenedata[j]

        for i in range(len(scenedata)):
            print(" " + str(scenedata[i][0]) + ": " + str(scenedata[i][1]))

    except Exception as e:
        print("Error while sorting " + scene + ": " + str(e))

def print_scene(scene: list):
    print("Total: " + str(scene[0]) + " Triforces\n")
    for place in range(1, len(scene)):
        print("\t" + scene[place][0] + ": " + str(scene[place][1]))

if __name__ == "__main__":
    main()