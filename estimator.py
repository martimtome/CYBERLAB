from utils import calculate_entropy, calculate_charset_size, format_time

def estimate_crack_time(password):
    entropy = calculate_entropy(password)
    charset_size = calculate_charset_size(password)

    if entropy == 0:
        print("Invalid password.")
        return

    combinations = 2 ** entropy

    guesses_per_second = 1_000_000_000

    seconds = combinations / guesses_per_second

    print("\n--- Crack Time Estimation ---")
    print(f"Character set size: {charset_size}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Total possible combinations: {combinations:.2e}")
    print(f"Assuming {guesses_per_second:,} guesses per second...\n")

    print("Estimated time to crack:")
    print(format_time(seconds))

    if seconds < minute:
        return f"{seconds:.2f} seconds"
    elif seconds < hour:
        return f"{seconds / minute:.2f} minutes"
    elif seconds < day:
        return f"{seconds / hour:.2f} hours"
    elif seconds < year:
        return f"{seconds / day:.2f} days"
    else:
        return f"{seconds / year:.2f} years"
