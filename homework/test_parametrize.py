"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene import by
from selene.support.shared import browser


@pytest.fixture(params=["desktop", "mobile"])
def browser_config_param(request):
    browser.config.base_url = "https://github.com"
    if request.param == "desktop":
        browser.config.window_width = 1680
        browser.config.window_height = 900
    elif request.param == "mobile":
        browser.config.window_width = 375
        browser.config.window_height = 667


@pytest.mark.parametrize("browser_config_param", ["desktop"], indirect=True)
def test_github_desktop(browser_config_param):
    browser.open("/")
    browser.element(".HeaderMenu-link--sign-in").click()


@pytest.mark.parametrize("browser_config_param", ["mobile"], indirect=True)
def test_github_mobile(browser_config_param):
    browser.open("/")
    browser.element(by.link_text("Sign up")).click()
    browser.element(by.link_text("Sign in →")).click()
