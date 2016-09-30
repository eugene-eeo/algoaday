from pylev import levenshtein
from pprint import pformat


class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def insert(self, string):
        dist = levenshtein(string, self.value)
        if dist not in self.children:
            self.children[dist] = Node(string)
            return
        self.children[dist].insert(string)

    def search(self, query, threshold):
        d = levenshtein(self.value, query)
        if d <= threshold:
            yield self.value

        lo = d - threshold
        hi = d + threshold

        for dist, node in self.children.items():
            if lo <= dist <= hi:
                for rv in node.search(query, threshold):
                    yield rv

    @classmethod
    def from_sequence(cls, data):
        data = iter(data)
        root = cls(next(data))
        for word in data:
            root.insert(word)
        return root


if __name__ == '__main__':
    words = ["abc", "abba", "abra", "different", "totally"]
    tree = Node.from_sequence(words)
    for n in range(1, 5):
        for word in words:
            assert set(tree.search(word, n)) == set([
                w for w in words if levenshtein(w, word) <= n
            ])
