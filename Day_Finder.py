from datetime import datetime

def main():
    # Prompt the user to enter a date
    date_input = input("Enter a date (dd/mm/yyyy): ").strip()

    try:
        # Parse the date input
        date = datetime.strptime(date_input, "%d/%m/%Y")
        
        # Get the day of the week
        weekday = date.strftime("%A")
        
        # Print the day of the week
        print(f"The day on {date.day}/{date.month}/{date.year} was a {weekday}")
        
    except ValueError:
        # Handle invalid date format or invalid date values
        print("Invalid date provided. Please ensure the date is valid and in the format dd/mm/yyyy.")

if __name__ == "__main__":
    main()
