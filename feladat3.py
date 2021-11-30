from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://wonderful-pond-0d96a8503.azurestaticapps.net/f3.html"

driver.get(URL)

op1 = driver.find_element_by_id("op1")
op2 = driver.find_element_by_id("op2")
num1 = driver.find_element_by_id("num1")
num2 = driver.find_element_by_id("num2")
num3 = driver.find_element_by_id("num3")
submit_button = driver.find_element_by_id("submit")


def assemble_expression(*args):
    return "{}{}{}{}{}".format(*args)


def test_evaluate_expression():
    submit_button.click()
    result_text = driver.find_element_by_id("result")
    ex = assemble_expression(num1.text, op1.text, num2.text, op2.text, num3.text)
    assert eval(ex) == int(result_text.text)

test_evaluate_expression()
