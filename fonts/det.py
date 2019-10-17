def det(a):
    d=0;
    if len(a)==1 and len(a[0])==1:
        return a[0][0];
    for i in range(len(a)):
        d+=((-1)**i)*a[0][i]*det(minor(a,0,i));
    return d;
def minor(a,x,y):
    return [[a[i][j] for j in range(len(a[0])) if j!=y] for i in range(len(a)) if i!=x];
print(det([[6,1,1],[4,-2,5],[2,8,7]]));

