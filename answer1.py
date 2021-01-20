def isSubset(set1, set2):
    for element in set2:
        if element not in set1:
            return False
    return True
