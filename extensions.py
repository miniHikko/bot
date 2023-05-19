import requests
from conf import keys


class convertionException(Exception):
    pass


class conventor:
    @staticmethod
    def get_price(quote: str, base: str, amaout: str):
        if quote == base:
            raise convertionException('нельзя переводить одинаковые валюты')
        try:
            from_ = keys[quote]
        except KeyError:
            raise convertionException(f"не получилось получить {quote}")
        try:
            to = keys[base]
        except KeyError:
            raise convertionException(f"не получилось получить {base}")
        try:
            amaout = float(amaout)
        except ValueError:
            raise convertionException(f'число не может быть строкой')
        url = requests.get(f'https://api.exchangerate.host/convert?from={from_}&to={to}')
        data = url.json()
        h = data['info']
        result = h['rate']
        real_result = result * amaout

        return round(real_result, 2)
