"""
Вашей задачей будет создать сервер агрегатор (он выполнит несколько запросов на адреса сторонних сайтов).
Количество сайтов и сами сайты на которые вы будете слать реквесты вы определяете сами
(вот например по ссылке ниже найдете список популярных ресурсов, но, как правило, они требуют регистрации,
после чего они предоставят вам что-то типа ключа с которым вы сможете запросить информацию)

1) Познакомиться с фреймворком AIOHTTP (https://docs.aiohttp.org/en/stable/).
2) Создать сервер который мог бы принимать GET запросы на адрес (http://localhost/collect_info)
3) В ответе должна быть агрегирована информация полученная от сторонних ресурсов.
"""
import aiohttp
from aiohttp import web
import asyncio

data = ''

weather_map_api = {'url': "https://community-open-weather-map.p.rapidapi.com/weather",
                   'params': {"q": "Odesa,ua",
                              "lat": "0", "lon": "0",
                              "callback": "test",
                              "id": "2172797",
                              "lang": "null",
                              "units": "\"metric\" or \"imperial\"",
                              "mode": "xml, html"},
                   'headers': {'x-rapidapi-key': "2752625ecfmshd32215ec67bc34cp16513bjsn75485a29c788",
                               'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
                               }
                   }
skyscanner_api = {'url': "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/referral/"
                         "v1.0/%7Bcountry%7D/%7Bcurrency%7D/%7Blocale%7D/%7Boriginplace%7D/%7Bdestinationplace%7D/"
                         "%7Boutboundpartialdate%7D/%7Binboundpartialdate%7D",
                  'params': {'shortapikey': 'ra66933236979928',
                             'apiKey': '{shortapikey}'
                             },
                  'headers': {'x-rapidapi-key': "2752625ecfmshd32215ec67bc34cp16513bjsn75485a29c788",
                              'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
                              }
                  }
yahoo_finance_api = {'url': "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete",
                     'params': {"q": "tesla",
                                "region": "US"
                                },
                     'headers': {'x-rapidapi-key': "2752625ecfmshd32215ec67bc34cp16513bjsn75485a29c788",
                                 'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
                                 }
                     }

apis = (skyscanner_api, weather_map_api, yahoo_finance_api)


async def get_info(api):
    global data
    async with aiohttp.ClientSession() as session:
        async with session.get(api['url'], headers=api['headers'], params=api['params']) as resp:
            text = await resp.text()
            data += f"{api['url']}:\n{text}\n\n"


async def collect_info(request):
    global data
    data = ''
    futures = [get_info(api) for api in apis]
    await asyncio.gather(*futures)
    return web.Response(text=data)


app = web.Application()
app.router.add_get('/collect_info', collect_info)
web.run_app(app, port=80)
