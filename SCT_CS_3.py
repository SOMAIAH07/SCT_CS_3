import re

def assess_password_strength(password):
    """
    Assesses the strength of a password based on various criteria.
    Returns a dictionary with strength score and feedback.
    """
    score = 0
    feedback = []
    
    # Check length
    length = len(password)
    if length >= 12:
        score += 3
        feedback.append("✓ Excellent length (12+ characters)")
    elif length >= 8:
        score += 2
        feedback.append("✓ Good length (8-11 characters)")
    elif length >= 6:
        score += 1
        feedback.append("⚠ Fair length (6-7 characters) - consider making it longer")
    else:
        feedback.append("✗ Too short (less than 6 characters)")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters")
    
    # Check for numbers
    if re.search(r'\d', password):
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 2
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters")
    
    # Check for common patterns (bonus deduction)
    common_patterns = ['123', 'abc', 'password', 'qwerty', '111', '000']
    for pattern in common_patterns:
        if pattern.lower() in password.lower():
            score -= 1
            feedback.append("⚠ Contains common pattern")
            break
    
    # Determine strength level
    if score >= 7:
        strength = "STRONG"
        color = "🟢"
    elif score >= 5:
        strength = "MODERATE"
        color = "🟡"
    elif score >= 3:
        strength = "WEAK"
        color = "🟠"
    else:
        strength = "VERY WEAK"
        color = "🔴"
    
    return {
        'score': score,
        'strength': strength,
        'color': color,
        'feedback': feedback
    }

def main():
    print("=" * 60)
    print("           --- PASSWORD STRENGTH CHECKER ---")
    print("=" * 60)
    print("\nThis tool will assess your password based on:")
    print("  • Length (minimum 6, recommended 12+)")
    print("  • Uppercase letters (A-Z)")
    print("  • Lowercase letters (a-z)")
    print("  • Numbers (0-9)")
    print("  • Special characters (!@#$%^&*, etc.)")
    print("=" * 60)
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\nThank you for using Password Strength Checker!")
            break
        
        if not password:
            print("⚠ Please enter a password!")
            continue
        
        # Assess the password
        result = assess_password_strength(password)
        
        # Display results
        print("\n" + "=" * 60)
        print(f"PASSWORD STRENGTH: {result['color']} {result['strength']}")
        print(f"Score: {result['score']}/8")
        print("=" * 60)
        print("\nDetailed Feedback:")
        for item in result['feedback']:
            print(f"  {item}")
        
        # Provide recommendations
        if result['score'] < 7:
            print("\n💡 Recommendations:")
            if len(password) < 12:
                print("  • Increase password length to 12+ characters")
            if not re.search(r'[a-z]', password):
                print("  • Add lowercase letters")
            if not re.search(r'[A-Z]', password):
                print("  • Add uppercase letters")
            if not re.search(r'\d', password):
                print("  • Add numbers")
            if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
                print("  • Add special characters")
        else:
            print("\n✓ Great job! Your password is strong.")
        
        print("=" * 60)

if __name__ == "__main__":
    main()