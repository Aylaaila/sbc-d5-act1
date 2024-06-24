def display_commands(commands):
    print("Display:", commands)

def main():
    u = [int(input(f"COMMAND {i+1}: ")) for i in range(4)]
    display_commands(u)

    while True:
        ai = input("Enter naa, wala, add: ").strip().lower()
        if ai == "naa":
            u.pop(0)
        elif ai == "wala":
            u.pop(3)
        elif ai == "add":
            u.append(int(input("Add: ")))
        else:
            print("nah")
        display_commands(u)

if __name__ == "_main_":
    main()