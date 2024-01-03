def solution(s, t):
    count = 0
    for i in range(len(s)-1):
        if s[i].isdigit() and t[i].isdigit():
            if int(s[i]) > int(t[i]):
                count += 1
                break
        elif s[i].isdigit() or t[i].isdigit():
            count += 1
            break
        return count
