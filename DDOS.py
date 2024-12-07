import random
import string

def generate_random_symbols():
    """Generate a random string with letters, numbers, and symbols."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(20))  # Generate a string of 20 characters

def insert_attack_message(target):
    """Insert the attack message in the middle of the target string."""
    attack_message = " attacking target port 8080 turbo 135 "
    mid_index = len(target) // 2
    return target[:mid_index] + attack_message + target[mid_index:]

def main():
    print("Welcome to the Symbol Generator and Attack Message Inserter!")
    target = input("Enter the target: ")
    modified_target = insert_attack_message(target)
    print(f"\nModified Target:\n{modified_target}\n")
    
    print("Generating unlimited random symbols. Press Ctrl+C to stop.\n")
    try:
        while True:
            print(generate_random_symbols())
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")

if __name__ == "__main__":
    main()