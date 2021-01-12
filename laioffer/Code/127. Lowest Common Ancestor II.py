# Definition for a binary tree node with parent pointer.
class TreeNodeP(object):
    def __init__(self, x, p):
        self.value = x
        self.left = None
        self.right = None
        self.parent = p


class Solution(object):
    def lowestCommonAncestor(self, one, two):
        """
        input: TreeNodeP one, TreeNodeP two
        return: TreeNodeP
        """
        # write your solution here
        lst_one = []
        lst_two = []

        while one.parent:
            lst_one.append(one.parent.value)
            one = one.parent

        while two.parent:
            lst_two.append(two.parent.value)
            two = two.parent
        print(lst_one, lst_two)

        if len(lst_one) > len(lst_two):
            lst_one, lst_two = lst_two, lst_one

        res = None
        while len(lst_one) != 0 and len(lst_two) != 0:
            a = lst_one.pop()
            b = lst_two.pop()

            if a != b:
                return res
            else:
                res = a

        return res


n3 = TreeNodeP(3, None)
n5 = TreeNodeP(5, n3)
n1 = TreeNodeP(1, n3)
n3.left = n5
n3.right = n1

n6 = TreeNodeP(6, n5)
n2 = TreeNodeP(2, n5)
n5.left = n6
n5.right = n2

n7 = TreeNodeP(7, n2)
n4 = TreeNodeP(4, n2)
n2.left = n7
n2.right = n4

n0 = TreeNodeP(0, n1)
n8 = TreeNodeP(8, n1)
n1.left = n0
n1.right = n8

print(Solution().lowestCommonAncestor(n6, n7))
