N = int(input('Enter an integer even number: '))

def flag(N):
    if N < 1 or N % 2 != 0:
        raise Exception('Please specify an integer even number')
        return 0
    width = N * 3
    height = N * 2
    v_dist = N / 2
    offset = 0
    result = []
    border = []
    for el in range(width + 2):
        if el != width + 1:
            border.append('#')
        else:
            border.append('#\n')
    border = ''.join(border)
    for i in range(height):
        result.append('#')
        for j in range(width):
            if (i >= v_dist and i <= height - v_dist - 1) and (j == width - N - v_dist - 1 - offset or j == N + v_dist + offset):
                result.append('*')
            elif (i >= v_dist and i <= height - v_dist - 1) and (j > width - N - v_dist - 1 - offset and j < N + v_dist + offset):
                result.append('o')
            else:
                result.append(' ')
        result.append('#\n')
        if i >= v_dist and i < v_dist * 2 - 1:
            offset += 1
        elif i > v_dist * 2 - 1:
            offset -= 1
    result = ''.join(result)
    result = border + result + border
    print(result)
if __name__ == '__main__':
    flag(N)