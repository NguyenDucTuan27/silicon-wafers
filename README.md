# silicon-wafers
 
This code was created in 2021 for the "Design and Analyze Algorithms Course"

TIME COMPLEXITY:
 
 T(n)= T(n-1)+1
 when
 i= 0, T(n)=(n-1)+1
 i= 1, T(n)=(n-2)+ 1^1
 ...
 i= n, T(n) = 1+...+(n-1)+(n-2)
 => T(n)=((n-1)  × n)/2
 => T(n) belongs in  Θ(n^2)

