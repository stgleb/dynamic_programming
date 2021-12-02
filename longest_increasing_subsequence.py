def longest_increasing_subsequence(a):
    n = len(a)
    seq = [0 for _ in range(n)]
    prev = [-1 for _ in range(n)]
    seq[0] = 1
    max_len = 0
    max_index = 0
    for i in range(n):
        for j in reversed(range(i)):
            if a[j] < a[i]:
                if seq[i] < seq[j] + 1:
                    seq[i] = seq[j] + 1
                    prev[i] = j

                if max_len < seq[i]:
                    max_len = seq[i]
                    max_index = i

    result = []
    while max_index != -1:
        result.append(a[max_index])
        max_index = prev[max_index]
    return result[::-1]


if __name__ == "__main__":
    print(longest_increasing_subsequence([2, 3, 1, 4, -1, 5, 6, 0, 2, 3, 4, 5, 6, 7]))
