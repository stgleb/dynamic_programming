from functools import lru_cache


class Node(object):
    def __init__(self, left, right):
        self.val = -1
        self.left = left
        self.right = right


def count_binary_trees(n):
    @lru_cache()
    def util(n):
        if n == 0:
            return 1

        total = 0
        for i in range(n):
            num_left = util(i)
            num_right = util(n - i - 1)
            total += num_left * num_right
        return total
    
    return util(n)


def generate_binary_trees(n):
    if n == 0:
        return [None]

    trees = []
    for i in range(n):
        trees_left = generate_binary_trees(i)
        trees_right = generate_binary_trees(n - i - 1)

        for l in trees_left:
            for r in trees_right:
                trees.append(Node(l, r))
    return trees


if __name__ == "__main__":
    print(count_binary_trees(5))
    print(len(generate_binary_trees(5)))
