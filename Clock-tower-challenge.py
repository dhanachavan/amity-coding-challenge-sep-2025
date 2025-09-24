def calculate_time_differences():
    """
    Calculates the time difference in minutes between a list of clocks
    and the Grand Clock Tower.
    """
    grand_clock_time = "15:00"
    clock_times = ["14:45", "15:05", "15:00", "14:40"]

    def time_to_minutes(time_str):
        """Converts a 'HH:MM' time string to total minutes from midnight."""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    # Convert the Grand Clock Tower time to minutes
    grand_clock_minutes = time_to_minutes(grand_clock_time)

    # Calculate the difference for each clock
    time_differences = []
    for time_str in clock_times:
        clock_minutes = time_to_minutes(time_str)
        difference = clock_minutes - grand_clock_minutes
        time_differences.append(difference)

    # Output the results
    print(f"Grand Clock Tower time: {grand_clock_time}")
    print(f"Clock times around town: {clock_times}")
    print(f"Time differences in minutes: {time_differences}")

if __name__ == "__main__":
    calculate_time_differences()