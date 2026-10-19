import math
import string
import hashlib

def pause():
    input("\nPress Enter to continue...")

def calculate_charset_size(password):
    charset_size= 0

    if any(c.islower() for c in password):
        charset_size += 26

    if any(c.isupper() for c in password):
        charset_size += 26

    if any(c.isdigit() for c in password):
        charset_size += 10

    if any(c in string.punctuation for c in password):
        charset_size += 32

    return charset_size

def calculate_entropy(password):
    length = len(password)
    charset_size = calculate_charset_size(password)

    if length == 0 or charset_size == 0:
        return 0

    entropy = length * math.log2(charset_size)
    return entropy

def total_combinations(entropy):
    return 2 ** entropy

def estimate_time(guesses_per_second, combinations):
    if guesses_per_second <= 0:
        return float("inf")
    return combinations / guesses_per_second

def format_time(seconds):
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day

    if seconds < minute:
        return f"{seconds:.4f} seconds"
    elif seconds < hour:
        return f"{seconds / minute:.2f} minutes"
    elif seconds < day:
        return f"{seconds / hour:.2f} hours"
    elif seconds < year:
        return f"{seconds / day:.2f} days"
    else:
        return f"{seconds / year:.2f} years"

def show_exponential_growth(charset_size, max_length=12, guesses_per_second=1_000_000_000):
    print("\n=== Exponential Growth Simulation ===")
    for length in range(1, max_length + 1):
        entropy = length * math.log2(charset_size)
        combinations = total_combinations(entropy)
        seconds = estimate_time(guesses_per_second, combinations)
        print(f"Length {length:2} | Entropy: {entropy:6.2f} bits | Combinations: {combinations:.2e} | Estimated crack time: {format_time(seconds)}")

def show_entropy_growth(charset_size, max_length=12, guesses_per_second=1_000_000_000):
    print("\n===== EXPONENTIAL GROWTH SIMULATION =====")

    previous_combinations = None

    for length in range(1, max_length + 1):
        entropy = length * math.log2(charset_size)
        combinations = 2 ** entropy
        seconds = combinations / guesses_per_second

        if previous_combinations:
            growth_factor = combinations / previous_combinations
            growth_text = f"{growth_factor:.0f}x increase"
        else:
            growth_text = "-"

        print(
            f"Length: {length:2} | "
            f"Entropy: {entropy:6.2f} bits | "
            f"Combinations: {combinations:.2e} | "
            f"Crack time: {format_time(seconds):>15} | "
            f"{growth_text}"
        )

        previous_combinations = combinations

    print("===============================================\n")

def security_report(password, guesses_per_second=1_000_000_000):
        entropy = calculate_entropy(password)
        combinations = total_combinations(entropy)
        est_time = estimate_time(guesses_per_second, combinations)

        print("\n======= PASSWORD SECURITY REPORT =======")
        print(f"Password Length: {len(password)}")
        print(f"Entropy: {entropy:.2f} bits")
        print(f"Search Space: 2^{entropy:.2f}")
        print(f"Total Combinations: {combinations:.2e}")
        print(f"Estimated Crack Time ({guesses_per_second:,} guesses/sec): {format_time(est_time)}")
        print("========================================\n")

def entropy_bar(entropy):
    max_bits= 100
    scale = min(40, int((entropy / max_bits) * 40))
    bar = "█" * scale
    print(f"Entropy Visualization: \n[{bar:<40}] {entropy:.2f} bits\n")
