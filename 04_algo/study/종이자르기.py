import sys
sys.stdin = open('종이자르기.txt')

V, H = map(int, input().split())
cnt_dot = int(input())
description = [list(map(int, input().split())) for _ in range(cnt_dot)]

ho = []
ver = []
if cnt_dot == 0:
    max_w = V * H
else:
    max_w = -987654322

for i in range(cnt_dot):
    if description[i][0] == 0:
        ho.append(description[i][1])
    elif description[i][0] == 1:
        ver.append(description[i][1])

ho = sorted(ho)
ver = sorted(ver)

if len(ho) != 0 and len(ver) != 0:
    for k in range(len(ho)):
        tmp = 0
        if k == 0:
            a = ho[k]
            for n in range(len(ver)):
                if n == 0:
                    tmp = a * ver[n]
                    if max_w < tmp:
                        max_w = tmp

                if n == len(ver)-1:
                    tmp = (V - ver[n]) * a
                    if max_w < tmp:
                        max_w = tmp

                if 0 < n <= len(ver)-1:
                    tmp = a * (ver[n] - ver[n-1])
                    if max_w < tmp:
                        max_w = tmp

        if k == len(ho)-1:
            a = H - ho[k]
            for n in range(len(ver)):
                if n == 0:
                    tmp = a * ver[n]
                    if max_w < tmp:
                        max_w = tmp

                if n == len(ver) - 1:
                    tmp = (V - ver[n]) * a
                    if max_w < tmp:
                        max_w = tmp

                if 0 < n <= len(ver) - 1:
                    tmp = a * (ver[n] - ver[n - 1])
                    if max_w < tmp:
                        max_w = tmp

        if 0 < k <= len(ho)-1:
            a = ho[k] - ho[k-1]
            for n in range(len(ver)):
                if n == 0:
                    tmp = a * ver[n]
                    if max_w < tmp:
                        max_w = tmp

                if n == len(ver) - 1:
                    tmp = (V - ver[n]) * a
                    if max_w < tmp:
                        max_w = tmp

                if 0 < n <= len(ver) - 1:
                    tmp = a * (ver[n] - ver[n - 1])
                    if max_w < tmp:
                        max_w = tmp

elif len(ho) == 0 and len(ver) != 0:
    for q in range(len(ver)):
        if q == 0:
            tmp = ver[q] * H
            if max_w < tmp:
                max_w = tmp
        if q == len(ver)-1:
            tmp = H * (V-ver[q])
            if max_w < tmp:
                max_w = tmp
        if 0 < q <= len(ver)-1:
            tmp = H * (ver[q] - ver[q-1])

elif len(ho) != 0 and len(ver) == 0:
    for q in range(len(ho)):
        if q == 0:
            tmp = ho[q] * V
            if max_w < tmp:
                max_w = tmp
        if q == len(ho)-1:
            tmp = V * (H-ho[q])
            if max_w < tmp:
                max_w = tmp
        if 0 < q <= len(ho)-1:
            tmp = V * (ho[q] - ho[q-1])

print(max_w)