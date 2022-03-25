# Version 1 / Flower mini game
day = 1
prc_growth = 0 #percent of growth
seed_planted = False
count = 0
flower_pot = [
    '''
  _ _ _ _ _
  \ _ _ _ /
   |     |
   | _ _ |

    ''',
    '''
  _ _ . _ _
  \ _ _ _ /
   |     |
   | _ _ |

    ''',
    '''
  *  . _|_
   _|_  |  *
    | .
  _ _ _ _ _
  \ _ _ _ /
   |     |
   | _ _ |

    ''',
    '''
 .  ` ^    .
  _ _/_\_*_
  \ _ _ _ /
   |     |
   | _ _ |

    ''',
    '''
    . ^ " 
 *   / \ .
  _`_\_/_ _*
  \ _ _ _ /
   |     |
   | _ _ |

    ''',
    '''
`     ^ . 
  .  / \   *
 •  /   \   `
    \ _ / .
 *_ _|_|_ _  •
  \ _ _ _ /
   |     |
   | _ _ |

    ''',
    '''
   "  ^    .
.    / \       •`
    /   \ .   
 • |     |    *
    \ _ /   | 
 `   | |/| - - 
* _ _|_/_|_ |
  \ _ _ _ /
   |     |
   | _ _ |

    ''',
    '''
   *        .
• .   ^ ` .   |  
  |\ / \ /|  -•- 
  |       |   |
 | \_ _ _/       .
- -  | |   *
 |   | |/|  
* _ _|_/_|_  "
  \ _ _ _ /
   |     |
   | _ _ |
    '''
    ]
print("~Welcome to Flower Mini Game!\n\n~To start the game, you have to plant a seed. :)")
print(flower_pot[0])
seed = input("~Do you want to plant the seed? \n(yes/no): ")
if seed == "no":
    exit(0)
elif seed == "yes":
    count += 1
    water = input("~Do you want to water the seed? \n(yes/no): ")
    being_nice = input("~Do you want to say nice things to the seed? \n(yes/no): ")
    if water and being_nice == "yes":
        prc_growth = 100
        watered = True
    if water and being_nice == "no":
        watered = False
        prc_growth = 0
    else:
        prc_growth += 50
    day += 1
while count < len(flower_pot):
    print("[ Day  " + str(day) + " ]")
    print(flower_pot[count])
    if count < 7:
        day += 1
        water = input("~Do you want to water the plant? \n(yes/no): ")
        being_nice = input("~Do you want to say nice things to the plant? \n(yes/no): ")
        if water == "yes":
            prc_growth += 50
        if being_nice== "yes":
            prc_growth += 50
        if water == "no":
            prc_growth += 0
        if being_nice == "no":
            prc_growth += 0
        else:
            prc_growth += 50
        if (prc_growth >= 100):
            count += 1
            prc_growth = 0
        elif (prc_growth <= 100):
            continue
    else:
        exit(0)
