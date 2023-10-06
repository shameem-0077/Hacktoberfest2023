import random

def main():
    print("Welcome to the Sudo Adventure Game!")
    print("You are a system administrator.")
    print("Your goal is to complete tasks using the 'sudo' command.")
    print("Be careful! Mistakes can have consequences.")

    tasks = [
        ("Install a package", "sudo apt-get install <package-name>"),
        ("Edit a system file", "sudo nano /etc/<file-name>"),
        ("View system logs", "sudo tail /var/log/syslog"),
        ("Delete a file", "sudo rm <file-name>"),
        ("List directory contents", "sudo ls -l <directory>"),
    ]

    score = 0

    while True:
        task, command = random.choice(tasks)
        print("\nTask: {}".format(task))
        user_input = input("Enter the 'sudo' command to complete the task (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            break

        if user_input.strip() == command:
            print("Task completed successfully!")
            score += 1
        else:
            print("Oops! That wasn't the correct command. Be careful!")

    print("Game Over! Your score: {}".format(score))

if __name__ == "__main__":
    main()
