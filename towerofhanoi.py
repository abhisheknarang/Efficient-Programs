def printMove(fr, to):
    print("Move from "+ str(fr) + " to " + str(to))

def TowerofHanoi(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        TowerofHanoi(n-1, fr, spare, to)
        TowerofHanoi(1, fr, to, spare)
        TowerofHanoi(n-1, spare, to, fr)
print TowerofHanoi(4, "D1", "D2", "D3")
