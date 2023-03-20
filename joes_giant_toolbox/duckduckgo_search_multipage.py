import random
import re
import time
import urllib
import requests
import bs4


def duckduckgo_search_multipage(
    query_str: str,
    restrict_to_site: str = None,
    n_pages: int = 1,
    wait_secs_between_requests_min_max: tuple = (2.0, 4.0),
    region: str = None,
    verbose: bool = True,
    **kwargs,
) -> dict:
    """Fetches search results from the DuckDuckGo Lite search engine

    Notes
    -----
    This function was last observed to work on 2023-03-20, but code relying on html structure is inherently unstable
    DuckDuckGo is a wonderful free service. Please don't be a wanker and abuse their API by sending too many requests in a short space of time
    If you wait random.uniform(2,4) seconds between requests, they should never block you
    Fetching just the first page of search results is much easier and more stable than fetching multiple pages, so the multi-page functionality is less stable (but it will fail loudly, so you will know)
    This function uses the service "https://lite.duckduckgo.com/lite/" API to retrieve search results

    Parameters
    ----------
    query_str: str
        The search query
    restrict_to_site: str, optional (default=None)
        Restrict results to a specific web domain (e.g. "https://www.linkedin.com/in" to search company employees only)
        If set to None, does not restrict results to a particular website
    n_pages: int, optional (default=1)
        Number of pages of search results to return
        If omitted,  defaults to 1
    wait_secs_between_requests_min_max: tuple, optional (default=(2.0, 4.0))
        Between requests to DuckDuckGo (i.e. between requesting each page of search results), there is a pause for a number of seconds randomly drawn from this interval
        This avoids you being rate limited by them
    region: str, optional (default=None)
        Region to specify to DuckDuckGo (e.g. "uk-en","us-en","za-en" etc.) - refer to the DuckDuckGo "URL parameters" documentation
    verbose: bool, optional (default=True)
        Whether to print status information as the requests are processed or not
    **kwargs
        Additional parameters to pass to requests.get() function (e.g. to alter the request timeout, headers etc.)

    Returns
    -------
    dict
        Dictionary containing search results, and logging for each request
        Example:
        {
            "request_log": {
                 "page_1": {"n_results": 30, "query":"...", "response_code":200,},
                 "page_2": {"n_results": 50, "query":"...", "response_code":200,},
                 ...
             },
            "search_results_list": [
                 {"result_desc": "...", "result_link": "...", "result_page": 1, "result_title": "..."},
                 {"result_desc": "...", "result_link": "...", "result_page": 1, "result_title": "..."},
                 ...
            ]
        }

    Example Usage
    -------------
    >>>ddg_result = duckduckgo_search_multipage(
    ...    query_str="data engineer meta",
    ...    region="uk-en",
    ...    n_pages=5,
    ...    wait_secs_between_requests_min_max=(2.0, 4.0),
    ...    restrict_to_site="https://www.linkedin.com/in",
    ...    # parameters passed to requests.get()/requests.post() functions #
    ...    timeout=5,
    ...    headers={"User-Agent":"Joe's Giant Toolbox"},
    ...)
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
    ddg_response = requests.get(
        url="https://lite.duckduckgo.com/lite/?",
        **kwargs,
    )
    results_dict["request_log"]["page_1"] = {
        "query": kwargs["params"]["q"],
        "response_code": ddg_response.status_code,
        "n_results": None,  # this is updated later
    }
    if verbose:
        print(
            f"sent request: results_page=1, status_code={ddg_response.status_code}, status_desc='{ddg_response.reason}'"
        )
    if ddg_response.status_code == 200:
        soup = bs4.BeautifulSoup(ddg_response.text, "html.parser")
        # extract search results #
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
                    "result_title": result_title_list[result_idx],
                    "result_desc": result_desc_list[result_idx],
                    "result_link": result_link_list[result_idx],
                }
            )
        if n_pages > 1:
            for page_num in range(2, n_pages + 1):
                # find parameters for [NEXT PAGE] post request #
                next_button_table = soup.find("table")
                post_request_params = {}
                for x in next_button_table.find_all("input"):
                    if "name" in x.attrs:
                        post_request_params[x.attrs["name"]] = x.attrs["value"]
                kwargs["params"].update(post_request_params)
                wait_time = random.uniform(*wait_secs_between_requests_min_max)
                if verbose:
                    print(f"waiting {wait_time:.2f} seconds")
                time.sleep(wait_time)
                ddg_response = requests.post(
                    url="https://lite.duckduckgo.com/lite", **kwargs
                )
                results_dict["request_log"][f"page_{page_num}"] = {
                    "query": kwargs["params"]["q"],
                    "response_code": ddg_response.status_code,
                    "n_results": 0,  # updated later
                }
                if verbose:
                    print(
                        f"sent request: results_page={page_num}, status_code={ddg_response.status_code}, status_desc='{ddg_response.reason}'"
                    )
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
                    results_dict["request_log"][f"page_{page_num}"]["n_results"] = len(
                        result_link_list
                    )
                    if verbose:
                        print(f"{len(result_link_list)} results returned")
                    for result_idx in range(len(result_link_list)):
                        results_dict["search_results_list"].append(
                            {
                                "result_page": page_num,
                                "result_title": result_title_list[result_idx],
                                "result_desc": result_desc_list[result_idx],
                                "result_link": result_link_list[result_idx],
                            }
                        )

    return results_dict