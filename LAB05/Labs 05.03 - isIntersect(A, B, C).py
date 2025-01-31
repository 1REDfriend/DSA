def isIntersect(a, b, c):
    for x in a:
        if x in b and x in c:
            return True
    return False

print(isIntersect(input().strip("[]").split(", "),input().strip("[]").split(", "),input().strip("[]").split(", ")))
