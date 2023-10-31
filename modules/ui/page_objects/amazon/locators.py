from re import A
from selenium.webdriver.common.by import By


class MainPageLocators:

    # START PAGE LOCATORS
    LOGO_LINK = (By.ID, "nav-logo-sprites")
    SEARCH_FIELD = (By.NAME, "field-keywords")
    GO_BUTTON = (By.CLASS_NAME, "nav-search-submit")
    ACCOUNT_LIST_LINK = (By.ID, "nav-flyout-accountList")
    HELP_LINK = (By.LINK_TEXT, "Help")
    CART_LINK = (By.LINK_TEXT, "Cart")
    HEADER_LINKS = (By.CSS_SELECTOR, "div[class='nav-bb-right']>a")
    FOOTER_LINKS = (By.CSS_SELECTOR, "a[class='nav_a']")
    DROPDOWN_BOX_LINK = (By.ID, "searchDropdownBox")
    RESULT_FIELD = ()
    ALL_LINK = (By.ID, "nav-hamburger-menu")
    BACK_TO_TOP_LINK = (By.ID, "navBackToTop")
    SIGN_IN_LINK = (By.ID, "nav-link-accountList")

    # LOGIN PAGE LOCATORS
    LOGIN_FIELD = (By.ID, "ap_email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    CONTINUE_BUTTON = (By.ID, "continue")
    SUBMIT_BUTTON = (By.ID, "signInSubmit")
    ALERT_MESSAGE = (By.CSS_SELECTOR, ".a-list-item")
    ALERT_HEADING = (By.CSS_SELECTOR, "#auth-error-message-box > div > h4")
    ALERT_MISSING = (By.CSS_SELECTOR, "#auth-email-missing-alert > div > div")
    NAV_LINKS = (By.CSS_SELECTOR, "#nav-xshop > a")

    # ACCOUNTS AND LISTS LOCATORS BOX
    LISTS_LINKS = (By.CSS_SELECTOR, "#nav-al-wishlist a")
    ACCOUNT_LINKS = (By.CSS_SELECTOR, "#nav-al-your-account a")
    CREATE_LIST_OUTER_LINK = (By.CSS_SELECTOR, "#nav-al-wishlist > a:nth-child(3)")
    CREATE_LIST_INNER_LINK = (By.CLASS_NAME, "a-button-input")
    CREATE_LIST_HEADER = (By.ID, "a-popover-header-1")
    CREATE_LIST_INPUT = (By.ID, "list-name")
    CREATE_LIST_BUTTON = (By.XPATH, "//*[@id='wl-redesigned-create-list']//input")
    SHOPPING_LISTS = (By.CSS_SELECTOR, "#left-nav a")

    # SEARCH PAGE
    FIRST_RESULT = (By.CSS_SELECTOR, "img[data-image-index='1']")
    ADD_TO_LIST_BUTTON = (By.ID, "add-to-wishlist-button-submit")
