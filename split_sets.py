from functools import lru_cache


# Given a set of numbers, split them in two subsets
# so sum of them are equal.


def split_sets(values):
    @lru_cache()
    def util(index, target):
        if target == 0:
            return True
        if index == len(values):
            return False
        return util(index + 1, target) or util(index + 1, target - values[index])
    total = sum(values)
    if total % 2:
        return None
    return util(0, total // 2)


def find_split(values):
    @lru_cache()
    def util(index, target):
        if target == 0:
            return []
        if index == len(values):
            return None
        result = None
        not_take = util(index + 1, target)
        if not_take is not None:
            result = not_take

        take = util(index + 1, target - values[index])
        if take is not None:
            result = take + [values[index]]
        return result
    total = sum(values)
    if total % 2:
        return None
    return util(0, total // 2)


if __name__ == "__main__":
    print(split_sets([2, 3, 5, 6]))
    print(split_sets([7, 8, 1, 3, 2, 4, 5]))

    print(find_split([2, 3, 5, 6]))
    print(find_split([7, 8, 1, 3, 2, 4, 5]))

