import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


def anonymous_view_public_linkedin_page(
    url_str: str,
    verify_popup_closed: bool,
    verify_min_html_char_len: int,
    inter_sleep_n_secs: float = 5.0,
    verbose: bool = True,
) -> str | None:
    """Extracts the information (HTML) from a public LinkedIn web page (e.g. person or company) using a virtual browser

    Parameters
    ----------
    url_str: str
        The URL of the public LinkedIn page
    verify_popup_closed: bool
        If this check fails, then the function returns <None> rather than the HTML found on the web page
        This check verifies that the length of the HTML increases after the pushing the [X] close button on the popup window
    verify_min_html_char_len: int
        If this check fails, then the function returns <None> rather than the HTML found on the web page
        This check verifies that the HTML string has length at least <verify_min_html_char_len>
        To disable this check, set verify_min_html_char_len=None
    inter_sleep_n_secs: float, optional (default=5.0)
        The process pauses for this number of seconds between subsequent actions in the virtual browser
    verbose: bool, optional (default=True)
        If verbose=True, progress reporting is printed to the console

    Returns
    -------
    str
        The webpage HTML, as a string

    Notes
    -----
    Selenium is used to locate the [X] close button on the initial popup window in order to make the full public page html visible
    Some pausing is required in order to wait for elements on the page to appear
    This sort of code relies closely on precise html structure, and so will definitely stop working at some point (as the LinkedIn website is modified)
    At the moment, this function uses ChromeDriver for the browser. You need to install this manually on your system in order for the function to work

    Example Usage
    -------------
    >>> extracted_person_html = anonymous_view_public_linkedin_page(
    ...     url_str="https://www.linkedin.com/in/williamhgates/",
    ...     verify_popup_closed=True,
    ...     verify_min_html_char_len=10_000,
    ...     inter_sleep_n_secs=5,
    ...     verbose=True,
    ... )
    >>> print(extracted_person_html)
    <html lang="en"><head>
        <meta name="pageKey" content="public_profile_v3_desktop">
          <meta name="linkedin:pageTag" content="nonCanonical">
        <meta name="locale" content="en_US">
        ...
    >>> extracted_company_html = anonymous_view_public_linkedin_page(
    ...     url_str="https://www.linkedin.com/company/microsoft/",
    ...     verify_popup_closed=True,
    ...     verify_min_html_char_len=10_000,
    ...     inter_sleep_n_secs=5,
    ...     verbose=True,
    ... )
    >>> print(extracted_company_html)
    <html lang="en"><head>
        <meta name="pageKey" content="d_org_guest_company_overview">
          <meta name="linkedin:pageTag" content="noncanonical_subdomain=control">
        <meta name="locale" content="en_US">
        ...
    """

    def if_verbose_print(*args, **kwargs) -> None:
        """if verbose=True, behaves identically to the print function (otherwise does nothing)"""
        if verbose:
            print(*args, **kwargs)

    if_verbose_print("opening browser..", end="")
    auto_browser = webdriver.Chrome()  # webdriver.Safari()
    if_verbose_print("..done")

    if_verbose_print("loading page..", end="")
    auto_browser.get(url_str)
    if_verbose_print("..done")

    if_verbose_print(f"waiting {inter_sleep_n_secs} seconds..", end="")
    time.sleep(inter_sleep_n_secs)
    if_verbose_print("..done")

    html_len = len(auto_browser.page_source)

    if_verbose_print(
        f"clicking close [X] button (after hovering for {inter_sleep_n_secs} seconds prior to click)..",
        end="",
    )
    try:
        actions = ActionChains(auto_browser)
        x_button = auto_browser.find_element(
            By.XPATH,
            "//icon[contains(@class,'contextual-sign-in-modal__modal-dismiss-icon lazy-loaded')]",
        )
        actions.move_to_element_with_offset(
            auto_browser.find_element(By.TAG_NAME, "body"), 0, 0
        )
        # actions.move_by_offset(100, 25).pause(5).click().perform()
        actions.move_to_element_with_offset(x_button, 1, -1).pause(
            inter_sleep_n_secs
        ).click().perform()
        if_verbose_print("..done")
    except NoSuchElementException:
        if_verbose_print("\nNo close [X] button found, so no button was clicked")

    if verify_popup_closed:
        if_verbose_print(
            "checking that initial popup window was successfully closed..", end=""
        )
        if len(auto_browser.page_source) == html_len:
            if_verbose_print("..TEST FAILED: returning <None>")
            return None
        else:
            if_verbose_print("..done")

    if_verbose_print(
        f"pausing for {inter_sleep_n_secs} seconds..",
        end="",
    )
    time.sleep(inter_sleep_n_secs)
    if_verbose_print("..done")

    if_verbose_print("extracting html..", end="")
    page_html_str = auto_browser.page_source
    auto_browser.close()
    if_verbose_print("..done")

    if verify_min_html_char_len is not None:
        if_verbose_print(
            "checking that HTML exceeds minimum character length..", end=""
        )
        if len(page_html_str) < verify_min_html_char_len:
            if_verbose_print("..TEST FAILED: returning <None>")
            return None
        else:
            if_verbose_print("..done")

    return page_html_str
