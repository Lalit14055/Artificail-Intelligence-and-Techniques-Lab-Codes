# Water Jug Problem: Jug A = 4L, Jug B = 3L, Goal = 2L in Jug A

jugA = 0  
jugB = 0  

goal = 2

print(f"Start: ({jugA}, {jugB})")

while True:
    
    if jugA == goal:
        print("Goal reached: ({jugA}, {jugB})")
        break

    if jugA == 0:
        jugA = 4
        print("Fill Jug A: ({jugA}, {jugB})")

    elif jugB < 3:
        pour = min(jugA, 3 - jugB)
        jugA -= pour
        jugB += pour
        print("Pour from A to B: ({jugA}, {jugB})")

    elif jugB == 3:
        jugB = 0
        print("Empty Jug B: ({jugA}, {jugB})")
