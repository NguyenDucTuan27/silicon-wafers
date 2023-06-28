def maxArea(mat,s):
    max_area = 0
    
    h = [0 for i in range(s)]   #store continuos 1s in each clumn
    l = [0 for i in range(s)]   #store left most index
    r = [s for i in range(s)]   #store right most index
    
    for i in range(s):
        #at each row lb =0, rb =mat-1
        currentLeft=0
        currentRight = len(mat[0])
        for j in range(s):
            if mat[i][j] == "0":
                h[j]=0 #reset if =0
            else:
                h[j] +=1    #count continuous 1s in each colum
        
        #compute left boundary from left to right
                
        for j in range(s):
            if mat[i][j]=="1":  #reset l[j]
                l[j]= max(l[j], currentLeft)
            else:   # update left boundary
                l[j]=0
                currentLeft = j +1
        
        #compute right boundary freom right to left
        for j in range(s-1,-1,-1):
            if mat[i][j] =="1":
                r[j]= min(r[j], currentRight)
            else:
                r[j]= s
                currentRight= j
        for i in range (s):
            max_area = max(max_area, h[j]*(r[j] -l[j][j]))
    return max_area

mat = open('in.txt','r')
mat = [item.split() for item in mat.split('\n')[1:]]
f = open('out.txt','w')
s = len(mat[0])
print(maxArea(mat,s), file = f)