play_again = True

def gameloop():
    print("Welcome to Valorant's gun shop")
    print("Types of guns:")
    print("Sidearm")
    print("SMGs")
    print("Rifles")
    print("Sniper")
    print("Shotgun")
    print("Heavy")
    x = input("Please select your weapon type: ")
    if x == 'Sidearm' or x == 'sidearm':
        print("Price:\tGun:")
        print("Free\tClassic")
        print("300\tShorty")
        print("450\tFrenzy")
        print("500\tBandit")
        print("500\tGhost")
        print("800\tSheriff")
    if x == 'SMGs' or x == 'smgs' or x == 'smgs':
        print("Price:\tGun:")
        print("1000\tStinger")
        print("1600\tSpectre")
    if x == 'Shotgun' or x == 'shotgun' or x == 'SHOTGUNS':
        print("Price:\tGun:")
        print("900\tBucky")
        print("1600\tJudge")
    if x == 'Rifles' or x == 'rifles' or x == 'rifle' or x == 'RIFLE' or x == 'RIFLES':
        print("Price:\tGun:")
        print("2050\tBulldog")
        print("2100\tGuardian")
        print("2900\tPhantom")
        print("2900\tVandal")
    if x == 'sniper' or x == 'snipers' or x == 'Sniper' or x == 'SNIPERS' or x == 'SNIPER' or x == 'Snipers':
        print("Price:\tGun:")
        print("1100\tMarshal")
        print("4700\tOperator")
    if x == 'Heavy' or x == 'heavy':
        print("Price:\tGun:")
        print("1600\tAres")
        print("3200\tOdin")

while play_again:
    gameloop()
    choice = input("Would you like to go back to the menu? ")
    if choice == 'yes' or choice == 'YES' or choice == 'Yes':
        pass
    if choice == 'no' or choice == 'NO' or choice == 'No':
        print("Thank you please come again!")
        play_again = False
        break
