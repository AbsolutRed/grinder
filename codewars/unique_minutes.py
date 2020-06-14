#!/usr/bin/env python3


def get_unique_watched_minutes(data):

    data.sort(key=lambda i: i[0])

    start, end = data[0]
    unique_watch_time = end - start

    for x in range(1, len(data)):
        if data[x][0] < end:
            if data[x][1] > end:
                unique_watch_time += data[x][1] - end
                start, end = data[x][0], data[x][1]
        else:
            unique_watch_time += data[x][1] - data[x][0]
            start, end = data[x][0], data[x][1]
    return unique_watch_time


def sum_of_intervals(intervals):

    r = set()

    for start, stop in intervals:
        for x in range(start, stop):
            r.add(x)
    return len(r)


if __name__ == '__main__':

    times1 = [(1, 10), (13, 18), (15, 23), (21, 26)]
    times2 = [(0, 15), (10, 25), (16, 33), (22, 42), (32, 49), (23, 50)]
    
    for t in times1, times2:
        r1 = get_unique_watched_minutes(data=t)
        r2 = sum_of_intervals(intervals=t)
        assert r1 == r2
