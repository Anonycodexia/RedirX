import os

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# RedirX Banner in light red style
banner = '''
\033[91m  
      ██▀███  ▓█████ ▓█████▄  ██▓ ██▀███  ▒██   ██▒
     ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓██▒▓██ ▒ ██▒▒▒ █ █ ▒░
     ▓██ ░▄█ ▒▒███   ░██   █▌▒██▒▓██ ░▄█ ▒░░  █   ░
     ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌░██░▒██▀▀█▄   ░ █ █ ▒ 
     ░██▓ ▒██▒░▒████▒░▒████▓ ░██░░██▓ ▒██▒▒██▒ ▒██▒
     ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░▓  ░ ▒▓ ░▒▓░▒▒ ░ ░▓ ░
       ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ▒ ░  ░▒ ░ ▒░░░   ░▒ ░
       ░░   ░    ░    ░ ░  ░  ▒ ░  ░░   ░  ░    ░  
        ░        ░  ░   ░     ░     ░      ░    ░  
                       ░                             \033[0m
'''

# Print the light red banner
print(banner)

# Print the "Coded by RedirX" message in green
print("\033[92m             RedirX Coded by Anonycodexia\033[0m")

print("")

def main():
    print("Please select your preference:")
    print("1) User Interaction (Recommended)")
    print("2) No User Interaction")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        print("Executing redirx.py...")
        os.system("python redirxx.py")
    elif choice == '2':
        print("Executing redirxx.py...")
        os.system("python redirxxx.py")
    else:
        print("Invalid choice. Please run the script again and select 1 or 2.")

if __name__ == "__main__":
    main()
