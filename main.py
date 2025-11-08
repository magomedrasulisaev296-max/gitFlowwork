# функция для выдачи словаря в зависимости от уровня сложности
def choose_difficulty(diffucult:str) -> dict:
    words_easy = {
        "family": "семья",
        "hand": "рука",
        "people": "люди",
        "evening": "вечер",
        "minute": "минута",
    }
    words_medium = {
        "believe": "верить",
        "feel": "чувствовать",
        "make": "делать",
        "open": "открывать",
        "think": "думать",
    }
    words_hard = {
        "rural": "деревенский",
        "fortune": "удача",
        "exercise": "упражнение",
        "suggest": "предлагать",
        "except": "кроме",
    }
    if diffucult == "легкий":
        return words_easy
    elif diffucult == "сложный":
        return words_hard
    else:
        return words_medium


levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# начало теста запрашиваем сложность
print("Привет, давай проверм твой английский!")
test_diffucult = input("Выбери уровень сложности(легкий, средний или сложный):").lower()

# получаем словарь
questions_and_answers = choose_difficulty(test_diffucult)


# создаем основную логику игры
def play_game(questions_and_answers:dict) -> int:
    answers = list(questions_and_answers.values())
    questions = list(questions_and_answers.keys())
    right_answers = 0
    for i in range(0, 5):
        word = answers[i]
        print(f"{questions[i]}, {len(answers[i])} букв, начинается на {word[0]}...")
        user_input = input("ваш ответ?:")
        if user_input == answers[i]:
            right_answers += 1
            print("молодец!")
        else:
            print(f"в следующий раз получится! ответ был({answers[i]})")
    return right_answers


right_answers = play_game(questions_and_answers)

# выводим ранг пользователя
print("пора узнать результаты!")


def calculate_rank(levels:dict) -> int:
    rank = 0
    if right_answers >= 0:
        rank = levels[right_answers]
    return rank


def display_results(rank:int) -> None:
    print(rank)


rank = calculate_rank(levels)
display_results(rank)
