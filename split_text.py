from functools import lru_cache

# given a text without spaces and dictionary of words.
# compute split of the text.


def compute_split_rec(text, words):
    @lru_cache
    def util(t):
        if t == "":
            return []

        for w in words:
            if t.startswith(w):
                partial_split = util(t[len(w):])
                if partial_split is not None:
                    return partial_split + [w]
        return None

    return util(text)


def compute_split_bfs(text, words):
    split = {"": []}
    q = [""]
    while q:
        prefix = q.pop()
        if prefix == text:
            return split[prefix]
        for w in words:
            if text[len(prefix):].startswith(w):
                split[prefix + w] = split[prefix] + [w]
                q.append(prefix + w)
    return None


if __name__ == "__main__":
    words = {"cat", "cats", "seat", "eat", "mice"}
    text = "catseatmice"
    print(compute_split_rec(text, words))
    print(compute_split_bfs(text, words))
