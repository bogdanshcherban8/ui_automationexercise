from enum import Enum


class AllureStory(str, Enum):
    API_TESTING = "API cases"
    TEST_CASES = "Test cases"
    SIGNUP = "Signup"
    LOGIN = "Login"
    BRANDS = "Brands"
    BREADCRUMB = "Breadcrumb"
    CAROUSEL = "Carousel"
    CATEGORY = "Category"
    CHOSEN_CATEGORY = "Chosen category"
    CHOSEN_BRAND = "Chosen brand"
    CONTACT_US = "Contact us"
    CURRENT_ITEM = "Current item"
    LOWER_PANEL = "Lower panel"
    NAVBAR = "Navbar"
    RECOMMENDED_ITEMS = "Recommended items"
    SCROLL_UP = "Scroll up"
    SEARCH_PRODUCTS = "Search products"