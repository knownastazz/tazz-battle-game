import random

curFightData = {

    "Op_MaxHP" : 0,
    "Op_HP" : 0,
    "Op_DamageReduction" : 1,
    "Op_DodgeChance" : 0.05,
    "Op_DamageReflect" : 0,
    "Op_Abilities" : [],
    "Op_AbilityUses" : [],

    "Op_Drops" : [],

    "User_MaxHP" : 0,
    "User_HP" : 0,
    "User_DamageReduction" : 1,
    "User_DodgeChance" : 0.05,
    "User_DamageReflect" : 0,
    "User_Abilities" : [],
    "User_AbilityUses" : []

}

def clampywampy(val, minval, maxval):
    if val < minval: return minval
    if val > maxval: return maxval
    return val

def analyzeFightData(sfd, cfd, dodged):

    print("")

    if dodged:
        print("The attack was dodged.")

    if sfd["Op_HP"] > cfd["Op_HP"]:
        print("Your opponent took damage.")
    elif sfd["Op_HP"] < cfd["Op_HP"]:
        print("Your opponent gained health.")

    if sfd["User_HP"] > cfd["User_HP"]:
        print("You took damage.")
    elif sfd["User_HP"] < cfd["User_HP"]:
        print("You gained health.")

# defense

    if sfd["Op_DamageReduction"] > cfd["Op_DamageReduction"]:
        print("Your opponent's defense weakens.")
    elif sfd["Op_DamageReduction"] < cfd["Op_DamageReduction"]:
        print("Your opponent gained defense.")

    if sfd["User_DamageReduction"] > cfd["User_DamageReduction"]:
        print("Your defense weakens.")
    elif sfd["User_DamageReduction"] < cfd["User_DamageReduction"]:
        print("You gained defense.")

# dodge chance

    if sfd["Op_DodgeChance"] > cfd["Op_DodgeChance"]:
        print("Your opponent becomes slower.")
    elif sfd["Op_DodgeChance"] < cfd["Op_DodgeChance"]:
        print("Your opponent is quicker on thier feet!")

    if sfd["User_DodgeChance"] > cfd["User_DodgeChance"]:
        print("You become slower.")
    elif sfd["User_DodgeChance"] < cfd["User_DodgeChance"]:
        print("You are quicker on your feet!")

# damage reflection

    if sfd["Op_DamageReflect"] > cfd["Op_DamageReflect"]:
        print("Your opponent reflects less damage.")
    elif sfd["Op_DamageReflect"] < cfd["Op_DamageReflect"]:
        print("Your opponent reflects more damage.")

    if sfd["User_DamageReflect"] > cfd["User_DamageReflect"]:
        print("Your reflect less damage.")
    elif sfd["User_DamageReflect"] < cfd["User_DamageReflect"]:
        print("You reflect more damage.")

    print("")

    

def opponentDodged(victim_dodgechance):
    if random.randrange(0, 101, 2)  <= (victim_dodgechance * 100):
        return True
    return False

def applyDamageReduction(basedamage, reduction):
    return basedamage / reduction

def clampPlayerValues():
    
    cfd = curFightData
    aPref = "User"
    vPref = "Op"

    cfd[vPref + "_HP"] = (round(cfd[vPref + "_HP"] * 100)) / 100
    cfd[aPref + "_HP"] = (round(cfd[aPref + "_HP"] * 100)) / 100

    cfd[aPref + "_HP"] = clampywampy(cfd[aPref + "_HP"], 0, cfd[aPref + "_MaxHP"])
    cfd[vPref + "_HP"] = clampywampy(cfd[vPref + "_HP"], 0, cfd[vPref + "_MaxHP"])

    cfd[aPref + "_DodgeChance"] = clampywampy(cfd[aPref + "_DodgeChance"], 0, 0.50)
    cfd[vPref + "_DodgeChance"] = clampywampy(cfd[vPref + "_DodgeChance"], 0, 0.50)

    cfd[aPref + "_DamageReduction"] = clampywampy(cfd[aPref + "_DamageReduction"], 0.2, 1.85)
    cfd[vPref + "_DamageReduction"] = clampywampy(cfd[vPref + "_DamageReduction"], 0.2, 1.85)

    cfd[aPref + "_DamageReflect"] = clampywampy(cfd[aPref + "_DamageReflect"], 0, 0.75)
    cfd[vPref + "_DamageReflect"] = clampywampy(cfd[vPref + "_DamageReflect"], 0, 0.75)

def useMove(name, aPref, vPref):

    sfd = curFightData.copy()
    cfd = curFightData

    dodged = False

    if name == "Swing":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 30
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])

    elif name == "Stab":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 25
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[aPref + "_DamageReduction"] += 0.04

    elif name == "Bad Intentions":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 30
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[aPref + "_HP"] += 7

    elif name == "Emergency Tsunami":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 25
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[aPref + "_DamageReduction"] += 0.035

    elif name == "Bad Grades":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 35
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[vPref + "_DamageReduction"] -= 0.05

    elif name == "Lightsaber":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 40
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])

    elif name == "Dirt House":
        cfd[aPref + "_DamageReduction"] += 0.08

    elif name == "Roll":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 40
            if random.randrange(0, 101, 2) <= 33:
                print("CRITICAL HIT!")
                basedamage += 25
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])

    elif name == "Smack":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 50
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])

    elif name == "Ragequit":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 80
            if random.randrange(0, 101, 2) <= 50:
                cfd[aPref + "_HP"] -= 30
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])

    elif name == "Smash":
        cfd[aPref + "_Abilities"].remove("Smash")
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 100
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[vPref + "_DamageReduction"] -= 0.05

    elif name == "Bonk":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 60
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])

    elif name == "W Key":
        basedamage = 50
        cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])

    elif name == "Red Phosphorus":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 40
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[vPref + "_DodgeChance"] -= 0.035

    elif name == "Fulminate of Mercury":
        basedamage = 40
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[aPref + "_DamageReduction"] += 0.06
        cfd[aPref + "_HP"] -= applyDamageReduction(basedamage / 1.8, cfd[vPref + "_DamageReduction"])

    elif name == "Buzzcut":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 60
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])

    elif name == "BMW":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 45
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[aPref + "_HP"] += 15

    elif name == "Squabble":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            cfd[vPref + "_DodgeChance"] -= 0.04

    elif name == "Mag Dump":
        cfd[aPref + "_Abilities"].remove("Mag Dump")
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 135
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[vPref + "_DodgeChance"] -= 0.03

    elif name == "Reload":
        if not ("Mag Dump" in cfd[aPref + "_Abilities"]):
            cfd[aPref + "_Abilities"].insert(0, "Mag Dump")

    elif name == "Draco Whip":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 55
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])

    elif name == "Driveby":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 70
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[aPref + "_DamageReduction"] += 0.035

    elif name == "Scam":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            basedamage = 10
            cfd[vPref + "_HP"] -= applyDamageReduction(basedamage, cfd[vPref + "_DamageReduction"])
            cfd[aPref + "_DamageReduction"] += 0.06
            cfd[vPref + "_DamageReduction"] -= 0.06

    elif name == "Skrahhh":
        if opponentDodged(cfd[vPref + "_DodgeChance"]):
            dodged = True
        else:
            cfd[aPref + "_DodgeChance"] += 0.2

    if name == "Ramadan":
        cfd[aPref + "_DamageReduction"] += 0.06
        cfd[aPref + "_HP"] += 10

    elif name == "Kick Back":
        cfd[aPref + "_DamageReflect"] += 0.166

    elif name == "Death":
        basedamage = 5000000
        cfd[vPref + "_HP"] -= basedamage

    elif name == "Good Habits":
        cfd[aPref + "_HP"] += 20

    elif name == "Meditate":
        cfd[aPref + "_DodgeChance"] += 0.1

    elif name == "Thorns":
        cfd[aPref + "_DamageReflect"] += 0.1

    elif name == "Shield":
        cfd[aPref + "_DamageReduction"] += 0.15
        cfd[aPref + "_HP"] += 10

    elif name == "Detroit Spirit":
        cfd[aPref + "_HP"] += 5
        cfd[aPref + "_DamageReduction"] += 0.035
        cfd[aPref + "_DodgeChance"] += 0.025
        cfd[aPref + "_DamageReflect"] += 0.025

    elif name == "Chug Jug":
        cfd[aPref + "_HP"] += 65
        cfd[aPref + "_Abilities"].remove("Chug Jug")

    elif name == "Crystal Math":
        num = cfd[aPref + "_MaxHP"] - cfd[aPref + "_HP"] 
        cfd[aPref + "_HP"] += num * 0.12

    if cfd[vPref + "_DamageReflect"] > 0 and sfd[vPref + "_HP"] > cfd[vPref + "_HP"]:
        d2reflect = (sfd[vPref + "_HP"] - cfd[vPref + "_HP"]) * cfd[vPref + "_DamageReflect"]
        cfd[aPref + "_HP"] -= d2reflect

    clampPlayerValues()

    analyzeFightData(sfd, cfd, dodged)
    


            

        # [damage done (self),
#  percent health lost (self),
#  damage reduction % gained (self),
#  miss chance % gained

#  crit chance (enemy), 

#  damage done (enemy), 
#  percent health lost (enemy), 
#  damage reduction % gained (enemy)