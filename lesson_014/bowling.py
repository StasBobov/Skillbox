import logging

# '12 X 34 -/ 17 44 X X 23 --'
# result = '1-X349/1744XX23--pppp'


def get_score(game_result):
    total_score = 0
    total_frames = 0
    frame = ""
    for i in game_result:
        if frame == "":
            if i.isdigit():
                frame = i
            elif i == "X":
                total_score += count_points(i)
                total_frames += 1
            elif i == "-":
                frame = i
            else:
                raise Exception("Invalid incoming data %s", i)
        elif frame.isdigit() or frame == "-":
            if i.isdigit():
                frame += i
                total_score += count_points(frame)
                total_frames += 1
                frame = ""
            elif i == '/':
                frame += i
                total_score += count_points(frame)
                total_frames += 1
                frame = ""
            elif i == "-":
                frame += i
                total_score += count_points(frame)
                total_frames += 1
                frame = ""
            else:
                raise Exception("Invalid incoming data")
    if frame != "":
        raise Exception("Invalid incoming data")
    if total_frames != 10:
        raise RuntimeError("Not 10 frames given")
    return total_score


def count_points(res):
    logging.debug(f"{res}")
    if res.isdigit():
        return currect_digit(res)
    elif res == "X":
        return 20
    elif res == "--":
        return 0
    elif res[1] == "/":
        return 15
    elif res[0] == '-':
        return int(res[1])
    elif res[1] == '-':
        return int(res[0])



def currect_digit(digit):
    first = int(digit[0])
    second = int(digit[1])
    if (first + second) > 9:
        raise Exception("Invalid incoming data")
    elif first <= 0 or second <= 0:
        raise Exception("Invalid incoming data")
    else:
        return first + second



logging.basicConfig(level=logging.DEBUG)
# try:
#     get_score(result)
# except Exception as arr:
#     print(f"Поймал {arr}")
