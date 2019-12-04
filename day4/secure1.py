def bruteforce(lower_limit: int, upper_limit) -> int:
    possible_passwords = 0
    for i in range(lower_limit, upper_limit + 1):
        if is_match(i):
            possible_passwords += 1
    return possible_passwords


def is_match(password: int) -> bool:
    s = str(password)
    if ''.join(sorted(s)) != s:
        return False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


upper_limit = 240298
lower_limit = 784856

print(bruteforce(upper_limit, lower_limit))
