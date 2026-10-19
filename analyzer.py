from utils import calculate_entropy

def analyze_password(password):
    entropy = calculate_entropy(password)

    if entropy < 28:
        level = "Very Weak"
    elif entropy < 36:
        level = "Weak"
    elif entropy < 60:
        level = "Reasonable"
    elif entropy < 128:
        level = "Strong"
    else:
        level = "Very Strong"

    return round(entropy, 2), level
