import requests
import json
from operator import itemgetter
import PySimpleGUI as sg

# xch pricing ripped from coinmarketcap
xch_raw = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=chia-network&start=1&limit=100&category=spot&sort=cmc_rank_advanced")
xch_dict = json.loads(xch_raw.text)
xch_dict = xch_dict["data"]["marketPairs"]

sg.theme('Dark Tan Blue')

headings = ['Exchange', 'Reputation', 'Volume', 'Current Price']
inputs = []
for market in xch_dict:
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
        inputs.append([market["exchangeName"], reputation, round(market["volumeQuote"], 2), round(market["quote"], 2)])
inputs = sorted(inputs, key = itemgetter(0))
header = [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]
layout = [[sg.Table(values = inputs, headings=headings, num_rows=len(inputs), hide_vertical_scroll = True, def_col_width = 15, auto_size_columns = False, enable_click_events=True)]]

window = sg.Window('XCH Pricing Table', layout, font='Courier 12')
event, values = window.read()
print(window.element_list())
evs = [0,0,0,0]
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):     # If user closed the window
        break
    if '+CICKED+' == event[1] and (-1, 0) == event[2]:
        if evs[0] == 0:
            evs[0] = 1
            inputs = sorted(inputs, key = itemgetter(0))
            window.Element(0).update(values=inputs)
        else:
            evs[0] = 0
            inputs = sorted(inputs, key=itemgetter(0), reverse=True)
            window.Element(0).update(values=inputs)
    if '+CICKED+' == event[1] and (-1, 1) == event[2]:
        if evs[1] == 0:
            evs[1] = 1
            inputs = sorted(inputs, key=itemgetter(1))
            window.Element(0).update(values=inputs)
        else:
            evs[1] = 0
            inputs = sorted(inputs, key=itemgetter(1), reverse=True)
            window.Element(0).update(values=inputs)
    if '+CICKED+' == event[1] and (-1, 2) == event[2]:
        if evs[2] == 0:
            evs[2] = 1
            inputs = sorted(inputs, key=itemgetter(2))
            window.Element(0).update(values=inputs)
        else:
            evs[2] = 0
            inputs = sorted(inputs, key=itemgetter(2), reverse=True)
            window.Element(0).update(values=inputs)
    if '+CICKED+' == event[1] and (-1, 3) == event[2]:
        if evs[3] == 0:
            evs[3] = 1
            inputs = sorted(inputs, key=itemgetter(3))
            window.Element(0).update(values=inputs)
        else:
            evs[3] = 0
            inputs = sorted(inputs, key=itemgetter(3), reverse=True)
            window.Element(0).update(values=inputs)
