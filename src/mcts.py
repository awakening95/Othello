import numpy as np
import random
from src.processing import *
from datetime import datetime
from multiprocessing import Process, Queue


def multi_process_mcts(board, depth, my_stone_color, opponent_stone_color, available_position, q):
    time_first = datetime.now()

    first_choice_list = [[], [], [], []]  # 위치, 승, 패, 승률

    for x, y in available_position:
        first_choice_list[0].append([x, y])  # 위치
        first_choice_list[1].append(0)  # 승
        first_choice_list[2].append(0)  # 패
        first_choice_list[3].append(0)  # 승률

    time_spent = (datetime.now() - time_first).seconds
    while time_spent < 25:  # 반복 시간으로 정하자
        deep_copy_board = np.copy(board)

        first_choice, result = mcts(deep_copy_board, depth, my_stone_color, opponent_stone_color)

        if result == 1:  # 승리
            first_choice_list[1][first_choice_list[0].index(first_choice)] += 1
        elif result == -1:  # 패배
            first_choice_list[2][first_choice_list[0].index(first_choice)] += 1
        else:
            pass

        time_spent = (datetime.now() - time_first).seconds

    print(first_choice_list)
    q.put(first_choice_list)


def get_good_position(board, depth, my_stone_color, opponent_stone_color):
    q = Queue()
    available_position = get_available_position(board, my_stone_color)
    procs = []

    for _ in range(6):
        proc = Process(target=multi_process_mcts,
                       args=(board, depth, my_stone_color, opponent_stone_color, available_position, q))
        procs.append(proc)
        proc.start()

    first_choice_list = [[], [], [], []]  # 위치, 승, 패, 승률

    for x, y in available_position:
        first_choice_list[0].append([x, y])  # 위치
        first_choice_list[1].append(0)  # 승
        first_choice_list[2].append(0)  # 패
        first_choice_list[3].append(0)  # 승률

    first_choice_list = np.array(first_choice_list)

    for _ in range(6):
        result = q.get()
        result = np.array(result)
        first_choice_list[1] += result[1]
        first_choice_list[2] += result[2]

    for proc in procs:
        proc.join()

    for i in range(len(available_position)):
        try:
            first_choice_list[3][i] = first_choice_list[1][i] / (first_choice_list[1][i] + first_choice_list[2][i])
        except ZeroDivisionError:
            pass
        print(first_choice_list[0][i], "win rate is", first_choice_list[3][i], ", numbers:",
              (first_choice_list[1][i] + first_choice_list[2][i]))

    best_position = first_choice_list[0][first_choice_list[3].tolist().index(max(first_choice_list[3]))]

    return best_position


def mcts(board, depth, my_stone_color, opponent_stone_color):
    available_position = get_available_position(board, my_stone_color)
    first_choice = random.choice(available_position)
    changed_points = get_reversed_position(board, my_stone_color, first_choice[0], first_choice[1])

    for i, j in changed_points:
        board[i][j] = my_stone_color
    board[first_choice[0]][first_choice[1]] = my_stone_color

    depth -= 1
    my_turn = False

    while depth != 0:
        if my_turn is True:
            available_position = get_available_position(board, my_stone_color)
        else:
            available_position = get_available_position(board, opponent_stone_color)

        if not available_position:  # 어떤 플레이어가 돌을 둘 수가 없으면 PASS, 다른 플레이어 차례
            # print("PASS")
            if my_turn is True:
                my_turn = False
                available_position = get_available_position(board, opponent_stone_color)  # 다른 플레이어가 돌을 둘 수 있는 곳
                if not available_position:  # 둘다 PASS면
                    # print("ALL PASS")
                    # print(board)
                    break  # 내가 결과적으로 얻을 수 있는 돌 반환
            else:
                my_turn = True
                available_position = get_available_position(board, my_stone_color)
                if not available_position:
                    # print("ALL PASS")
                    # print(board)
                    break

        if my_turn:
            choice = random.choice(available_position)
            changed_points = get_reversed_position(board, my_stone_color, choice[0], choice[1])

            for i, j in changed_points:
                board[i][j] = my_stone_color
            board[choice[0]][choice[1]] = my_stone_color

            depth -= 1
            my_turn = False

        else:
            choice = random.choice(available_position)
            changed_points = get_reversed_position(board, opponent_stone_color, choice[0], choice[1])

            for i, j in changed_points:
                board[i][j] = opponent_stone_color
            board[choice[0]][choice[1]] = opponent_stone_color

            depth -= 1
            my_turn = True

    sum_my_stone = len(np.where(board == my_stone_color)[0])

    if sum_my_stone > 32:  # 승리
        return first_choice, 1
    elif sum_my_stone <= 32:  # 패배
        return first_choice, -1
    else:  # 무승부
        return first_choice, 0
