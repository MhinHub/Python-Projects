for raw in range(7):
    for col in range(5):
        if (raw in {0,3}):
            print("F", end=" ")
        elif (raw in {1,2,4,5,6}) and (col == 0):
            print("F", end=" ")
        else:
            print(" ", end=" ")
    print()