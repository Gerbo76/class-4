while True:
    meows = int(input("How many times should the cat meow? "))
    if meows < 0:
        print("Number of meows cannot be negative.")
        continue
    else:
        break


for i in range(meows):
    print('meow')