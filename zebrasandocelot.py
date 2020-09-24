def expect_time(alist):
    ocelot = []
    for i in range(len(alist)):
        if alist[len(alist)-1-i] == 'O':
            ocelot.append(2**i)

    return ocelot

num_of_animal = int(input())

zoo = []
while(num_of_animal):
    num_of_animal -= 1
    zoo.append(input())

time = 0
time += sum(expect_time(zoo))

print(time)

