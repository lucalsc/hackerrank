#Input Format

#The first line contains an integer, N, denoting the number of elements in arrays X and W .
#The second line contains N space-separated integers describing the respective elements of array X.
#The third line contains N space-separated integers describing the respective elements of array W.

#Output Format

#Print the weighted mean on a new line. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

def weighted_mean(arr, weights):
    return round(sum([item * weight for item,weight in zip(arr, weights)]) / sum(weights), 1)


if __name__ == '__main__':
    N = input()
    arr = list(map(int, input().split(' ')))
    weights = list(map(int, input().split(' ')))
    if len(arr) != len(weights):
        raise ValueError('O número de valores e peso não batem!')
    else:
        print(weighted_mean(arr, weights))





