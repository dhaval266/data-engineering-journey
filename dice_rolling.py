import random

dies = int(input("How many dice do you want to roll? (1 or 2): ").strip())
count = 0
while True:
    
        
    choice = input("Do you want to roll the dice? (y/n): ").strip().lower()
    
    if choice =='y' or choice == "Y":
        for i in range(dies):
            i = random.randint(1,6)
            print(f'({i})')
        count += 1
        print(f"You rolled the dice {count} time(s).")
    elif choice == 'n' or choice == 'N':
        print("thank you for playing!")
        break
    else:
        print("Invalid input, please enter 'y' or 'n'.")