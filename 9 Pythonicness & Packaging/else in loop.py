#else statements after for and while loops will run if the loop ends without breaking
for i in range(20):
    if i > 18:
        break
else:
    print("loop 1 did not break")
x = 10
while x > 0:
    x -= 1
    if x > 20:
        break
else:
    print("loop 2 did not break")