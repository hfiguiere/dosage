# -*- coding: utf-8 -*-
from ..scraper import make_scraper, _ParserScraper


def add(name, url, firstUrl=None, lang=None):
    attrs = dict(
        name=name,
        url=url,
        imageSearch='//div[@id="comic"]//img',
        prevSearch=['//a[contains(text(), " Prev")]', "//a[contains(concat(' ', @class, ' '), ' navi-prev ')]"]
    )
    if lang:
        attrs['lang'] = lang
    if firstUrl:
        attrs['firstUrl'] = url + firstUrl
    globals()[name] = make_scraper(name, _ParserScraper, **attrs)


add('CourtingDisaster', 'http://www.courting-disaster.com/', 'comic/courting-disaster-17/')
add('OnTheEdge', 'http://ontheedgecomics.com/', 'comic/ote0001/')
add('PandyLand', 'http://pandyland.net/', '1/')
add('Hipsters', 'http://www.hipsters-comic.com/', 'comic/hip01/')