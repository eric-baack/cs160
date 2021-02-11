#!/usr/bin/env python3
"""Using Breadth first search to find Kevin Bacon's number of actors"""

# To build graph, read in list of actors in each movie, and save to list
# For each combination, add edge to graph.  This will create vertex if needed.
# make 'movie' the weight for the edge.  It will be changed into a base10 int
# Track name of movie:  build edges after each change, and after last one.
# Next, use breadth-first-search to find distance from each actor to Kevin Bacon.
# Finally, find any actor, distance to Kevin Bacon, and path working backwards to
# Kevin Bacon, relating movie at each step.
# Perhaps easiest project of semester.

import sys
import time

from pythonds3.graphs import Graph


def read_file(filename):
    """Build a graph from the file"""
    kb_graph = Graph()
    old_movie = ""
    first_movie = True
    v_list = []
    file_read = open(filename, "r")
    first_line = True
    for line in file_read:
        if first_line:
            first_line = False
        else:
            line2 = line.strip()
            act_list = line2.split("|")
            movie = act_list[0]
            actor = act_list[1]
            if first_movie:
                old_movie = movie
                first_movie = False
            if movie != old_movie:
                for actor1 in v_list:
                    for actor2 in v_list:
                        if actor1 != actor2:
                            kb_graph.add_edge(actor1, actor2, movie)
                v_list = []
                old_movie = movie
                v_list.append(actor)
            else:
                v_list.append(actor)
    for actor1 in v_list:  # Needed for the last movie to ensure that edges are added
        for actor2 in v_list:
            if actor1 != actor2:
                kb_graph.add_edge(actor1, actor2, movie)
    return kb_graph


def main():
    print("---Kevin Bacon number calculator---")
    print("\nReading the file")
    b_graph = read_file("data/projects/kevinbacon/movie_actors_full.txt")
    # b_graph = read_file("data/projects/kevinbacon/movie_actors_test.txt")
    # for v in b_graph:
    #   print(f"actor {v.get_key()}")
    kbv = b_graph.get_vertex("Kevin Bacon")
    b_graph.bfs(kbv)
    trace_name = ""
    while trace_name != "exit":
        trace_name = input("What actor would you like to trace? ('exit' to quit) ")
        if trace_name != "exit":
            if not b_graph.get_vertex(trace_name):
                print("I'm sorry, that actor is not the in database")
            else:
                vert = b_graph.get_vertex(trace_name)
                print(
                    f"The Kevin Bacon Number for {trace_name} is {vert.get_distance()}"
                )
                while vert.get_previous():
                    nvert = vert.get_previous()
                    movie = str(nvert.get_neighbor(vert))
                    print(f"{vert.get_key()} acted with {nvert.get_key()} in {movie}")
                    vert = nvert
                print()
    print("Thank you for your interest in movie trivia")


if __name__ == "__main__":
    main()
