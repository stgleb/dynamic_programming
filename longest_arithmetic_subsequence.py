def longest_arithmetic_subsequence(a):
    n = len(a)
    subseq_len = [{} for _ in range(n)]
    best_len = 0
    best_index = 0
    best_step = 0
    for i, v in enumerate(a):
        for j in range(i):
            step = v - a[j]
            prev_len = subseq_len[j].get(step, 1)
            if subseq_len[i].get(step, 1) < prev_len + 1:
                subseq_len[i][step] = prev_len + 1

            if subseq_len[i].get(step, 1) > best_len:
                best_len = subseq_len[i].get(step, 1)
                best_index = i
                best_step = step
    result = []
    prev = a[best_index]
    result.append(prev)
    for i in reversed(range(best_index)):
        if prev - a[i] == best_step:
            result.append(a[i])
            prev = a[i]

    return result[::-1]


if __name__ == "__main__":
    print(longest_arithmetic_subsequence([1, 2, 4, 5, -1, 6, 8, 0, 10]))
