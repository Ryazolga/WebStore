import time

def test_add_to_cart_button(browser):
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link1)
    time.sleep(30)
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket"), "Button not found"
