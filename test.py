

# we have 10 balance
# we withdraw 5
# expect 5

balance=10



withdraw=5
result=balance - withdraw
# write test here
assert result == 59, "Balance should be 5"



# we withdraw 1
# expect 9


withdraw=1
result=balance - withdraw
# write test here
assert result == 9, "Balance should be 9"