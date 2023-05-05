print("Welcome to the game TAZZ FIGHTING SIMULATOR. In this game, you will breach all of tazz's bodyguards, and break through their rooms to eventually fight the renown tazz.")
gaming = True

import playerdata
import gamedata
import fightHandle
import random
import os
import glob

while gaming:

    def Inventory():

        done = False
        while done == False:

            print("")
            print("-------- Inventory --------")
            print("- 0: Exit inventory")
            print("------- Weapons -------")

            items = []
            weaponmax = 0

            weapon = playerdata.data["weapon"]
            ability = playerdata.data["ability"]

            for index, key in enumerate(playerdata.data["Weapons"]):
                if (gamedata.data["Items"]["Weapons"][key]):

                    suffix = ""

                    if (weapon == key):
                        suffix = " (Equipped)"
                    print("- " + str(len(items) + 1) + ": " + "(LVL " + str(gamedata.data["Items"]["Weapons"][key]["LVL"]) + ") " + key + suffix + " - " + gamedata.data["Items"]["Weapons"][key]["Description"])
                    items.append(key)
                    weaponmax = len(items)

            print("------- Abilities -------")
                
            for index, key in enumerate(playerdata.data["Abilities"]):
                if (gamedata.data["Abilities"][key]):

                    suffix = ""
                    ability = playerdata.data["ability"]
                    
                    if (ability == key):
                        suffix = " (Equipped)"
                    print("- " + str(len(items) + 1) + ": " + "(LVL " + str(gamedata.data["Abilities"][key]["LVL"]) + ") " + key + suffix + " - " + gamedata.data["Abilities"][key]["Description"])
                    items.append(key)


            print("------- Consumables -------")

            for index, key in enumerate(playerdata.data["Consumables"]):
                if (key[1] != 0):
                    print(str(key[0]) + " (" + str(key[1]) + "x) " )

            print("-----------------------")

            action = input("Choose your action.")
            if action.isdigit() and int(action) <= len(items):

                stype = "Wep"
                if int(action) > weaponmax:
                    stype = "Abil"

                selected = items[int(action) - 1]

                if int(action) == 0:
                    done = True
                    break

                if (stype == "Wep"):
                    if selected == weapon:
                        print("")
                        print("Weapon already equipped. Retry")
                    else:
                        playerdata.data["weapon"] = selected
                        print("")
                        print("Equipped " + selected)
                else:
                    if selected == ability:
                        print("")
                        print("Ability already equipped. Retry")
                    else:
                        playerdata.data["ability"] = selected
                        print("Equipped " + selected)
            else:
                print("")
                print("Invalid input. Reselect.")

    def potionMenu():
        potionamount = 0
        potionchoosing = True
        while potionchoosing:

            potionlist = []

            print("---------- Choose a potion to use ----------")
            print("- 0: Exit potion menu.")
            print("-------------------")
            for index, key in enumerate(playerdata.data["Consumables"]):
                if (key[1] != 0):
                    potionamount += 1
                    print("- " + str(potionamount) + ": " + str(key[0]) + " (" + str(key[1]) + "x) " )     
                    potionlist.append(key)
            if potionamount == 0:
                print("You have no potions :( good luck!!")
            print("--------------------------------------------")
            action = input("Choose your action.")
            if (int(action) and int(action) <= len(potionlist)) or (action == "0"):
                if action != "0":
                    ptype = potionlist[int(action) - 1][0]
                    print("You used a " + ptype)
                    potionlist[int(action) - 1][1] -= 1
                    if ptype == "Health Potion":
                        fightHandle.curFightData["User_HP"] += 30
                    elif ptype == "Damage Potion":
                        fightHandle.curFightData["Op_HP"] -= 25
                    elif ptype == "Damage Resistance Potion":
                        fightHandle.curFightData["User_DamageReduction"] += 0.1
                    elif ptype == "GOLDEN APPLE":
                        fightHandle.curFightData["User_DamageReduction"] += 0.35
                        fightHandle.curFightData["User_HP"] += 50

                    fightHandle.clampPlayerValues()

                potionchoosing = False
            else:
                print("Invalid input. Reselect.")

    def FightSys(opnum):

        global gaming

        num2opponent = ["", "NAV", "Mr. Simonsen", "Walter White", "BabyTron", "Tazz"]
        stats = gamedata.data["Enemies"][num2opponent[opnum]]

        cfd = fightHandle.curFightData

        cfd["Op_DamageReduction"] = 1
        cfd["User_DamageReflect"] = 0
        cfd["Op_DodgeChance"] = 0.05
        cfd["Op_Abilities"] = []
        cfd["Op_Drops"] = []

        cfd["User_Abilities"].clear()
        cfd["Op_Abilities"].clear()
        cfd["Op_Drops"].clear()

        cfd["User_HP"] = 150
        cfd["User_MaxHP"] = 150
        cfd["User_DamageReflect"] = 0
        cfd["User_Abilities"] = gamedata.data["Items"]["Weapons"][playerdata.data["weapon"]]["Abilities"].copy()
        cfd["User_Abilities"].append(playerdata.data["ability"])
        cfd["User_DamageReduction"] = 1
        cfd["User_DodgeChance"] = 0.05

        cfd["Op_HP"] = stats["Health"]
        cfd["Op_MaxHP"] = cfd["Op_HP"]
        cfd["Op_Abilities"] = stats["Abilities"]
        cfd["Op_Drops"] = stats["Drops"]

        if opnum == 1:
            print(" NAV - ♫ Your whip is a toilet, you're lookin' like poop in it. ♫")
            input("Type anything to continue")
            print("")
            print(" NAV - What do you think you are doing challenging me? im literally the supreme musical artist.")
            input("Type anything to continue")
            print("")
            print(" NAV - Get ready to fight the musical master.")
            input("Type anything to continue")

        if opnum == 2:
            print(" Mr. Simonsen - Hello friend. You think you could beat me in my own language??")
            input("Type anything to continue")
            print("")
            print(" Mr. Simonsen - I'm sorry to say, but i've got something different for our lesson plans today.")
            input("Type anything to continue")

        if opnum == 3:
            print(" Walter White - Prepare to be beat so hard you wont know which way is up.")
            input("Type anything to continue")

        if opnum == 4:
            print(" BabyTron - ♫ Birds of a feather flock together gang in goose coats ♫")
            input("Type anything to continue")
            print("")
            print(" BabyTron - ♫ I was lil' dog now my pape' like Manute Bol ♫")
            input("Type anything to continue")
            print("")
            print(" BabyTron - ♫ 10K a day, all blues, this a new roll ♫")
            input("Type anything to continue")
            print("")

        if opnum == 5:
            print(" Tazz - this is gonna be ez.")
            input("Type anything to continue")

        gdataabilities = gamedata.data["Abilities"]

        wep = playerdata.data["weapon"]
        turn = 0

        while (cfd["User_HP"] > 0 and cfd["Op_HP"] > 0):
            if turn == 0:
                choosingmove = True
                while choosingmove:
                    print("")
                    print("-- Your HP: " + str(cfd["User_HP"]) + " -- Enemy HP: " + str(cfd["Op_HP"]) + " --")
                    for index, key in enumerate(cfd["User_Abilities"]):
                        print("- " + str(index) + ": " + key + " - " + gamedata.data["Abilities"][key]["Description"])
                    print("--------------------------")
                    choice = input("Choose your move.")
                    if choice.isdigit() and int(choice) < len(cfd["User_Abilities"]):
                        print("You chose " + cfd["User_Abilities"][int(choice)])
                        fightHandle.useMove(cfd["User_Abilities"][int(choice)], "User", "Op")
                        choosingmove = False
                        input("Press enter to continue.")
                        turn = 1
                    else:
                        print("Invalid input. Reselect.")

            else:
                print("Opponent's turn.")
                print("")  
                opchoice = random.choice(list(cfd["Op_Abilities"]))
                print("--------------------------")
                print("Your opponent uses " + opchoice + ".")
                print("--------------------------")
                fightHandle.useMove(opchoice, "Op", "User")
                if (cfd["User_HP"] > 0 and cfd["Op_HP"] > 0):
                    pinput = input("Press enter to continue, or type P to use a potion.")
                    if pinput == "P":
                        potionMenu()
                turn = 0

        print("--------------------------") 
        print("- Your HP: " + str(cfd["User_HP"]) + " | Enemy HP: " + str(cfd["Op_HP"]) + " -")
        if cfd["User_HP"] <= 0:
            if cfd["Op_HP"] > 0:
                print("- YOU LOSE! Returning to menu.")
                if opnum == 1:
                    print(" NAV - I told you. Dont run up on me like that again blud.")
                elif opnum == 2:
                    print(" Mr. Simonsen - I hope you learned your lesson!")
                elif opnum == 3:
                    print(" Walter White - Get Cooked!")
                elif opnum == 4:
                    print(" BabyTron - dont try none of that goofy every again lil dog.")
                elif opnum == 5:
                    print(" Tazz - Maybe bring golden apples next time.")
            else:
                print("- ITS A TIE! Returning to menu.")
        else:

            print("--------------------------") 
            print("- YOU WIN! " + num2opponent[opnum] + " dropped the following: ")
            print("--------------------------") 

            for index, key in enumerate(cfd["Op_Drops"]):
                randnum = random.randrange(0, 101, 2)
                name = key[0]
                chance = key[1]
                invtype = key[2]
                if (randnum < chance * 100):
                    canpass = True
                    if (invtype == "Weapons" or invtype == "Abilities"):
                        if key[0] in playerdata.data[invtype]:
                            canpass = False
                    if canpass:
                        print("- " + name)
                        if (invtype != "Consumables"):
                            playerdata.data[invtype].append(name)
                        else:
                            for index2, key2 in enumerate(playerdata.data["Consumables"]):
                                if key2[0] == name:
                                    key2[1] += 1    
            print("--------------------------")

            if opnum == 1:
                print(" NAV - Back to music i guess...")
                playerdata.data["Rooms Beat"][0] = True
            elif opnum == 2:
                print(" Mr. Simonsen - This wasn't apart of the lesson plans!")
                playerdata.data["Rooms Beat"][1] = True
            elif opnum == 3:
                print(" Walter White - I did not calculate for this.")
                playerdata.data["Rooms Beat"][2] = True
            elif opnum == 4:
                print(" BabyTron - good job jit.")
                playerdata.data["Rooms Beat"][3] = True
            elif opnum == 5:
                print(" Tazz - You have defeated me. I am no longer the best. Congratulations")
                print("-----------------------------------------------------------------")
                print("GAME OVER. YOU WIN. Play again, and try to collect all the items!")
                print("-----------------------------------------------------------------")
                playerdata.data["Rooms Beat"][4] = True 
                gaming = False

    def saveGame(name):

        filename = name + ".tazz"

        f = open(filename, "w")
        for key in playerdata.data:
            f.write(key + " - " + str(playerdata.data[key]) + "\n")

        print("Success! Thanks for playing!")
        gaming = False
        exit()



    def loadGame():
        choosingsave = True
        while choosingsave:
            print("--- Please choose a save to load. ---")
            saves = glob.glob("*.tazz")
            for index, key in enumerate(saves):
                print("- " + str(index) + ": " + str(key))
            print("-------------------------------------")
            action = input("Choose your action.")
            if (int(action) or action == "0") and int(action) >= 0 and int(action) < len(saves):
                print("Loading " + str(saves[int(action)]))
                choosingsave = False

                file = saves[int(action)]
                f = open(file, "r")
                lines = f.readlines()
                #lines = [line.strip() for line in f]

                worked = True
                for index, key in enumerate(lines):
                    data = key.strip().split(' - ')
                    if len(data) == 2:

                        pd_key = data[0]
                        pd_val = data[1]

                        try:
                            playerdata.data[pd_key] = eval(pd_val)
                        except:
                            playerdata.data[pd_key] = pd_val
                            
                    else:
                        print("Save file corrupt. Sorry :/")
                        worked = False

                if worked == True:
                    print("Save loaded successfully!")

            else:
                print("Bad input. Retry")

    def GameMenu():

        selecting = True
        while selecting:
            print("")
            print("-------- Choose your action --------")
            print("- 1: Challenge room 1. (NAV)")
            print("- 2: Challenge room 2. (Mr. Simonsen)")
            print("- 3: Challenge room 3. (Walter White)")
            print("- 4: Challenge room 4. (BabyTron)")
            print("- 5: Challenge THE FINAL ROOM. (Tazz)")
            print("---------------")
            print("- 6: Open inventory")
            print("- 7: Load game data.")
            print("- 8: Save, and quit.")
            print("------------------------------------")
            action = input("Choose your action.")
            if action.isdigit() and len(action) == 1 and int(action) <= 8 and int(action) != 0:
                print("")
                print("You chose " + action)
                print("")
                selecting = False
                if action == "6":
                    Inventory()
                if (int(action) >= 1 and int(action) <= 5):
                    if action == "1" or playerdata.data["Rooms Beat"][int(action) - 2] == True:
                        FightSys(int(action));
                    else:
                        print("Beat the previous rooms before going into this one")
                if action == "7":
                    loadGame()
                if action == "8":
                    name = input("What is the name of your save file? (Type 0 to cancel)")
                    if name != "0":
                        saveGame(name)
            else:
                print("")
                print("Invalid input. Reselect.")

    GameMenu()