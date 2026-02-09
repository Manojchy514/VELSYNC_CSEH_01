import re

def check_password_strength(password):
    # Criteria tracking
    score = 0
    remarks = ""
    points = {
        "length": False,
        "upper": False,
        "lower": False,
        "digit": False,
        "special": False
    }

    # 1. Check Length
    if len(password) >= 8:
        points["length"] = True
        score += 1
    
    # 2. Check Uppercase
    if re.search(r"[A-Z]", password):
        points["upper"] = True
        score += 1

    # 3. Check Lowercase
    if re.search(r"[a-z]", password):
        points["lower"] = True
        score += 1

    # 4. Check Digits
    if re.search(r"\d", password):
        points["digit"] = True
        score += 1

    # 5. Check Special Characters
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password):
        points["special"] = True
        score += 1

    # Determine Strength Label
    if score < 3:
        remarks = "TOO WEAK ❌"
    elif score == 3:
        remarks = "WEAK ⚠️"
    elif score == 4:
        remarks = "MEDIUM ✅"
    elif score == 5:
        remarks = "STRONG 💪"

    return score, remarks, points

def main():
    print("--- 🛡️ Password Strength Analyzer ---")
    user_pass = input("Enter a password to test: ")
    
    score, remarks, points = check_password_strength(user_pass)

    print(f"\nStrength Result: {remarks}")
    print(f"Score: {score}/5")
    
    print("\n--- Detailed Breakdown ---")
    print(f"[{'✔' if points['length'] else ' '}] 8+ Characters")
    print(f"[{'✔' if points['upper'] else ' '}] Uppercase Letters")
    print(f"[{'✔' if points['lower'] else ' '}] Lowercase Letters")
    print(f"[{'✔' if points['digit'] else ' '}] Numbers")
    print(f"[{'✔' if points['special'] else ' '}] Special Characters")

if __name__ == "__main__":
    main()