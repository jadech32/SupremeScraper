# SupremeScraper
Scrapes the online shop for products, searched by name, color and category. This will find your item and open it in your default web browser. Meant for Python 3

## Installation:
1. Clone via git or download as zip file
2. Install the requirements (done once per install)
```
     pip install -r requirements.txt
```

## Set Up and Configuration:
### Acceptable categories:
- jackets
- shirts
- sweaters
- tshirts
- sweatshirts
- hats
- pants
- bags
- accessories
- shoes
- skate
### Proxy Support

- Create a ```config``` folder, and under that please create a ```proxies.txt``` and paste your HTTP proxies line by line.
- Now supports ```user:pass``` proxies as well as non auth proxies.
- Does not have support for non proxy scraping (use localhost).

### Example Thread
```
     threading.Thread(target=supreme.findItem, args=(['blimp'], ['white'], 'accessories'))
```
- Keywords: First list in the args tuple. Example: ```['box','logo','hooded']```
- Color: Second list in the args tuple, but usually just one word. Example: ```['red']``` or ```['desert','camo']```
- Category: Third argument in the args tuple. This is just one string (has to be one of the categories from above).

### Tips
- Recommended to be used with another bot (e.g. HeatedSneaks)
- For US users, see UK product names for keywords and color.
