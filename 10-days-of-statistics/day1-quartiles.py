def quantiles(arr, N):
    if N % 2 == 0:
        lower = arr[:N//2]
        upper = arr[N//2:]
        return lower, arr, upper
    else:
        lower = arr[:(N-1)//2]
        upper = arr[(N+1)//2:]
        return lower, arr, upper

def median(*args):
    for array in args[0]:
        N = len(array)
        if N % 2 == 0:
            print((array[(N // 2)] + array[(N//2) - 1]) // 2)
        else:
            print(array[(N - 1) // 2])


if __name__ == '__main__':
    N = int(input())
    arr = sorted(list(map(int, input().split(' '))))
    if len(arr) != N:
        raise ValueError('Tamanho de N e Array não conferem!')
    else:
        median(quantiles(arr, N))
    

