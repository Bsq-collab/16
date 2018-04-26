def union(a,b):
    ans= []
    [ans.append(x) for x in a if x not in ans]
    [ans.append(x) for x in b if x not in ans]
    return ans

def intersection(a,b):
    ans=[]
    [ans.append(x) for x in a if x in b and x not in ans]
    return ans
def set_diff(a,b):
    ans=[]
    [ans.append(x) for x in a if x not in b and x not in ans]
    return ans

def symmetrical_diff(a,b):
    u=union(a,b)
    inter=intersection(a,b)
    return set_diff(u,inter)

def cartesian_product(a,b):
    ans=[]
    [ans.append((x,y)) for x in a for y in b if (x,y) not in ans]
    return ans


print union([1,2,3,4,5,5,5,5,6,6,7],[9,8,7,6,5,5])
print intersection([1,2,3,4,5],[3,5,6,7,8])
print set_diff([8,9,3,5,2,2],[5,6,10,3,3,8])
print symmetrical_diff([1,2,3],[2,3,4])
print cartesian_product([2,'white'],[9,'orange',78,'bob','jen'])
