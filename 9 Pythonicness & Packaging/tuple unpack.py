#tuples can be unpacked and assigned to variables
yes, no, maybe, so = [1,2,3,4]
print(yes)
print(no)
print(maybe)
print(so)
#Values assigned to variables can be changed by changing the position of the variable
yes, no, maybe, so = so, maybe, no, yes
print(so)
#an asterisk can be added so the left over values are assigned to that variable
alpha, *beta, charlie, delta = [11,22,33,44,55,66,77,88,99]
#no asterisk needed here
print(beta)