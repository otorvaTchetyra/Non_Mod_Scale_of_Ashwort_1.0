def get_score(description):
    while True:
        try:
            score = int(input(f"{description} (0-4): "))
            if 0 <= score <= 4:
                return score
            else:
                print("Введите число от 0 до 4.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def main():
    print("Оценка мышечного тонуса по шкале Эшфорта")
    
    scores = []
    joint_descriptions = [
        "Оцените тонус в плечевом суставе",
        "Оцените тонус в локтевом суставе",
        "Оцените тонус в запястье",
        "Оцените тонус в тазобедренном суставе",
        "Оцените тонус в коленном суставе",
        "Оцените тонус в голеностопном суставе"
    ]
    
    for description in joint_descriptions:
        score = get_score(description)
        scores.append(score)
    
    total_score = sum(scores)
    average_score = total_score / len(scores)
    
    print(f"\nИтоговая оценка тонуса: {total_score}")
    print(f"Средний балл: {average_score:.2f}")
    
    if average_score == 0:
        print("Нормальный тонус.")
    elif average_score <= 1:
        print("Легкое увеличение тонуса.")
    elif average_score <= 2:
        print("Выраженное увеличение тонуса.")
    elif average_score <= 3:
        print("Значительное увеличение тонуса.")
    else:
        print("Очень высокий тонус.")

if __name__ == "__main__":
    main()