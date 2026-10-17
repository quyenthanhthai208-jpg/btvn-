def getCount(tmp):
    count = 0

    for i in range(0, len(tmp)):
        if tmp[i] != 0:
            count+=1

    return count


def check(in_data1, in_data2):
    tmp = list()

    for i in range(0, len(in_data1)):
          tmp.append(in_data1[i])   

    for i in range(0, len(tmp)):
        for j in range(0, len(in_data2)):
            if tmp[i] == in_data2[j]:
                tmp[i] = 0
                break

    return tmp


def solution(in_data1, in_data2):
    tmp1 = check(in_data1, in_data2)
    tmp2 = check(in_data2, in_data1)

    count = getCount(tmp1) + getCount(tmp2)
    answer = list()

    c = 0
    for i in range(0, len(tmp1)):
        if tmp1[i] !=0 and c <= count:
              answer.append(tmp1[i])   
              count += 1

    for i in range(0, len(tmp2)):
        if tmp2[i] != 0 and c <= count:
            answer.append(tmp2[i])
            count += 1

    answer.sort()
    return answer





