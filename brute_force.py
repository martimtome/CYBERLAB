import itertools
import string
import time
import hashlib
from utils import calculate_entropy, total_combinations, estimate_time, format_time

def brute_force_realistic(target_password, max_length = 4, guesses_per_second=1_000_000_000):

    charsets = [
        string.ascii_lowercase,
        string.ascii_letters,
        string.ascii_letters + string.digits,
        string.ascii_letters + string.digits + string.punctuation
    ]

    target_hash = hashlib.sha256(target_password.encode()).hexdigest()
    attempts = 0
    start_time = time.time()

    print("\n=== Starting Blind Brute Force Attack ===")

    entropy = calculate_entropy(target_password)
    combinations = total_combinations(entropy)
    est_time = estimate_time(guesses_per_second, combinations)
    print(f"Estimated search space: 2^{entropy:.2f} ≈ {combinations:.2e} combinations")
    print(f"Theoretical crack time at {guesses_per_second:,} guesses/sec: {format_time(est_time)}\n")

    for charset in charsets:
        for length in range(1, max_length+1):
            for guess_tuple in itertools.product(charset, repeat=length):
                guess = ''.join(guess_tuple)
                attempts += 1
                guess_hash = hashlib.sha256(guess.encode()).hexdigest()
                if guess_hash == target_hash:
                    elapsed = time.time() - start_time
                    guesses_per_sec_real = attempts / elapsed
                    print("\n=== Password Cracked ===")
                    print(f"Password: {guess}")
                    print(f"Attempts: {attempts}")
                    print(f"Time taken: {elapsed:.4f} seconds")
                    print(f"Real guesses/sec: {guesses_per_sec_real:,.0f}")
                    print(f"Theoretical crack time comparison: {format_time(est_time)}")
                    return
    elapsed = time.time() - start_time
    print("\nPassword not found within max length or charset limit.")
    print(f"Attempts: {attempts}")
    print(f"Time elapsed: {elapsed:.4f} seconds")
