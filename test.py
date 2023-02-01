

# we have 10 balance
# we withdraw 5
# expect 5

balance=10



withdraw=5
result=balance - withdraw
# write test here
assert result == 5, "Balance should be 5"



# we withdraw 1
# expect 9


withdraw=1
result=balance - withdraw
# write test here
assert result == 9, "Balance should be 9"


# we withdraw 3
# expect 7

withdraw=3
result=balance - withdraw
# write test here
assert result == 7, "Balance should be 7"


# we withdraw 6
# expect 4


withdraw=6
result=balance - withdraw
# write test here
assert result == 4, "Balance should be 4"


# we withdraw 8
# expect 2


withdraw=8
result=balance - withdraw
# write test here
assert result == 20, "Balance should be 2"