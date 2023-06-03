import copy
import pprint


def set_num(data, idx):
    if idx >= 81:
        pprint.pprint(data)
        return True
    else:
        # 行:
        # idxが0〜8の場合は0,
        # idxが9〜17の場合は1,
        # ...,
        # idxが72〜80の場合は8,
        # idxが81〜の場合はここには到達しない。
        row = idx // 9
        # 列:
        # idxが0の場合は0,
        # idxが1の場合は1,
        # ...,
        # idxが8の場合は8,
        # idxが9の場合は0。
        # idxが10の場合は1。
        col = idx % 9

        if data[row][col] != 0:
            return set_num(data, idx + 1)
        else:
            virtical = []
            horizontal = []
            for i in range(9):
                virtical.append(data[i][col])
                horizontal.append(data[row][i])

            for number in range(1, 10):
                if number in virtical:
                    continue
                elif number in horizontal:
                    continue
                elif number in numbers_in_3x3(data, col, row):
                    continue
                else:
                    ndata = copy.deepcopy(data)
                    ndata[row][col] = number
                    if set_num(ndata, idx + 1):
                        return True
            return False


def numbers_in_3x3(data, col, row):
    position_3x3_start_col = col // 3 * 3
    position_3x3_start_row = row // 3 * 3
    result = set([])
    for x in range(0, 3):
        for y in range(0, 3):
            x_in_3x3 = position_3x3_start_col + x
            y_in_3x3 = position_3x3_start_row + y
            result.add(data[y_in_3x3][x_in_3x3])

    return result


initial_data = [[0, 0, 0, 0, 2, 0, 0, 0, 0],
                [1, 0, 0, 3, 0, 4, 0, 0, 7],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 4, 0, 1, 0, 8, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 3, 0, 8, 0, 5, 0, 9, 0],
                [0, 9, 7, 0, 0, 0, 5, 1, 0],
                [0, 0, 4, 0, 0, 0, 9, 0, 0],
                [0, 5, 1, 0, 9, 0, 8, 7, 0]]
set_num(initial_data, 0)
