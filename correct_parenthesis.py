def solution(s):

    top = 0
    result = False
    
    for i in range(len(s)):
        if s[i] == '(':
            top += 1
        elif s[i] == ')':
            if top == 0:
                result = False
                return result
            else:
                top -= 1
            result = True
    if top != 0:
        result = False
    return result