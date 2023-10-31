from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.NAME, "field-keywords")
    GO_BUTTON = (By.CLASS_NAME, "nav-search-submit")
    ACCOUNT_LINK = (By.LINK_TEXT, "Your Account")
    HELP_LINK = (By.LINK_TEXT, "Help")
    CART_LINK = (By.LINK_TEXT, "Cart")
    HEADER_LINKS = (By.CSS_SELECTOR, "div[class='nav-bb-right']>a")
    FOOTER_LINKS = (By.CSS_SELECTOR, "a[class='nav_a']")

    #
    DROPDOWN_BOX_LINK = (By.ID, "searchDropdownBox")
    RESULT_FIELD = ()
    ALL_LINK = (By.ID, "nav-hamburger-menu")
    BACK_TO_TOP_LINK = (By.ID, "navBackToTop")
