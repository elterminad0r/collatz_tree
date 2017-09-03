#coding: utf-8

import argparse
import itertools

def get_args():
    parser = argparse.ArgumentParser("generate collatz tree")
    parser.add_argument("-s", "--spacing", type=int, default=1, help="visual tree spacing")
    parser.add_argument("-m", "--max-value", type=int, default=100, help="max value to recurse up to")
    return parser.parse_args()

hor_s = "─"
ver_s = "│"
cross = "┼"
l_t_j = "├"
r_t_j = "┤"
t_t_j = "┬"
b_t_j = "┴"
tl_co = "┌"
bl_co = "└"
tr_co = "┐"
br_co = "┘"

def tree_str(t):
    if t:
        return str(t)
    return ""

class PartialCollatz(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "PartialCollatz({})".format(self.value)

    def __str__(self):
        return "{}...".format(self.value)

class CollatzTree(object):
    def __init__(self, value, k, m, spacing=1):
        self.spacing = spacing
        self.value = value
        self.k = k
        self.m = m

    @staticmethod
    def generative_tree(value, max_value, spacing=1):
        if value > max_value:
            return PartialCollatz(value)
        k = CollatzTree.generative_tree(value * 2, max_value, spacing)
        m = r_t_j
        if value % 6 == 4:
            m = CollatzTree.generative_tree((value - 1) // 3, max_value, spacing)
        return CollatzTree(value, k, m, spacing)

    @staticmethod
    def start_tree(max_value, spacing):
        return CollatzTree(1, CollatzTree(2, CollatzTree(4, CollatzTree.generative_tree(8, max_value, spacing),
                                                            PartialCollatz(1),
                                                            spacing),
                                             None, spacing),
                              None, spacing)

    def __repr__(self):
        return "CollatzTree(value={0.value!r}, k={0.k!r}, m={0.m!r})".format(self)
        
    def __str__(self):
        k_formatted = l_t_j + hor_s * (self.spacing - 1) + tree_str(self.k).replace("\n", "\n{ver_s}".format(ver_s=ver_s + " " * (self.spacing - 1)))
        m_formatted = bl_co + hor_s * (self.spacing - 1) +  tree_str(self.m).replace("\n", "\n{}".format(" " * self.spacing))
        return "{self.value}\n{k_formatted}\n{m_formatted}".format(**locals())

def main():
    args = get_args()
    print(CollatzTree.start_tree(args.max_value, spacing=args.spacing))

if __name__ == "__main__":
    main()
