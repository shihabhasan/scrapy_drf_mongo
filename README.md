# BBCscrapping: Scrapy, MongoDB & Django REST Framework API for BBC scrapping

The homepage shows all the scrapped data using the API.

## API Sever & Source Code
The API server can be access at https://bbc.shihabhasan.com. The source codes of BBCscrapping can be found on [GitHub](https://github.com/shihabhasan/scrapy_drf_mongo).

## API
The API homepage of BBCscrapping can be found on bbc.shihabhasan.com. API has been built by Django REST Framework.

### Tag List
bbc.shihabhasan.com/tag

### Title List
bbc.shihabhasan.com/title

### Heading List
bbc.shihabhasan.com/heading

### Getting list of articles by tag name.
bbc.shihabhasan.com/tag={tag name}. Provide the tag name to get the list of articles.

#### Example:
1. bbc.shihabhasan.com/tag=Australia
2. bbc.shihabhasan.com/tag=Science & Environment


### Getting individual article by title.
bbc.shihabhasan.com/title={title}. Provide the title to get the article.

#### Example:
bbc.shihabhasan.com/title=Troubled Toshiba misses results deadline

### Getting individual article by heading.
bbc.shihabhasan.com/heading={heading}. Provide the heading to get the article.

#### Example:
bbc.shihabhasan.com/heading=Troubled Toshiba misses annual results deadline

### Getting individual article by number.
bbc.shihabhasan.com/n={number}. Provide the number to get the article.

#### Example:
bbc.shihabhasan.com/n=2

## Running BBC Spider
cd to 'scrapy_app' directory then run the command: 'scrapy crawl bbc' or 'scrapy crawl bbc -o bbc.json'


## Enjoy the software!

