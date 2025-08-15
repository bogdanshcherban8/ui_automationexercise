from enum import Enum


class AllureFeature(str, Enum):
    API_CASES = "API cases"
    AUTHENTICATION = "Authentication"
    BRANDS = "Brands"
    BREADCRUMB = "Breadcrumb"
    CAROUSEL = "Carousel"
    CATEGORY = "Category"
    CHOSEN_CATEGORY = "Chosen category"
    CONTACT_US = "Contact us"
    CURRENT_ITEM = "Current item"
    LOWER_PANEL = "Lower panel"
    NAVBAR = "Navbar"
    RECOMMENDED_ITEMS = "Recommended items"
    SCROLL_UP = "Scroll up"
    SEARCH_PRODUCTS = "Search products"