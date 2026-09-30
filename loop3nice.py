def main():
    meow(get_n_meows())

def get_n_meows():
    while True:
        meows = int(input("How many times should the cat meow? "))
        if meows <= 0:
            print("Number of meows cannot be negative.")
        else:
            return meows

def meow(meows):
    for i in range(meows):
        print('meow')

main()