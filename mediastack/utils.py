from typing import List

from mediastack.const import CATEGORIES
from mediastack.const import COUNTRIES
from mediastack.const import LANGUAGES
from mediastack.const import SORT


def verify_live_news_args(
    sources:  object,
    categories:  object,
    countries:  object,
    languages:  object,
    keywords:  object,
    date:   object,
    sort: object,
    limit: object,
    offset: object
) -> bool:

    def verify_list_string(arg: object, name: str) -> bool:
        if not arg:
            return True

        if isinstance(arg, list):
            if not all(isinstance(i, str) for i in arg):
                raise TypeError(
                    f"All entries in {name!r} must be of type 'str'")

            else:
                return True

        else:
            raise TypeError(
                f"{name!r} must be of type 'list' and not {type(arg).__name__!r}")

    def validate_list_entries(values: object, valid: List[str], name: str) -> bool:
        if not values:
            return True

        if isinstance(values, list):
            for v in values:
                if v not in valid:
                    raise ValueError(
                        f"Invalid value {v!r} for {name!r}, must be any of {valid}")

            else:
                return True
        else:
            return False

    if verify_list_string(sources, "sources") and \
            verify_list_string(categories, "categories") and \
            verify_list_string(countries, "countries") and \
            verify_list_string(languages, "languages"):
        if validate_list_entries(categories, CATEGORIES, "categories") and \
                validate_list_entries(countries, COUNTRIES, "countries") and \
                validate_list_entries(languages, LANGUAGES, "languages"):
            if keywords is None or isinstance(keywords, str):
                if date is None or isinstance(date, str):
                    if isinstance(sort, str) and sort in SORT:
                        if isinstance(limit, int):
                            if 0 <= limit <= 100:
                                if isinstance(offset, int):
                                    return True

                            else:
                                raise ValueError(
                                    "'limit' must be between 0 and 100")

                        else:
                            raise TypeError(
                                f"'limit' must be of type 'int' and not {type(limit).__name__!r}")

                    else:
                        raise TypeError(f"'sort' by of type 'str' and not {type(sort).__name__!r}"
                                        f"and must be any of {SORT}")

                else:
                    raise TypeError(
                        f"'date' must be of type 'str' and not {type(date).__name__!r}")

            else:
                raise TypeError(
                    f"'keywords' must be of type 'str' and not {type(keywords).__name__!r}")

    return False


def generate_request_url() -> str: ...
