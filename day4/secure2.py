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

    groupings = []
    matching = False
    start = 0
    end = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            if matching:
                end = i + 1
            else:
                start = i
                end = i + 1
                matching = True
        elif matching:
            groupings.append(s[start:end + 1])
            matching = False
    if matching:
        groupings.append(s[start:end + 1])

    for g in groupings:
        if len(g) == 2:
            return True
    return False


lower_limit = 240298
upper_limit = 784856

print(bruteforce(lower_limit, upper_limit))
