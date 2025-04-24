import time
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_check_lang_btn(browser,request):
    language = request.config.getoption("language")
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    btn = browser.find_element(By.XPATH,"//button[contains(@class, 'btn-add-to-basket') and contains(@class, 'btn-primary')]")
    expected_text = {
        "en": "Add to basket",
        "fr": "Ajouter au panier",
        "es": "Añadir al carrito",
        "ru": "Добавить в корзину"
    }

    assert btn.text == expected_text[language], \
        f"Expected '{expected_text[language]}' but got '{btn.text}'"