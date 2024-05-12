ls = [1,2,3,4,5]
def findtarg(ls,target):
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if ls[i] + ls[j] == target:
                return i,j
x = findtarg(ls,8)
print(x)


def deepcop(x,y):
    hold =[]
    for i in range(len(x)):
        hold.append(i)
    y = hold
    return y

