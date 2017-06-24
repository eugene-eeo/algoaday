from collections import namedtuple
import random



class Node:
    __slots__ = ('data', 'left', 'right')

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self, k=0):
        indent = ('  ' * k)
        u = [indent + 'Node(%r)' % (self.data,)]
        if self.left:
            u.append(self.left.__repr__(k+1))
        if self.right:
            u.append(self.right.__repr__(k+1))
        return '\n'.join(k for k in u)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data == other.data and \
                self.left == other.left and \
                self.right == other.right


#Node = namedtuple('Node', 'data,left,right')


def graph(node):
    a = ['digraph BST {']
    u = lambda n, v: a.append('"%s" -> "%s"' % (n, v))
    def g(node):
        if node.left:
            u(node.data, node.left.data)
            g(node.left)
        if node.right:
            u(node.data, node.right.data)
            g(node.right)
    g(node)
    a.append('}')
    return '\n'.join(a)


def mknode(data, left=None, right=None):
    return Node(data, left, right)


def preorder(t):
    if t is not None:
        yield t.data
        yield from preorder(t.left)
        yield from preorder(t.right)


def postorder(t):
    if t is not None:
        yield from postorder(t.left)
        yield from postorder(t.right)
        yield t.data


def inorder(t):
    if t is not None:
        yield from inorder(t.left)
        yield t.data
        yield from inorder(t.right)


def full_pp(pre, post):
    root, *pre  = pre
    *post, root = post
    if not pre:
        return mknode(root)

    left  = pre[0]
    right = post[-1]
    L = post.index(left)
    R = pre.index(right)

    return mknode(
            root,
            full_pp(pre[:R], post[:L+1]),
            full_pp(pre[R:], post[L+1:]),
            )


def min_index(target, a, b):
    b = b[b.index(target)+1:]
    for item in a:
        if item in b:
            return item


def full_pi(pre, inord):
    root, *pre = pre
    if not pre:
        return mknode(root)
    left  = pre[0]
    right = min_index(root, pre, inord)
    R = pre.index(right)
    T = inord.index(root)
    return mknode(
            root,
            full_pi(pre[:R], inord[:T]),
            full_pi(pre[R:], inord[T+1:]),
            )


def inc_uid():
    a = [0]
    def inc(a=a):
        a[0] += 1
        return a[0]
    def peek(a=a):
        return a[0]
    return inc, peek


def rand_tree(p=0.5, maxdepth=5):
    inc, peek = inc_uid()
    root = mknode(inc())
    q = [root]
    while q:
        node = q.pop()
        if len(q) >= maxdepth:
            continue
        if random.random() < p:
            node.left = mknode(inc())
            node.right = mknode(inc())
            q.append(node.left)
            q.append(node.right)
    return root


if __name__ == '__main__':
    for i in range(100):
        t = rand_tree()
        pre   = list(preorder(t))
        post  = list(postorder(t))
        inord = list(inorder(t))
        assert full_pp(pre, post) == t
        assert full_pi(pre, inord) == t
