#all is true if all values in a list match argument
f = [1.12,4.34,6.91,2.456,0.991]
if all([i < 10 for i in f]):
    print("All smaller than 10")
#any is true if at least one value in a list matches argument
if any([i > 5 for i in f]):
    print("At least one larger than 5")