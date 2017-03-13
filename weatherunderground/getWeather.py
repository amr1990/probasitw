#!/usr/bin/env python
# -*- coding: utf-8 -*-
#vim: set fileencoding=utf8 :

import sys
import urllib2
import bs4
api_key = None

class WeatherClient(object):
    '''Client for weather underground'''

    url_base = "http://api.wunderground.com/api/"
    url_service = {"almanac": "/almanac/q/CA/",
                    "hourly": "/hourly/q/CA/"}

    def __init__(self, api_key):
        self.api_key = api_key

    def almanac(self, location):
        # obtenir la url

        url = WeatherClient.url_base + self.api_key + WeatherClient.url_service["almanac"] + location + "." + "xml"
        web = urllib2.urlopen(url)
        page = web.read()
        web.close()

        # extreure les dades

        soup = bs4.BeautifulSoup(page, "lxml")
        maxim = soup.find("temp_high")
        normal = maxim.find("normal").find("c").text
        record_max = maxim.find("record").find("c").text
        record_year = maxim.find("recordyear").text

        # retornar dades

        resposta = {}
        resposta["high"] = {}
        resposta["high"]["record"] = record_max
        resposta["high"]["normal"] = normal
        resposta["high"]["year"] = record_year

        print normal, record_max, record_year

        pass


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "la API a la linea de comandes"

    wc = WeatherClient(api_key)
    wc.almanac("lleida")
