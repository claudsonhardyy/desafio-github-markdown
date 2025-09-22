import string


def is_palindrome(s: str) -> bool:
    # Remove espaços e pontuação, e converte para minúsculas
    allowed = set(string.ascii_letters + string.digits)
    cleaned = ''.join(c.lower() for c in s if c in allowed)
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    exemplos = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "python",
        "12321",
        "Não é palíndromo!"
    ]
    for exemplo in exemplos:
        print(f"'{exemplo}' -> {is_palindrome(exemplo)}")
