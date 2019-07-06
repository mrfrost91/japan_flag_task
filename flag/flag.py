import sys
import argparse


def check_even(N):
    N = int(sys.argv[1])
    if N < 1 or N % 2 != 0:
        raise argparse.ArgumentError()


parser = argparse.ArgumentParser()
parser.add_argument("N", type=check_even, help='an even integer number')
args = parser.parse_args()


def flag(N):
    N = int(N)
    width = N * 3
    height = N * 2
    v_dist = N / 2
    offset = 0
    result = []
    border = ['#\n' if x == width + 1 else '#' for x in range(width + 2)]
    border = ''.join(border)
    for i in range(height):
        result.append('#')
        for j in range(width):
            if (i >= v_dist and i <= height - v_dist - 1) and (
                    j == N + v_dist + offset or j == N + v_dist - 1 - offset):
                result.append('*')
            elif (i >= v_dist and i <= height - v_dist - 1) and (
                    j < N + v_dist + offset and j > N + v_dist - 1 - offset):
                result.append('o')
            else:
                result.append(' ')
        if i >= v_dist and i < v_dist * 2 - 1:
            offset += 1
        elif i > v_dist * 2 - 1 and i < height - v_dist - 1:
            offset -= 1
        result.append('#\n')
    result = ''.join(result)
    result = border + result + border
    return result


if __name__ == '__main__':
    flag(sys.argv[1])
