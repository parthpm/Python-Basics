li=[True,True,True,False]

print(all(li))
print(any(li))


def all_(li):
    for item in li:
        if not item:
            return False
    return True
def any_(li):
    for item in li:
        if item:
            return True
    return False

print(all_(li))
print(any_(li))
