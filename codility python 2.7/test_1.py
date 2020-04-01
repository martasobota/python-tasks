# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")
import sys

def solution(N):
    for i in range(N):
        sys.stdout.write(N * 'L') if i == N-1 else sys.stdout.write('L\n')
