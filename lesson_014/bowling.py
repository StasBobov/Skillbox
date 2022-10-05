import logging

# '12 X 34 -/ 17 44 X X 23 --'
result = '12X34-/1744XX23--'


def get_score(game_result):
    total_score = 0
    total_frames = 0
    frame = ""
    for i in game_result:
        if frame == "":
            logging.debug(f"Фрейм {total_frames} - первый бросок.")
            if i.isdigit():
                logging.info(f"Фрейм {total_frames}, с первого броска выбил: {i}.")
                frame = i
            elif i == "X":
                logging.info(f"Фрейм {total_frames} - Strike!")
                total_score += count_points(i)
                total_frames += 1
            elif i == "-":
                logging.info(f"Фрейм {total_frames} - первый нах.")
                frame = i
        elif frame.isdigit() or frame == "-":
            logging.debug(f"Фрейм {total_frames} - второй бросок.")
            if i.isdigit():
                logging.info(f"Фрейм {total_frames} со второго броска выбил: {i}.")
                frame += i
                total_score += count_points(frame)
                total_frames += 1
                frame = ""
            elif i == '/':
                logging.info(f"Фрейм {total_frames} - Spare!")
                frame += i
                total_score += count_points(frame)
                total_frames += 1
                frame = ""
            elif i == "-":
                logging.info(f"Фрейм {total_frames} - второй нах.")
                frame += i
                total_score += count_points(frame)
                total_frames += 1
                frame = ""
    if total_frames != 10:
        raise RuntimeError
    return total_score


def count_points(res):
    if res.isdigit():
        return int(res[0]) + int(res[1])
    elif res == "X":
        return 20
    elif res == "--":
        return 0
    elif res[1] == "/":
        return 15





# logging.basicConfig(level=logging.DEBUG)
try:
    get_score(result)
except Exception as arr:
    print(f"Поймал {arr}")