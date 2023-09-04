def isValidBST(order: [int]) -> bool:
    for i in range(len(order)-1):
        if order[i]<=order[i+1]:
            continue
        else:
            return False
    return True
