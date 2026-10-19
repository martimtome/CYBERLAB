from hashing import sha256_hash, sha1_hash, md5_hash
from analyzer import analyze_password
from brute_force import brute_force_realistic
from estimator import estimate_crack_time
from utils import pause, security_report, entropy_bar, show_entropy_growth, calculate_entropy

def main():
    while True:
        print("\n======= CYBERLAB: Password Security Simulator =======")
        print("1. Generate Hash")
        print("2. Analyze Password Strength")
        print("3. Simulate Brute Force Attack")
        print("4. Estimate Crack Time")
        print("5. Exit")
        print("=======================================================")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice not in ["1", "2", "3", "4", "5"]:
            if choice == "":
                continue
            print("\nInvalid choice. Try again.")
            continue

        elif choice == "1":
            password = input("\nEnter password: ")
            print("\n--- Hash Results ---")
            print("SHA256:", sha256_hash(password))
            print("SHA1:", sha1_hash(password))
            print("MD5:", md5_hash(password))
            pause()

        elif choice == "2":
            password = input("\nEnter password: ")
            entropy, level = analyze_password(password)
            print("\n--- Password Analysis ---")
            print(f"Entropy: {entropy:.2f} bits")
            print(f"Strength Level: {level}")
            entropy_bar(entropy)
            pause()

        if choice == "3":
            target = input("\nEnter target password (max 4 characters recommended): ")
            brute_force_realistic(target)
            pause()

        if choice == "4":
            password = input("\nEnter password: ")
            security_report(password)
            entropy_bar(calculate_entropy(password))
            pause()

        elif choice == "5":
            print("\nExiting CYBERLAB. Stay secure 🔒")
            break

if __name__ == "__main__":
    main()
