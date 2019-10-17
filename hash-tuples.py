if __name__ == '__main__':
    n = int(input())
    integers = map(int, input().split())
    tuple_i = tuple(integers)
    print(hash(tuple_i))
    