#Mean, Median and Mode
#Given an array, X , of N integers, calculate and print the respective mean, median, and mode on separate lines. 
#If your array contains more than one modal value, choose the numerically smallest one.

def mean(arr, N):
    return sum(arr) / N

def median(arr, N):
    if N%2 != 0:
        return arr[int((N+1)//2) - 1]
    else:
        return (arr[(N//2)-1] + arr[(N//2)]) / 2

def mode(arr, N):
    arr_dic = dict()
    for item in arr:
        if item in arr_dic.keys():
            arr_dic[item] += 1
        else:
            arr_dic[item] = 1
    
    return sorted(arr_dic.items(), key = lambda x: x[1], reverse=True)[0][0]


if __name__ == '__main__':
    N = int(input())
    arr = sorted(list(map(int, input().split(' '))))
    if len(arr) != N:
        raise ValueError('Integer e array não possuem mesmo tamanho!')
    else:
        print(mean(arr, N))
        print(median(arr, N))
        print(mode(arr, N))


    




