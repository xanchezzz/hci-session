x, y = 0, 0
news = "N", "E", "W", "S", "n", "e", "w", "s"
direction = ""
while True:
    print("Option:")
    print("[1] Location ")
    print("[2] Move ")
    print("[3] Reset ")
    print("[4] Exit ")
    choice = int(input("Enter your choice "))
    if choice == 1:
        print("Robby is currently at", x, y)
    elif choice == 2:
        while direction not in news:
            direction = input("Enter direction (N, E, W , S)")
        while distance <= 0:
            distance = float(input("Enter distance>>"))
        if direction == "N":
            y+= distance
        elif direction == "E":
            x += distance
        elif direction == "W":
            x -= direction
        elif direction == "S":
            y -= direction
        print(f"Robby moved {direction}, {distance}, units")
    elif choice == 3:
        x=y=0
        print(f"Robby reset at ({x},{y})")
    else:
        break
    print("Goodbye")