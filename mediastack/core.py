from dataclasses import dataclass
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

import requests

from mediastack.errors import MediastackApiError
from mediastack.utils import generate_news_request_url
from mediastack.utils import verify_live_news_args

__all__ = ("MediaStack")


@dataclass
class Pagination:
    limit: int
    offset: int
    count: int
    total: int


@dataclass
class Article:
    author: str
    title: str
    description: str
    url: str
    image: str
    category: str
    language: str
    country: str
    published_at: str
    source: str


@dataclass
class LiveNewsResponse:
    pagination: Pagination
    data: List[Article]
    request_url: str


class MediaStack:

    def __init__(self, access_key: str) -> None:
        self.access_key = access_key

    def get_live_news(
        self,
        sources: Optional[List[str]] = None,
        categories:  Optional[List[str]] = None,
        countries:  Optional[List[str]] = None,
        languages:  Optional[List[str]] = None,
        keywords: Optional[str] = None,
        date:  Optional[str] = None,
        sort: Literal["published_desc", "published_asc",
                      "popularity"] = "published_desc",
        limit: int = 25,
        offset: int = 0

    ) -> Union[LiveNewsResponse, None]:

        if verify_live_news_args(sources, categories, countries,
                                 languages, keywords, date, sort, limit, offset):
            url = generate_news_request_url(self.access_key, sources, categories,
                                            countries, languages, keywords, date, sort, limit)

            resp = requests.get(url).json()
            if "error" in resp:
                raise MediastackApiError(**resp["error"])

            else:
                if "pagination" and "data" in resp:
                    p = Pagination(**resp["pagination"])
                    d = [Article(**a) for a in resp["data"]]
                    return LiveNewsResponse(p, d, url)

        return None
