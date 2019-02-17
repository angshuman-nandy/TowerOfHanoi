def printInfo():
    print("------------------TOWER OF HANOI---------------")
    print("\n There are three towers: 1,2 and 3. Initially the \"tower 1\" has all the 5 rings, numbered 1 to 5")
    print("The objective of the game is to move all the rings from \"tower 1\" to \"tower 3\" using \"tower 2\"")
    print("The only rule of the game is that one cannot place a higher numbered ring over a lower numbered ring \n "
          "in a tower, trying to do so will make it a \"WRONG MOVE\"....\n Cheers!!:)")
    print("-------------------------------------------------")


def printTower(t1,t2,t3,step):
    tr1 = reversed(t1)
    tr2 = reversed(t2)
    tr3 = reversed(t3)
    rings = {1: "    *1*", 2: "   **2**", 3: "  ***3***", 4: " ****4****", 5: "*****5*****"}
    # max_len = 0
    # if len(t1) > len(t2):
    #     max_len = len(t1)
    # else:
    #     max_len = len(t2)
    # if max_len < len(t3):
    #     max_len = len(t3)


    print("----- TOWERS ------")
    print("Tower 1")
    if t1 == []:
        print("(NO RINGS)") 
    for i in tr1:
        print("  "+rings[i])
    print("Tower 2")
    if t2 == []:
        print("(NO RINGS)") 
    for i in tr2:
        print("  "+rings[i])
    print("Tower 3")
    if t3 == []:
        print("(NO RINGS)")
    for i in tr3:
        print("  "+rings[i])
    print("------STEP: "+str(step)+"----------")		
    print("--------------------")


def move(t_from, t_to):
    t_to.append(t_from[len(t_from)-1])
    t_from.pop()
    return t_from, t_to


def checkMove(t_from, t_to):
    if t_to != []:
        if t_to[len(t_to)-1] < t_from[len(t_from)-1]:
            return False
        else:
            return True
    else:
        return True	


def gameEnd(t, step):
    if t == [5, 4, 3, 2, 1]:
        print("Congratulations!!! you have completed the game in "+str(step)+" steps") 
        return True
    else:
        return False	


def initGame():
    printInfo()
    towers = {"1": [5, 4, 3, 2, 1], "2": [], "3": [], "exit": [-1]}
    step_count = 0
    printTower(towers["1"], towers["2"], towers["3"], step_count)
    g_end = False
    while not g_end:
        while True:
            tower_from = input("move from tower")
            if tower_from not in ["1", "2", "3", "exit"]:
                print("please choose from 1,2,3 or exit")
            if tower_from in ["1", "2", "3"] and towers[tower_from] == []:
                    print("please choose a tower with rings to move from!!")
            if tower_from in ["1", "2", "3", "exit"] and towers[tower_from] != []:
                break
        while True:
            tower_to = input("move to tower")
            if tower_to not in ["1", "2", "3", "exit"]:
                print("please choose from 1,2,3 or exit")
            if tower_to in ["1", "2", "3", "exit"]:
                break
        if checkMove(towers[tower_from], towers[tower_to]) and tower_from != tower_to:
            step_count = step_count+1
            towers[tower_from], towers[tower_to] = move(towers[tower_from], towers[tower_to])
            printTower(towers["1"], towers["2"], towers["3"], step_count)
        else:
            print("Wrong Move!!!!!")
        g_end = gameEnd(towers["3"], step_count)
        if tower_from == "exit" or tower_to == "exit":
            print("see you next time.. hope you liked playing")
            g_end = True


initGame()
