import requests
import json
from operator import itemgetter
import PySimpleGUI as sg

slugs = ["chia-network", "bitcoin", "ethereum", "chives-coin", "dogecoin", "avalanche"]
master_dict = {}
keys = []
for slug in slugs:
    raw = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=" + slug + "&start=1&limit=100&category=spot&sort=cmc_rank_advanced")
    raw_dict = json.loads(raw.text)
    key = raw_dict["data"]["symbol"]
    keys.append(key)
    raw_dict = raw_dict["data"]["marketPairs"]
    master_dict[key] = []
    for market in raw_dict:
        if "USDT" in market["marketPair"]:
            reputation = "unknown"
            if market["marketReputation"] >= 0.75:
                reputation = "Great"
            elif market["marketReputation"] >= 0.5:
                reputation = "Good"
            elif market["marketReputation"] >= 0.25:
                reputation = "fair"
            elif market["marketReputation"] >= 0:
                reputation = "poor"
            master_dict[key].append([market["exchangeName"], reputation, round(market["volumeQuote"], 2), round(market["quote"], 2)])

sg.theme('Dark Tan Blue')
headings = ['Exchange', 'Reputation', 'Volume', 'Current Price']
header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
window = sg.Window('Crypto Pricing Table', [[sg.TabGroup([[sg.Tab(key, [[sg.Table(values=master_dict[key], key=key, headings=headings, num_rows=len(master_dict[key]), hide_vertical_scroll=True, def_col_width=15, auto_size_columns=False, enable_click_events=True)]]) for key in keys]])]], font='Courier 12')
event, values = window.read()
evs = [0, 0, 0, 0]

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):  # If user closed the window
        break
    for i, key in enumerate(keys):
        if event[0] == key:
            inputs = master_dict[key]
    if '+CICKED+' == event[1] and (-1, 0) == event[2]:
        if evs[0] == 0:
            evs[0] = 1
            inputs = sorted(inputs, key=itemgetter(0))
            window.Element(event[0]).update(values=inputs)
        else:
            evs[0] = 0
            inputs = sorted(inputs, key=itemgetter(0), reverse=True)
            window.Element(event[0]).update(values=inputs)
    if '+CICKED+' == event[1] and (-1, 1) == event[2]:
        if evs[1] == 0:
            evs[1] = 1
            inputs = sorted(inputs, key=itemgetter(1))
            window.Element(event[0]).update(values=inputs)
        else:
            evs[1] = 0
            inputs = sorted(inputs, key=itemgetter(1), reverse=True)
            window.Element(event[0]).update(values=inputs)
    if '+CICKED+' == event[1] and (-1, 2) == event[2]:
        if evs[2] == 0:
            evs[2] = 1
            inputs = sorted(inputs, key=itemgetter(2))
            window.Element(event[0]).update(values=inputs)
        else:
            evs[2] = 0
            inputs = sorted(inputs, key=itemgetter(2), reverse=True)
            window.Element(event[0]).update(values=inputs)
    if '+CICKED+' == event[1] and (-1, 3) == event[2]:
        if evs[3] == 0:
            evs[3] = 1
            inputs = sorted(inputs, key=itemgetter(3))
            window.Element(event[0]).update(values=inputs)
        else:
            evs[3] = 0
            inputs = sorted(inputs, key=itemgetter(3), reverse=True)
            window.Element(event[0]).update(values=inputs)
