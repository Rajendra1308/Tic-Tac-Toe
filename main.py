def printBoard(xList, yList):
    zero = 'X' if xList[0] else ('O' if yList[0] else 0)
    one = 'X' if xList[1] else ('O' if yList[1] else 1)
    two = 'X' if xList[2] else ('O' if yList[2] else 2)
    three = 'X' if xList[3] else ('O' if yList[3] else 3)
    four = 'X' if xList[4] else ('O' if yList[4] else 4)
    five = 'X' if xList[5] else ('O' if yList[5] else 5)
    six = 'X' if xList[6] else ('O' if yList[6] else 6)
    seven = 'X' if xList[7] else ('O' if yList[7] else 7)
    eight = 'X' if xList[8] else ('O' if yList[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("--|---|---")
    print(f"{three} | {four} | {five}")
    print("--|---|---")
    print(f"{six} | {seven} | {eight}")


def win(xList, yList):
    possiblities = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [2, 5, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7]]
    g_x = 0
    g_y = 0
    for list in possiblities:
        count_x = 0
        for num in list:
            if x_list[num] == 1:
                count_x += 1
                g_x += 1
        if count_x == 3:
            return 24  # X is 24
        count_y = 0
        for num in list:
            if y_list[num] == 1:
                count_y += 1
                g_y += 1

        if count_y == 3:
            return 25  # Y is 25
    # if  len(xList) == 9 and len(yList) == 9:
    #     return 10  # 10 is forced end
    return 15 # game still on


print("Welcome to Tic Tac Toe")

x_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
y_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1  # 1 for X and 0 for O
# print("X's chance")

'''
Board
        0|1|2
        -----
        3|4|5
        -----
        6|7|8
'''
counter=0
while True:
    counter+=1
    if turn == 1:
        printBoard(x_list, y_list)
        print("X's Chance")
        value = int(input("Enter Choice: "))
        if y_list[value] != 1:
            x_list[value] = 1
            turn = 1 - turn

        else:
            # printBoard()
            print("Enter a new value:")
            turn = 1

    else:
        printBoard(x_list, y_list)
        print("0's Chance")
        value = int(input("Enter Choice: "))
        if x_list[value] != 1:
            y_list[value] = 1
            turn = 1 - turn

        else:
            # printBoard()
            print("ENTER A NEW VALUE:")
            turn = 0


    if win(x_list,y_list)==24:

        print("X Won!!!")
        printBoard(x_list, y_list)
        break
    if win(x_list, y_list) == 25:
        print("Y Won!!!")
        printBoard(x_list, y_list)
        break
    if win(x_list, y_list) == 10:
        print("Game Over")
        printBoard(x_list, y_list)
        break
    if counter==9:
        print("Game Over")
        break