#!/usr/bin/env python3

# Project Euler: problem 107
# https://projecteuler.net/problem=107

# Summary: build a minumum spanning tree using Prim's algorithm

import heapq

if __name__ == "__main__":
    fname = "p107_network.txt"
    f = open(fname, 'r')
    lines = [map(lambda x: 0 if x == '-' else int(x),x.strip().split(',')) for x in f.readlines()]

    cost = 0
    mst = {0}
    edges = set()
    for x in xrange(len(lines)):
        for y in xrange(len(lines)):
            if lines[x][y] != 0:
                edges.add((x,y,lines[x][y]))
    orig_cost = sum(sum(lines, []))/2

    while(len(mst) != len(lines)):
        relevant_edges = filter(lambda x: (x[0] not in mst and x[1] in mst) or\
                                (x[1] not in mst and x[0] in mst), edges.copy())
        edge = min(relevant_edges, key=lambda x: x[2])
        x, y, weight = edge
        for i in [x,y]: mst.add(i)
        cost += weight

    print "orig", orig_cost
    print "new", cost

    print orig_cost - cost
