
'''
sondan başla
her adımda  n inci parçayı alıp 
almayacağına  karar ver.

base case  hiç parça kalmaması

'''
def recursive_knapsack(v,w,n,W):
    if (n==0):
        return 0

    # take last item if possible
    take_it=0
    if(w[n]<=W):
        take_it=v[n]+recursive_knapsack(v,w,n-1,W-w[n],)
    leave_it=recursive_knapsack(v,w,n-1,W)

    if (take_it>leave_it):
     #   if n not in tokens:
      #      tokens.append(n)
        return take_it
    else:
        return leave_it
    


values = [ -1, 30, 20, 100, 90, 160 ]
weights = [ -1, 5, 10, 20, 30, 40 ]
W=60
tokens=[]
print(recursive_knapsack(values,weights,5,60))
print(tokens)