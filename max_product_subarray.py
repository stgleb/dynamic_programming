def max_product_subarray(a):
    def max_product_subarray(values):
        max_product = 0
        product = 1
        for v in values:
            product *= v
            if not product:
                product = 1
            else:
                max_product = max(max_product, product)
        return max_product

    return max(max_product_subarray(a), max_product_subarray(a[::-1]))


if __name__ == "__main__":
    print(max_product_subarray([-5, -6, -7, -8]))
    print(max_product_subarray([-5, 3, 7, 8, 0, -6, 1, -8]))
    print(max_product_subarray([11, 17, 0, -2, 4, 9, 8]))
    print(max_product_subarray([1, -2, -3, 0, 7, -8, -2]))
