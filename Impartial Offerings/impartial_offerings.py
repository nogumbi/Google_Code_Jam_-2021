def arohaOfferings():
    t = int(input("Input test cases: "))
    for j in range(t):
        print(t)
        n = int(input("Number of pets: "))
        sizes = input("sizes: ").split()

        int_list = [int(i) for i in sizes]
        x = min(int_list)
        y = max(int_list)
        

        min_list = [i for i in int_list if (i == x)]
        max_list = [i for i in int_list if (i == y)]
        mid_list = [i for i in int_list if (x<i<y)]

        if len(mid_list) == 0:
            treats = len(min_list) *1 + len(max_list) *2
        elif x == y:
            treats = len(int_list) * 1
        else:
            treats = (len(min_list) * 1 + len(mid_list) * 2 + len(max_list) * 3)

        print(f'Cases #{j + 1}: {treats}')

if __name__ == "__main__":
    arohaOfferings()