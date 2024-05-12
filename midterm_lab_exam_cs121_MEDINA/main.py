game_library = {
    "Donkey Kong": {"copies_available": 3, "cost": 2},
    "Super Mario Bros": {"copies_available": 5, "cost": 3},
    "Tetris": {"copies_available": 2, "cost": 1}
}

account_library = {}


def list_available_games():
    print("Available Games:")
    for index, (game, details) in enumerate(game_library.items(), start=1):
        print(f"{index}. {game} - Copies available: {details['copies_available']}, Cost: ${details['cost']}")


def register_user():
    while True:
        print("Registration Page")
        username = input("Please input a username: ")
        password = input("Enter a password (min 8 characters): ")
        if len(password) < 8:
            print("The password must be at least 8 characters long.")
            continue
        account_library[username] = {
            "username": username,
            "password": password,
            "balance": 0,
            "points": 0,
            "rented_games": []
        }
        print("Account created successfully!")
        return


def authenticate(username, password):
    return account_library.get(username, {}).get("password") == password


def user_login():
    print("User Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if authenticate(username, password):
        print("Login successful.")
        user_dashboard(username)
    else:
        print("Invalid username or password")


def admin_login():
    print("Admin Login")
    username = input("Admin username: ")
    password = input("Admin password: ")
    if username == "admin" and password == "adminpass":
        print("Admin login successful.")
        admin_dashboard()
    else:
        print("Invalid admin credentials")


def user_dashboard(username):
    while True:
        print(f"--- {username}'s User Dashboard ---")
        print("1. Rent a game")
        print("2. Return a game")
        print("3. Top up balance")
        print("4. View rented games")
        print("5. Redeem free game rentals")
        print("6. View points")
        print("7. Log out")
        choice = input("Select an option: ")
        if choice == '1':
            rent_game(username)
        elif choice == '2':
            return_game(username)
        elif choice == '3':
            top_up(username)
        elif choice == '4':
            display_rented_games(username)
        elif choice == '5':
            redeem_games(username)
        elif choice == '6':
            display_points(username)
        elif choice == '7':
            print("Logging out...")
            break
        else:
            print("Invalid option selected. Please try again.")


def top_up(username):
    amount = float(input("Enter the amount to top-up: $"))
    if amount > 0:
        account_library[username]["balance"] += amount
        print(f"New balance is ${account_library[username]['balance']}")
    else:
        print("Please enter a positive number for top-up amount")


def rent_game(username):
    list_available_games()
    choice = int(input("Select a game to rent by indexing number: "))
    game_title = list(game_library.keys())[choice - 1]
    game_details = game_library[game_title]
    if game_details["copies_available"] > 0:
        cost = game_details["cost"]
        if account_library[username]["balance"] >= cost:
            account_library[username]["balance"] -= cost
            account_library[username]["points"] += cost // 2  # Earn points
            account_library[username]["rented_games"].append(game_title)
            game_details["copies_available"] -= 1
            print(f"Rented {game_title}.")
        else:
            print("Insufficient balance.")
    else:
        print("No copies available.")


def return_game(username):
    print("Your rented games:")
    for idx, game in enumerate(account_library[username]["rented_games"], start=1):
        print(f"{idx}. {game}")
    choice = int(input("Select a game to return by index number: "))
    game_title = account_library[username]["rented_games"].pop(choice - 1)
    game_library[game_title]["copies_available"] += 1
    print(f"{game_title} returned successfully.")


def display_rented_games(username):
    if account_library[username]["rented_games"]:
        print("Rented Games:")
        for game in account_library[username]["rented_games"]:
            print(game)
    else:
        print("No games rented.")


def redeem_games(username):
    needed_points = 10
    points = account_library[username]["points"]
    if points >= needed_points:
        account_library[username]["points"] -= needed_points
        print("Congratulations! You've redeemed a free game rental!")
    else:
        print(f"Need {needed_points} points to redeem a game, you have {points} points.")


def display_points(username):
    print(f"Your points: {account_library[username]['points']}")


def admin_dashboard():
    while True:
        print("Admin Dashboard")
        print("1. View all games")
        print("2. Add or update a game")
        print("3. Log out")
        choice = input("Select an option: ")
        if choice == '1':
            list_available_games()
        elif choice == '2':
            add_or_update_game()
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid option.")


def add_or_update_game():
    game = input("Enter the game name: ")
    copies = int(input("Enter the number of copies: "))
    cost = float(input("Enter the cost per rental: "))
    game_library[game] = {"copies_available": copies, "cost": cost}
    print(f"Game {game} updated. Copies: {copies}, Cost: ${cost}.")


def main_menu():
    while True:
        print("Main Menu")
        print("1. Show Available Games")
        print("2. Register")
        print("3. User Login")
        print("4. Admin Login")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_available_games()
        elif choice == '2':
            register_user()
        elif choice == '3':
            user_login()
        elif choice == '4':
            admin_login()
        elif choice == '5':
            print("Thank you for using the system.")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main_menu()
