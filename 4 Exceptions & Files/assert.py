#assert let's you check stuff and errors out if wrong
try:
    temp = -10
    #it is checking if temp is greater than or equal to 0, since it is not it goes to the except
    assert (temp >= 0)
    #this is skipped
    print("hmm")
#because this except is for AssertionError, it will print. It does not need to be specifically told to catch AssertionErrors
except AssertionError:
    print("Too cold buddy")