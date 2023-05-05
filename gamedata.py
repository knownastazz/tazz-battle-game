
data = {
    "Enemies" : {
        "NAV" : { 
            "Abilities" : ["Bad Intentions", "Emergency Tsunami", "Good Habits", "Smack"],
            "Drops" : [
                ["Damage Potion", 0.25, "Consumables"],
                ["Health Potion", 0.25, "Consumables"],
                ["Damage Resistance Potion", 0.25, "Consumables"],
                ["Roti Roller", 1, "Weapons"],
                ["GOLDEN APPLE", 0.02, "Consumables"],
                ["Shield", 0.25, "Abilities"]
            ],
            "Health" : 150
        },

        "Mr. Simonsen" : {
            "Abilities" : ["Bad Grades", "Lightsaber", "Dirt House", "W Key"],
            "Drops" : [
                ["Damage Potion", 0.5, "Consumables"],
                ["Health Potion", 0.5, "Consumables"],
                ["Damage Resistance Potion", 0.5, "Consumables"],
                ["GOLDEN APPLE", 0.06, "Consumables"],
                ["Keyboard", 1, "Weapons"],
                ["Thorns", 0.25, "Abilities"]
            ],
            "Health" : 250
        },

        "Walter White" : { 
            "Abilities" : ["Red Phosphorus", "Fulminate of Mercury", "Crystal Math", "Smash"],
            "Drops" : [
                ["Damage Potion", 0.75, "Consumables"],
                ["Health Potion", 0.75, "Consumables"],
                ["Damage Resistance Potion", 0.75, "Consumables"],
                ["GOLDEN APPLE", 0.1, "Consumables"],
                ["Boiling Flask", 1, "Weapons"],
                ["Chug Jug", 0.25, "Abilities"]   
            ],
            "Health" : 335
        },

        "BabyTron" : { 
            "Abilities" : ["Driveby", "Skrahhh", "Kick Back", "Scam"],
            "Drops" : [
                ["Damage Potion", 0.8, "Consumables"],
                ["Health Potion", 0.8, "Consumables"],
                ["Damage Resistance Potion", 0.8, "Consumables"],
                ["GOLDEN APPLE", 0.13, "Consumables"],
                ["Draco", 1, "Weapons"],
                ["Detroit Spirit", 0.25, "Abilities"]   
            ],
            "Health" : 315
        },
      
        "Tazz" : { 
            "Abilities" : ["Buzzcut", "BMW", "Ramadan", "Squabble", "Meditate"],
            "Health" : 750,
            "Drops" : [
            ]
        }
    },

    "Items" : {
        "Weapons" : {
            "Sword" : {
                "Abilities" : ["Swing", "Stab"],
                "Description" : "The basic sword. Swing at enemy, kill enemy.",
                "LVL" : 1
            },
            "Roti Roller" : {
                "Abilities" : ["Roll", "Smack"],
                "Description" : "This was the first thing nav could grab out of his pantry to fight you with.",
                "LVL" : 2
            },
            "Keyboard" : {
                "Abilities" : ["Ragequit", "W Key"],
                "Description" : "Mr. Simonsen's secret weapon.",
                "LVL" : 3
            },
            "Boiling Flask" : {
                "Abilities" : ["Smash", "Bonk"],
                "Description" : "The secret weapon of Walter White.",
                "LVL" : 4
            },
            "Dev Sword" : {
                "Abilities" : ["Death"],
                "Description" : "you werent supposed to have this.",
                "LVL" : 999
            },
            "Draco" : {
                "Abilities" : ["Mag Dump", "Reload", "Draco Whip"],
                "Description" : "The necessary tool for the job in the streets of detroit",
                "LVL" : 5
            }
        }
    },

    "Abilities" : {

        "Swing" : {
            "Description" : "Does a rather small amount of damage.",
            "LVL" : "1"
        },
        "Stab" : {
            "Description" : "Does a small amount of damage. Gives damage reduction.",
            "LVL" : "1"
        },
        "Meditate" : {
            "Description" : "Channel your inner monk to dodge enemy attacks more often.",
            "LVL" : "1"
        },
        "Shield" : {
            "Description" : "Player gains 15 percent damage reduction, and a small health bonus",
            "LVL" : "2"
        },
        "Thorns" : {
            "Description" : "Player gains 6 percent damage reflection.",
            "LVL" : "3"
        },
        "Roll" : {
            "Description" : "Rolls the enemy out. Can critical hit for a serious amount of damage.",
            "LVL" : "3"
        },
        "Smack" : {
            "Description" : "Give'm the good ol' smack!",
            "LVL" : "2" 
        },
        "Death" : {
            "Description" : "Ouch!",
            "LVL" : "999"
        },
        "Ragequit" : {
            "Description" : "Sometimes raging can be bad for you. Be careful!",
            "LVL" : "3"
        },
        "W Key" : {
            "Description" : "Nobody can stop you when you W Key. Unblockable",
            "LVL" : "4"
        },
        "Smash" : {
            "Description" : "Does an immense amount of harm. But be careful, Smash can only be used once.",
            "LVL" : "6"
        },
        "Chug Jug" : {
            "Description" : "You need a lot of health instantly? Ok! (One time use)",
            "LVL" : "6"
        },
        "Bonk" : {
            "Description" : "Getting bonked on the head with a flask is... well... unpleasant",
            "LVL" : "5"
        },
        "Mag Dump" : { 
            "Description" : "Dump a mag on the opposition",
            "LVL" : "6"
        },
        "Reload" : {
            "Description" : "Lets u dump some more rounds from the draco",
            "LVL" : "1"
        },
        "Draco Whip" : {
            "Description" : "Not a fan of reloading? Need to finish the job? This is the perfect ability for you!",
            "LVL" : "4"
        },
        "Detroit Spirit" : {
            "Description" : "Embrace the michigan lifestyle. Increases all of your stats slightly.",
            "LVL" : "5"
        }
    }
}
