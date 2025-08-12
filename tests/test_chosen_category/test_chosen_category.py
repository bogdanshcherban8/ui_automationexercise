from urllib.parse import urljoin
import allure
import pytest
from config import settings
from pages.products_page.products_page import ProductsPage

category_data = [
    ("women_category_button", "women_dress_button", "Women - Dress Products", "Sleeveless Dress",
     "category_products/1"),
    ("women_category_button", "women_tops_button", "Women - Tops Products", "Blue Top", "category_products/2"),
    ("women_category_button", "women_saree_button", "Women - Saree Products", "Cotton Silk Hand Block Print Saree",
     "category_products/7"),
    ("men_category_button", "men_tshirts_button", "Men - Tshirts Products", "Men Tshirt", "category_products/3"),
    ("men_category_button", "men_jeans_button", "Men - Jeans Products", "Soft Stretch Jeans", "category_products/6"),
    ("kids_category_button", "kids_dress_button", "Kids - Dress Products", "Sleeves Top and Short - Blue & Pink",
     "category_products/4"),
    ("kids_category_button", "kids_tops_shirts_button", "Kids - Tops & Shirts Products", "Sleeves Printed Top - White",
     "category_products/5")
]
brands_data = [("brands_polo_button", "Brand - Polo Products", "Blue Top", "brand_products/Polo"),
               ("brands_hm_button", "Brand - H&M Products", "Men Tshirt", "brand_products/H&M"),
               ("brands_madame_button", "Brand - Madame Products", "Sleeveless Dress", "brand_products/Madame"),
               ("brands_mast_button", "Brand - Mast & Harbour Products", "Winter Top",
                "brand_products/Mast%20&%20Harbour"),
               ("brands_baby_button", "Brand - Babyhug Products", "Sleeves Printed Top - White",
                "brand_products/Babyhug"),
               ("brands_allen_button", "Brand - Allen Solly Junior Products", "Frozen Tops For Kids",
                "brand_products/Allen%20Solly%20Junior"),
               ("brands_kookie_button", "Brand - Kookie Kids Products", "Full Sleeves Top Cherry - Pink",
                "brand_products/Kookie%20Kids"), ("brands_biba_button", "Brand - Biba Products", "Blue Cotton Indie Mickey Dress", "brand_products/Biba")]


@pytest.mark.smoke
@pytest.mark.no_path
@pytest.mark.parametrize("url", [settings.app_url, urljoin(settings.app_url, "products")])
class TestChosen:
    @pytest.mark.chosen_category
    @pytest.mark.parametrize("cat_btn, subcat_btn, expected_title, expected_product, expected_url", category_data)
    @allure.title("Checking chosen category on static pages")
    def test_chosen_category(self, products_page: ProductsPage, url, cat_btn, subcat_btn, expected_title,
                             expected_product,
                             expected_url):
        products_page.visit(url)

        products_page.category.check_chosen_category(
            getattr(products_page.category, cat_btn),
            getattr(products_page.category, subcat_btn),
            expected_title,
            expected_product,
            expected_url
        )

    @pytest.mark.parametrize("cat_btn, expected_title, expected_product, expected_url", brands_data)
    @pytest.mark.chosen_brand
    @allure.title("Checking chosen brand on static pages")
    def test_chosen_brand(self, products_page: ProductsPage, url, expected_title, expected_product, expected_url,
                          cat_btn):
        products_page.visit(url)
        products_page.brands.check_chosen_brand(
            getattr(products_page.brands, cat_btn),
            expected_title,
            expected_product,
            expected_url
        )
