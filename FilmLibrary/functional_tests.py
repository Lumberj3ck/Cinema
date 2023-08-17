import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def some_function(arg: int):
    sums = arg + 2
    return sums


class ReviewsTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_get_review_url(self):
        response = self.browser.get("http://127.0.0.1:8000/movies/oppengeimer")
        # client click on review block at the right side of film detail
        # and then redirects to review page of current film
        # there he would see comments and like button or dislike button
        button_name = self.browser.find_element(By.CLASS_NAME, "review_button")
        self.assertEqual(button_name.text, "Обзор фильма")
        self.assertEqual(
            button_name.get_attribute("href"),
            "http://127.0.0.1:8000/movies/oppengeimer/review",
        )


if __name__ == "__main__":
    unittest.main()
    some_function(1)
