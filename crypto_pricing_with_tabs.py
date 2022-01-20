import requests
import json
from operator import itemgetter
import PySimpleGUI as sg

# Pricing ripped from coinmarketcap
xch_raw = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=chia-network&start=1&limit=100&category=spot&sort=cmc_rank_advanced")
xch_dict = json.loads(xch_raw.text)
xch_dict = xch_dict["data"]["marketPairs"]
btc_raw = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=bitcoin&start=1&limit=100&category=spot&sort=cmc_rank_advanced")
btc_dict = json.loads(btc_raw.text)
btc_dict = btc_dict["data"]["marketPairs"]
eth_raw = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=ethereum&start=1&limit=100&category=spot&sort=cmc_rank_advanced")
eth_dict = json.loads(eth_raw.text)
eth_dict = eth_dict["data"]["marketPairs"]


xch_inputs = []
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
        xch_inputs.append([market["exchangeName"], reputation, round(market["volumeQuote"], 2), round(market["quote"], 2)])
xch_inputs = sorted(xch_inputs, key=itemgetter(0))

btc_inputs = []
for market in btc_dict:
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
        btc_inputs.append([market["exchangeName"], reputation, round(market["volumeQuote"], 2), round(market["quote"], 2)])
btc_inputs = sorted(btc_inputs, key=itemgetter(0))

eth_inputs = []
for market in eth_dict:
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
        eth_inputs.append([market["exchangeName"], reputation, round(market["volumeQuote"], 2), round(market["quote"], 2)])
eth_inputs = sorted(eth_inputs, key=itemgetter(0))

sg.theme('Dark Tan Blue')
headings = ['Exchange', 'Reputation', 'Volume', 'Current Price']

header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
xch_layout = [[sg.Table(values=xch_inputs, key="XCH", headings=headings, num_rows=len(xch_inputs), hide_vertical_scroll=True, def_col_width=15, auto_size_columns=False, enable_click_events=True)]]
btc_layout = [[sg.Table(values=btc_inputs, key="BTC", headings=headings, num_rows=len(btc_inputs), hide_vertical_scroll=True, def_col_width=15, auto_size_columns=False, enable_click_events=True)]]
eth_layout = [[sg.Table(values=eth_inputs, key="ETH", headings=headings, num_rows=len(eth_inputs), hide_vertical_scroll=True, def_col_width=15, auto_size_columns=False, enable_click_events=True)]]
tabgrp = [[sg.TabGroup([[sg.Tab("XCH", xch_layout), sg.Tab("BTC", btc_layout), sg.Tab("ETH", eth_layout)]])]]

window = sg.Window('Crypto Pricing Table', tabgrp, font='Courier 12')
event, values = window.read()
evs = [0, 0, 0, 0]
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):  # If user closed the window
        break
    if event[0] == "XCH":
        inputs = xch_inputs
    if event[0] == "BTC":
        inputs = btc_inputs
    if event[0] == "ETH":
        inputs = eth_inputs
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
