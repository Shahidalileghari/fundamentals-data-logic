def is_eligible(age: int, has_consent: bool) -> bool:
    return age >= 18 and has_consent

def classify_number(number: int) -> str:
    if number == 0:
        return "zero"
    return "positive" if number > 0 else "negative"

if __name__ == "__main__":
    print(is_eligible(21, True))
    print(classify_number(-4))
