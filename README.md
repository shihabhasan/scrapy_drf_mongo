# BBCscrapping: Scrapy, MongoDB & Django REST Framework API for BBC scrapping

The homepage shows all the scrapped data using the API.

## Data & Source Code
The source codes of BBCscrapping can be found on [GitHub](https://github.com/shihabhasan/scrapy_drf_mongo).

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
2. bbc.shihabhasan.com/tag=Latin America & Caribbean


### Getting individual article by title.
bbc.shihabhasan.com/title={title}. Provide the title to get the article.

#### Example:
bbc.shihabhasan.com/title=Trump urged to hand over any Comey tapes

### Getting individual article by heading.
bbc.shihabhasan.com/heading={heading}. Provide the heading to get the article.

#### Example:
bbc.shihabhasan.com/heading=Australian top IS recruiter Neil Prakash 'to be extradited'

### Getting individual article by number.
bbc.shihabhasan.com/n={number}. Provide the number to get the article.

#### Example:
bbc.shihabhasan.com/n=2

## Running BBC Spider
cd to 'scrapy_app' directory then run the command: 'spider crawl bbc' or 'spider crawl bbc -o bbc.json'


## Enjoy the software!

