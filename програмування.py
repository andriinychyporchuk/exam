def search_paragraphs(file_path, keyword):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            paragraphs = file.read().split('\n\n')                             
            for i, paragraph in enumerate(paragraphs, start=1):
                if keyword.lower() in paragraph.lower():
                    print(f"Абзац {i}:\n{paragraph}\n{'='*30}")
            if all(keyword.lower() not in paragraph.lower() for paragraph in paragraphs):
                print(f"Слово '{keyword}' не знайдено")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")

def main():
    while True:
        print("1. Шукати слово")
        print("2. Вихід")
        
        choice = input("Виберіть опцію: ")

        if choice == '1':
            file_path = input("Введіть шлях до файлу: ")
            keyword = input("Введіть слово для пошуку: ")
            search_paragraphs(file_path, keyword)
        elif choice == '2':
            break
        else:
            print("Неправильний вибір. ")

if __name__ == "__main__":
    main()