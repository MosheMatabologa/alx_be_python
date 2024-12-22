#!/usr/bin/env python3


def daily_reminder():
    # Prompt the user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Validate priority input using a match case
    match priority:
        case "high":
            priority_message = f"'{task}' is a high priority task"
        case "medium":
            priority_message = f"'{task}' is a medium priority task"
        case "low":
            priority_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level entered. Please enter 'high', 'medium', or 'low'.")
            return

    # Check if the task is time-sensitive
    if time_bound == "yes":
        time_message = "that requires immediate attention today!"
    else:
        time_message = "Consider completing it when you have free time."

    # Display the customized reminder
    print(f"Reminder: {priority_message} {time_message}")

if __name__ == "__main__":
    daily_reminder()
