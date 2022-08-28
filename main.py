import time
from typing import Any


def fibonacci(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """

    assert type(num) == int
    assert num > 0

    if num <= 2:
        return num - 1
    prev = 0
    result = 1
    for i in range(2, num):
        result, prev = result + prev, result
    return result


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """

    if __is_not_square_matrix(matrix):
        raise Exception("The parameter value is not a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    row_idx = __choose_row(matrix)
    result = 0
    for column_idx, value in enumerate(matrix[row_idx]):
        if value != 0:
            result += value * __co_factor(matrix, row_idx, column_idx)
    return result


def __is_not_square_matrix(matrix: [[int]]) -> bool:
    if type(matrix) != list or not matrix or type(matrix[0]) != list:
        return True
    first_row_len = len(matrix[0])
    if first_row_len != len(matrix):
        return True
    for row in matrix:
        if type(row) != list or len(row) != first_row_len:
            return True
    return False


def __choose_row(matrix: [[int]]) -> int:
    max_zero_cnt = 0
    target_row_idx = 0
    for idx, row in enumerate(matrix):
        zero_cnt = 0
        for value in row:
            zero_cnt += bool(value == 0)
        target_row_idx = idx if zero_cnt > max_zero_cnt else target_row_idx
        max_zero_cnt = max(zero_cnt, max_zero_cnt)
    return target_row_idx


def __co_factor(matrix: [[int]], row_idx: int, column_idx: int) -> int:
    if len(matrix) < 2:
        raise Exception("Can't calculate co_factor for if matrix order is less"
                        "than 2")
    reduced_matrix = [[val for idx, val in enumerate(row) if idx != column_idx]
                      for idx, row in enumerate(matrix) if idx != row_idx]
    i = row_idx + 1
    j = column_idx + 1
    return (-1) ** (i + j) * determinant(reduced_matrix)


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def main():
    for num in [10, 20, 30, 35]:
        print_exec_time(lambda x: print(x, fibonacci(x)), x=num)

    matrix = [[1, 2],
              [3, 4]]
    print(f'determinant: {determinant(matrix)}')


if __name__ == '__main__':
    main()
