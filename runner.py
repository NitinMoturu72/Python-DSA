if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sarr = list(arr)
    for i in range(len(sarr)):
        for j in range(i, len(sarr)):
            if(sarr[i]> sarr[j]):
                temp = sarr[j]
                sarr[j] = sarr[i]
                sarr[i] = temp
            elif(sarr[i] == sarr[j]):
                sarr = sarr.pop(j)
    print(sarr)