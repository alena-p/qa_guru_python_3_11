"""
Сделайте разные фикстуры для каждого теста
"""
from selene import by
import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_config_desktop():
    browser.config.base_url = "https://github.com"
    browser.config.window_width = 1680
    browser.config.window_height = 900


@pytest.fixture()
def browser_config_mobile():
    browser.config.base_url = "https://github.com"
    browser.config.window_width = 375
    browser.config.window_height = 667


def test_github_desktop(browser_config_desktop):
    browser.open("/")
    browser.element(".HeaderMenu-link--sign-in").click()


def test_github_mobile(browser_config_mobile):
    browser.open("/")
    browser.element(by.link_text("Sign up")).click()
    browser.element(by.link_text("Sign in →")).click()
