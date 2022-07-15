
values = [  30, 20, 100, 90, 160 ]
weights = [  5, 10, 20, 30, 40 ]
W=60
N=len(values);
unit_values=dict();
tokens=[]

for idx in range(N):
    unit_values[idx]=values[idx]/weights[idx]

sorted_values = sorted(unit_values.items(), key=lambda x: x[1], reverse=True)

totalValue=0
for item in sorted_values:
    idx=item[0]
    if (weights[idx]<=W):
        totalValue+=values[idx]
        W-= weights[idx]
        tokens.append(idx)


print("selected items=", tokens)
print("Total  value ",totalValue)