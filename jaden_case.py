def solution(s):
    s = s.lower()
    list_s = list(s)
    list_s[0] = list_s[0].upper()

    length = len(list_s)

    for i in range(length):
        if list_s[i] == ' ':
            if i == length - 1:
                print(i)
                break
            list_s[i + 1] = list_s[i + 1].upper()
    new_string = ''.join(list_s)

    return new_string

print(solution("3people unFollowed me "))