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





