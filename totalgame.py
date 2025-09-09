total = int(input("number of games played = " ))
won  = int(input("number of games won = "))
loss  = int(input("number of games loss = "))
tie  = total-won-loss
print(tie)


won points = won*4 + tie*2

print(points)
