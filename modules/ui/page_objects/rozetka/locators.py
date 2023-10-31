from selenium.webdriver.common.by import By

class BasketPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[name='search']")
    ADD_TO_CART = (By.CSS_SELECTOR, "button[aria-label='Купити']")
    CART_LINK = (By.CSS_SELECTOR, "li[class='header-actions__item header-actions__item--cart']")
    BASKET_HEADING = (By.CSS_SELECTOR, "h3[class='modal__heading']")
    LIST_PRODUCTS = (By.CSS_SELECTOR, "ul[class='cart-list']")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "a[data-testid='title']")
    DISCOUNT_VALUE = (By.CSS_SELECTOR, "span[data-testid='picture-discount']")
    OLD_COST = (By.CSS_SELECTOR, "p[data-testid='old-cost']")
    COST_WITH_DISCOUNT = (By.CSS_SELECTOR, "p[data-testid='cost']")
    MINUS_BUTTON = (By.CSS_SELECTOR, "button[data-testid='cart-counter-decrement-button']")
    PLUS_BUTTON = (By.CSS_SELECTOR, "button[data-testid='cart-counter-increment-button']")
    INPUT_FIELD = (By.CSS_SELECTOR, "input[data-testid='cart-counter-input']")
    TREE_DOTS_BUTTON = (By.ID, "cartProductActions0")
    DELETE_BUTTON = (By.CSS_SELECTOR, "#cartProductActions0 > ul > li:nth-child(1) > rz-trash-icon > button")
    FINAL_PRICE = (By.CSS_SELECTOR, ".cart-receipt__sum-price>span")
    CART_MESSAGE = (By.CSS_SELECTOR, "h4[class='cart-dummy__heading']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".rz-checkout-button a")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "button[data-testid='continue-shopping-link']")