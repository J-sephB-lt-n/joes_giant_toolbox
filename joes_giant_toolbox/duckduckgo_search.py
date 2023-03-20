import random
import re
import time
import urllib
import requests
import bs4


def duckduckgo_search(
    query_str: str,
    restrict_to_site: str = None,
    n_pages: int = 1,
    wait_secs_between_requests_min_max: tuple = (5.0, 10.0),
    region: str = None,
    verbose: bool = True,
    **kwargs,
) -> dict:
    """documentation TODO

    Notes
    -----
    This function was last observed to work on 2023-03-19, but I think that DuckDuckGo is likely to change their system regularly
    DuckDuckGo is a wonderful free service. Please don't be a wanker and abuse their API by sending too many requests in a short space of time
    Fetching just the first page of search results is much easier and more stable than fetching more, so this functionality is likely to break first if DuckDuckGo change their html

    Parameters
    ----------
    query_str: str
        The search query
    restrict_to_site: str, optional (default=None)
        Restrict results to a specific web domain (e.g. "https://www.linkedin.com/in" to search company employees only)
        If set to None, does not restrict results to a particular domain
    n_pages: int, optional (default=1)
        Number of pages of search results to return
        If omitted,  defaults to 1
    wait_secs_between_requests_min_max: tuple, optional (default=(2.0, 4.0))
        TODO
    region: str, optional (default=None)
        Region to specify to DuckDuckGo (e.g. "uk-en","us-en","za-en" etc.) - refer to the DuckDuckGo "URL parameters" documentation
    verbose: bool, optional (default=True)
        Whether to print status information as the requests as processed
    **kwargs
        Additional parameters to pass to requests.get() function

    Returns
    -------
    dict
        TODO

    Example Usage
    -------------
    >>>ddg_result = duckduckgo_search(
        query_str="bayesian decision network",
        region="uk-en",
        n_pages=4,
        # parameters passed to requests.get() function #
        timeout=5
    )
    >>>print( f"{len(ddg_result['response']['search_results'])} search results returned" )
    >>>print("first results is:"); ddg_result['response']['search_results'][0]
    """
    results_dict = {
        "request_log": {},
        "search_results_list": [],
    }
    if "params" not in kwargs:
        kwargs["params"] = {}
    if restrict_to_site is not None:
        kwargs["params"]["q"] = f"{query_str} site:{restrict_to_site}"
    else:
        kwargs["params"]["q"] = query_str
    if region is not None:
        kwargs["params"]["region"] = region
    if "headers" not in kwargs:
        kwargs["headers"] = {
            "User-Agent": "Joe's Giant Toolbox",
        }
    results_dict["request_log"]["page_1"] = {"query": kwargs["params"]["q"]}
    ddg_response = requests.get(
        url="https://lite.duckduckgo.com/lite/?",
        # "https://html.duckduckgo.com/html/?",
        **kwargs,
    )
    results_dict["request_log"]["page_1"]["response_code"] = ddg_response.status_code
    if verbose:
        print(
            f"sent request: results_page=1, status_code={ddg_response.status_code}, status_desc='{ddg_response.reason}'"
        )
    results_dict["request_log"]["page_1"]["n_results"] = 0  # can be updated later
    if ddg_response.status_code == 200:
        soup = bs4.BeautifulSoup(ddg_response.text, "html.parser")
        result_title_list = [x.text for x in soup.find_all(class_="result-link")]
        result_link_list = [
            urllib.parse.unquote(
                re.sub(r"//duckduckgo.com/l/\?uddg=", "", x["href"])
            ).split("&")[0]
            for x in soup.find_all(class_="result-link")
        ]
        result_desc_list = [x.text for x in soup.find_all(class_="result-snippet")]
        results_dict["request_log"]["page_1"]["n_results"] = len(result_desc_list)
        if verbose:
            print(f"{len(result_link_list)} results returned")
        for result_idx in range(len(result_link_list)):
            results_dict["search_results_list"].append(
                {
                    "result_page": 1,
                    "search_rank": None,
                    "result_title": result_title_list[result_idx],
                    "result_desc": result_desc_list[result_idx],
                    "result_link": result_link_list[result_idx],
                }
            )
        if n_pages > 1:
            for page_num in range(2, n_pages + 1):
                wait_time = random.uniform(*wait_secs_between_requests_min_max)
                if verbose:
                    print(f"waiting {wait_time:.2f} seconds")
                time.sleep(wait_time)
                potential_next_page_urls = soup.find_all(
                    string=lambda text: isinstance(text, bs4.Comment)
                )
                next_page_url = None
                for potential_next_page_url in potential_next_page_urls:
                    found_next_page_url = re.search(
                        r"rel=\"next\" href=\"([^\"]+\.js)\"", potential_next_page_url
                    )
                    if found_next_page_url:
                        next_page_url = re.sub(
                            r"^/lite/\?q=", "", found_next_page_url.groups(0)[0]
                        )
                        break
                if next_page_url is not None:
                    if verbose:
                        print(f"found search results page {page_num} url")
                    kwargs["params"]["q"] = next_page_url
                    results_dict["request_log"][f"page_{page_num}"] = {
                        "query": kwargs["params"]["q"]
                    }
                    ddg_response = requests.post(
                        url="https://lite.duckduckgo.com/lite/?", **kwargs
                    )
                    results_dict["request_log"][f"page_{page_num}"][
                        "response_code"
                    ] = ddg_response.status_code
                    if verbose:
                        print(
                            f"sent request: results_page={page_num}, status_code={ddg_response.status_code}, status_desc='{ddg_response.reason}'"
                        )
                    results_dict["request_log"][f"page_{page_num}"][
                        "n_results"
                    ] = 0  # can be updated later
                    if ddg_response.status_code == 200:
                        soup = bs4.BeautifulSoup(ddg_response.text, "html.parser")
                        result_title_list = [
                            x.text for x in soup.find_all(class_="result-link")
                        ]
                        result_link_list = [
                            urllib.parse.unquote(
                                re.sub(r"//duckduckgo.com/l/\?uddg=", "", x["href"])
                            ).split("&")[0]
                            for x in soup.find_all(class_="result-link")
                        ]
                        result_desc_list = [
                            x.text for x in soup.find_all(class_="result-snippet")
                        ]
                        results_dict["request_log"][f"page_{page_num}"][
                            "n_results"
                        ] = len(result_link_list)
                        if verbose:
                            print(f"{len(result_link_list)} results returned")
                        for result_idx in range(len(result_link_list)):
                            results_dict["search_results_list"].append(
                                {
                                    "result_page": page_num,
                                    "search_rank": None,
                                    "result_title": result_title_list[result_idx],
                                    "result_desc": result_desc_list[result_idx],
                                    "result_link": result_link_list[result_idx],
                                }
                            )
                else:
                    print(f"FAILED to find search results page {page_num} url")
                    break

    return results_dict


if __name__ == "__main__":
    from pprint import pprint
    from view_nested_dict_structure import view_nested_dict_structure

    ddg_result = duckduckgo_search(
        query_str="data amazon",
        region="uk-en",
        n_pages=10,
        wait_secs_between_requests_min_max=(5.0, 10.0),
        restrict_to_site="https://www.linkedin.com/in",
        # parameters passed to requests.get() function #
        timeout=5,
    )

    pprint(ddg_result["request_log"])

    for x in ddg_result["search_results_list"]:
        view_nested_dict_structure(x, value_preview_len=100)
        print()
