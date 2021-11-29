from functools import lru_cache

# Given an integer array, find number of ways
# to calculate a target number using only array
# elements and addition or subtraction operator.


def count_expressions_rec(values, target):
    @lru_cache
    def count(index, partial_value):
        if index == len(values):
            if partial_value == 0:
                return 1
            return 0
        return count(index + 1, partial_value - values[index]) + \
               count(index + 1,  partial_value + values[index])
    return count(0, target)


if __name__ == "__main__":
    print(count_expressions_rec([2], 3))
    print(count_expressions_rec([2], 2))
    print(count_expressions_rec([2, 1, 1], 2))
    print(count_expressions_rec([1, 2, 2, 3, 3], 7))
    print(count_expressions_rec([1, 2, 2, 3, 1], 3))

