def m():
    magic_square=[[8,3,4],[1,5,9],[6,7,2]]
    i=0
    while i<len(magic_square):
        j=0
        row=0
        c=0
        d=0
        while j<len(magic_square[i]):
            row=row+magic_square[i][j]
            c=c+magic_square[j][i]
            d=d+magic_square[j][j]
            j=j+1
        i=i+1
    if row==c==d:
       print("magic_square")
    else:
       not("not magic _square")
    print(row)
    print(d)
    print(c)
m()