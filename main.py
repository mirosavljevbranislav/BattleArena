import random

if __name__ == '__main__':
    eng_game = True
    igrac_counter = 0
    comp_counter = 0

    while eng_game:
        print(f"Vi: {igrac_counter}\nProtivnik: {comp_counter}")
        # 1 - kamen
        # 2 - Papir
        # 3 - Makaze
        rng = random.randint(1, 4)
        player_choice = input("1)Kamen\n2)Papir\n3)Makaze\n4)Quit\n")
        if player_choice == '1':
            if 1 <= rng <= 2:
                print("Kamen - Kamen \nNereseno!")
                continue
            if 2 <= rng <= 3:
                print("Kamen - Papir \nIzgubili ste!")
                comp_counter += 1
                continue
            if 3 <= rng <= 4:
                print("Kamen - Makaze \nPobeda!")
                igrac_counter += 1
                continue
        if player_choice == '2':
            if 1 <= rng <= 2:
                print("Papir - Kamen \nPobeda!")
                igrac_counter += 1
                continue
            if 2 <= rng <= 3:
                print("Papir - Papir \nNereseno!")
                continue
            if 3 <= rng <= 4:
                print("Papir - Makaze \nIzgubili ste!")
                comp_counter += 1
                continue
        if player_choice == '3':
            if 1 <= rng <= 2:
                print("Makaze - Kamen \nIzgubili ste!")
                comp_counter += 1
                continue
            if 2 <= rng <= 3:
                print("Makaze - Papir \nPobeda!")
                igrac_counter += 1
                continue
            if 3 <= rng <= 4:
                print("Makaze - Makaze \nNereseno!")
                continue
        if player_choice == '4':
            break
