from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


# Функция для листания параграфов статьи
def scroll_through_paragraphs(browser):
    paragraphs = browser.find_elements(By.XPATH, "//p")
    for i, paragraph in enumerate(paragraphs):
        print(f"\nПараграф {i + 1}: {paragraph.text[:300]}...")  # Показ первых 300 символов
        user_input = input("Введите 'n' для следующего параграфа, или 'q' чтобы вернуться: ")
        if user_input == 'q':
            break

# Функция для перехода на связанную статью
def go_to_link(browser):
    links = browser.find_elements(By.XPATH, "//div[@id='bodyContent']//a[@href and not(contains(@href, 'Help:')) and not(contains(@href, 'Special:'))]")
    for i, link in enumerate(links[:10]):
        print(f"{i + 1}. {link.text} - {link.get_attribute('href')}")
    choice = input("\nВведите номер ссылки для перехода, или 'q' для выхода: ")

    if choice.isdigit() and 1 <= int(choice) <= 10:
        browser.get(links[int(choice) - 1].get_attribute('href'))
        time.sleep(3)
        scroll_through_paragraphs(browser)

# Основная функция программы
def wikipedia_search():
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org")

    query = input("Введите запрос для поиска на Википедии: ")
    search_box = browser.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.submit()

    time.sleep(3)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        user_choice = input("Введите номер действия: ")

        if user_choice == '1':
            scroll_through_paragraphs(browser)
        elif user_choice == '2':
            go_to_link(browser)
        elif user_choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

    browser.quit()

# Запуск программы
if __name__ == "__main__":
    wikipedia_search()
