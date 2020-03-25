#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    @functools.wraps(func)
    def inner(*args,**kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        output = func(*args,**kwargs)
        profiler.disable()
        ps = pstats.Stats(profiler).strip_dirs().sort_stats('cumulative')
        ps.print_stats(5)
        return output
    return inner


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    return title in movies

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    t = timeit.Timer(
        stmt='find_duplicate_movies("movies.txt")',
        setup='from __main__ import find_duplicate_movies'
        )
    runs = 3
    repeat_num = 7
    results = t.repeat(repeat=repeat_num, number=runs)
    min_time = min(results) / float(runs)
    print('best time: ' + str(min_time))


def main():
    # timeit_helper()
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
