def xmas(board, line, col, step_col, step_line):
    for c in "XMAS":
        if len(board) <= line or len(board[line]) <= col or line < 0 or col < 0 or board[line][col] != c:
            return 0
        col += step_col
        line += step_line
    return 1


def part1():
    with open("day4_input.txt") as f:
        board = f.read().splitlines()
    result = 0
    for line, _ in enumerate(board):
        for col, _ in enumerate(board[line]):
            horizontal_right = xmas(board, line, col, 1, 0)
            horizontal_left = xmas(board, line, col, -1, 0)
            vertical_down = xmas(board, line, col, 0, 1)
            vertical_up = xmas(board, line, col, 0, -1)

            diag_right_up = xmas(board, line, col, 1, -1)
            diag_right_down = xmas(board, line, col, 1, 1)
            diag_left_up = xmas(board, line, col, -1, -1)
            diag_left_down = xmas(board, line, col, -1, 1)

            result += horizontal_right
            result += horizontal_left
            result += vertical_down
            result += vertical_up
            result += diag_right_up
            result += diag_right_down
            result += diag_left_up
            result += diag_left_down
    print(result)  # 2462


def part2():
    with open("day4_input.txt") as f:
        board = f.read().splitlines()

    result = 0
    for line in range(1, len(board) - 1):
        for col in range(1, len(board[line]) - 1):
            if board[line][col] != "A":
                continue
            if not (
                (board[line - 1][col - 1] == "M" and board[line + 1][col + 1] == "S")
                or (board[line - 1][col - 1] == "S" and board[line + 1][col + 1] == "M")
            ):
                continue
            if not (
                (board[line - 1][col + 1] == "M" and board[line + 1][col - 1] == "S")
                or (board[line - 1][col + 1] == "S" and board[line + 1][col - 1] == "M")
            ):
                continue
            result += 1

    print(result)


if __name__ == "__main__":
    part1()
    part2()
