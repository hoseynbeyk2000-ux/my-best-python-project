import string

password = input("Enter your password: ")

length = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(c in string.punctuation for c in password)

score = 0

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1

print("\n🔐 Password Analysis")

if score <= 2:
    print("❌ Weak password")
elif score == 3 or score == 4:
    print("⚠️ Medium password")
else:
    print("✅ Strong password")

print("\nSuggestions:")
if length < 8:
    print("- Use at least 8 characters")
if not has_upper:
    print("- Add uppercase letters")
if not has_lower:
    print("- Add lowercase letters")
if not has_digit:
    print("- Add numbers")
if not has_symbol:
    print("- Add symbols")
