def max_sum_subarray(a):
    total = 0
    max_sum = 0
    for i in range(len(a)):
        total += a[i]
        if total < 0:
            total = 0
        max_sum = max(max_sum, total)
    return max_sum


if __name__ == "__main__":
    print(max_sum_subarray([2, 1, 4, -7, 5, 3, -1, 4]))
