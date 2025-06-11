a = 4

while a >= 1:
    if a != 3:
        print(a)

    a = a-1
print("while loop execution is finished")

b = 10

while b >= 1:
    if b==9:
        b = b-1 #need to stop the infinite loop of b = 9 as it will not decrement as it skips that step.
        continue # with this the value of b remains 9 as all other steps are crossed
    if b== 3:
        break # only  values till 3 will be displayed as loop will be broken after having values 3
    print(b)

    b = b-1
print("while loop execution is done")
