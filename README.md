# py-mediastack

An unofficial python helper package to interact with the mediastack API.

## Drawbacks

- No historical Data (I don't have a paid account to test it)
- No News Sources search (I don't have time to implement it)

Feel free to contribute. Make sure that you use the `pre-commit` hooks.

## what can it do ?

It can give you live news updated.

## installation

```commandline
pip3 install py-mediastack
```

## Usage

### Get the api key from [here](https://mediastack.com/)

```python
from mediastack import MediaStack
client = MediaStack("<your-api-key>")

resp = client.get_live_news()

print(resp.pagination)
print(resp.data[0])

```

```
Pagination(limit=25, offset=0, count=25, total=10000)

Article(author='Redazione', title='Via agli incontri di quartiere:
primo appuntamento con i residenti di San Lorenzo',

description='Hanno preso il via ieri sera, dalla sala Biasin dove l’Amministrazione ha convocato i residenti del quartiere San Lorenzo, gli ‘Incontri di quartiere’ con cui la Giunta si confronta con i cittadini. Presenti, oltre al Sindaco Gian Francesco Menani, il vicesindaco Camilla Nizzoli e gli assessori Corrado Ruini e Massimo Malagoli, che hanno ascoltato le [&#8230;]',
url='https://www.bologna2000.com/2021/09/07/via-agli-incontri-di-quartiere-primo-appuntamento-con-i-residenti-di-san-lorenzo/',
image=None,
category='general',
language='it',
 country='it',
 published_at='2021-09-07T08:32:52+00:00',
 source='bologna2000')
```

---

The parameters for MediaStack.get_live_news are as follow:

- `access_key`: `str` -> Use this parameter to specify your unique API access key, which is shown when you log in to your account dashboard.
- `sources`: `Optional[list[str]]` -> Use this parameter to include or exclude one or multiple news sources. Example: To include CNN, but exclude BBC: `sources=["cnn", "-bbc"]`
- `categories`: `Optional[list[str]]` Use this parameter to include or exclude one or multiple news categories. Example: To include business, but exclude sports: `categories=["business", "-sports"]`.

- `countries`: `Optional[list[str]]` -> Use this parameter to include or exclude one or multiple countries. Example: To include Australia, but exclude the US: `countries=["au", "-us"]`.

- `languages`: `Optional[list[str]]` -> Use this parameter to include or exclude one or multiple languages. Example: To include English, but exclude German: `languages=["en", "-de"]`.

- `keywords`: `Optional[str]` -> Use this parameter to search for sentences, you can also exclude words that you do not want to appear in your search results. Example: To search for "New movies 2021" but exclude "Matrix": `keywords='new movies 2021 -matrix'`
- `date`: `Optional[str]` -> Use this parameter to specify a date or date range. Example: `date=2020-01-01` for news on Jan 1st and `date='2020-12-24,2020-12-31'` for news between Dec 24th and 31st.
- `sort`: `Optional[str]` -> Use this parameter to specify a sorting order. Available values: `published_desc` (default), `published_asc`, `popularity`
- `limit`: `Optional[int]` -> Use this parameter to specify a pagination limit (number of results per page) for your API request. Default limit value is 25, maximum allowed limit value is 100.
- `offset`: `Optional[int]` -> Use this parameter to specify a pagination offset value for your API request. Example: An offset value of 100 combined with a limit value of 10 would show results 100-110. Default value is 0, starting with the first available result.

---

The `get_live_news` methods returns a `LiveNewsResponse` data class.
It contains the `pagination` details and the `data`.

---

The `LiveNewsResponse.pagination` is of type `Pagination` and has the following
attributes.

- `Pagination.limit` -> your pagination limit value.
- `Pagination.offset` -> your pagination offset value.
- `Pagination.count` -> the results count on the current page.
- `Pagination.total` -> the total count of results available.

---

The `LiveNewsResponse.data` is a `list[Article]` and each `Article` has the following
attributes.

- `Article.author` -> the name of the author of the given news article.
- `Article.title` -> the title text of the given news article.
- `Article.description` -> the description text of the given news article.
- `Article.url` - > the URL leading to the given news article.
- `Article.image` -> an image URL associated with the given news article.
- `Article.category` -> the category associated with the given news article.
- `Article.language` -> the language the given news article is in.
- `Article.country` -> the country code associated with the given news article.
- `Article.published_at` -> the exact time stamp the given news article was published.
- `Article.source` -> the source from which the article was taken

---

## Supported News Categories

- general - Uncategorized News
- business - Business News
- entertainment - Entertainment News
- health - Health News
- science - Science News
- sports - Sports News
- technology - Technology News

## Supported Countries

Click [Here](https://mediastack.com/sources) to see the list of all the supported countries.

## Supported Languages

- ar - Arabic
- de - German
- en - English
- es - Spanish
- fr - French
- he - Hebrew
- it - Italian
- nl - Dutch
- no - Norwegian
- pt - Portuguese
- ru - Russian
- se - Swedish
- zh - Chinese

---

most the docs are directly taken from the [`mediastacks api docs`](https://mediastack.com/documentation)
