from datetime import datetime

import lxml.html as html
import requests

from apps.core import constants


class CoinScraper:

    def __init__(self):
        self.HOME_URL = constants.HOME_URL

    def extract_coin_data(self, coin_name):
        """Function to parse the data from the coin"""

        link = self.get_coin_page(coin_name)
        response = requests.get(link)
        try:
            if response.status_code == 200:
                bitcoin_page = response.content.decode('utf-8')
                parsed = html.fromstring(bitcoin_page)
                data = dict()
                for index, value in enumerate(constants.VALUES_LIST):
                    tag = parsed.xpath(constants.XPATH_NODES[index])
                    data[value] = tag[0]
                return data
            else:
                raise ValueError(f'Error: {response.status_code}')
        except ValueError as error:
            print(error)

    def get_coin_page(self, coin_name):
        """Function to get the coin page"""
        return f"{self.HOME_URL}/currencies/{coin_name}/"
