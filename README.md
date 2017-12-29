This program scrape all profile in the search result from "http://recruitmentgeek.com/tools/linkedin/", the result are limited to 100 results which is not so useful.

One example of input is:

- python recruitmentgeek.py CEO Brasil

I created a count variable which is stored on count.txt, it is used to come back in the same pagination in case of something. Everytime that you run the program reset the number in count to 1.

Requiments:

- BeautifulSoup
- dryscrape