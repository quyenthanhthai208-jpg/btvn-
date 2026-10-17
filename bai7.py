
def solution(fishes, k, n):
    counter = [0] * 61

    for fish in fishes:
        counter[fish] += 1

    cnt = 0
    for i in range(1, k + 1):
        cnt += counter[i]

    for i in range(k + 1, 61):
        if cnt >= n:
            return True
        cnt += counter[i]
        cnt -= counter[i - k]
    
    if cnt >= n:
        return True
