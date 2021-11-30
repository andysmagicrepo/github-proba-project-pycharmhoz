# ## 2 Feladat: Kártya
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a kártyakeverés app-ot az [https://wonderful-pond-0d96a8503.azurestaticapps.net/f2.html](https://wonderful-pond-0d96a8503.azurestaticapps.net/f2.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a kártyakeverő app tesztelését.
#
# Az alkalmazás akkor működik helyesen ha 52 gombnyomásból legalább van 4db 9-es szám. Ezt kell ellenőrizned.
#
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!
#
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `feladat2.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# * majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
# * ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
# * akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# * a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
# * nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://wonderful-pond-0d96a8503.azurestaticapps.net/f2.html"

driver.get(URL)


def find_all_cards():
    return driver.find_elements_by_xpath('//div[@class="card"]')


test_data = [(True, ), (0, ), (52, "9", 4)]

submit_button = driver.find_element_by_id("submit")
card_list = find_all_cards()


def test_initial_submit_enabled():
    assert submit_button.is_enabled() == test_data[0][0]


def test_initial_card_list_empty():
    assert len(card_list) == test_data[1][0]


def test_proper_card_deck():
    for _ in range(test_data[2][0]):
        submit_button.click()
    current_card_list = find_all_cards()
    niners = 0
    for card in current_card_list:
        if test_data[2][1] in card.text:
            niners += 1

    assert niners == test_data[2][2]


test_initial_submit_enabled()
test_initial_card_list_empty()
test_proper_card_deck()
