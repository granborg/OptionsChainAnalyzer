from td.client import TDClient
import requests
import json

import oca_config
import option_chain

settingsLocation = "Settings/oca_config.ini"
oca_config_ini = oca_config.OcaConfig(settingsLocation)

# Create a new session, credentials path is optional.
TDSession = TDClient(
    client_id=oca_config_ini.consumerKey,
    redirect_uri=oca_config_ini.callbackUrl,
)

# Login to the session
TDSession.login()

full_url = 'https://api.tdameritrade.com/v1/marketdata/chains?'

page = requests.get(
    url=full_url,
    params=
    {
        'apikey' : oca_config_ini.consumerKey,
        'symbol' : oca_config_ini.ticker,
        'fromDate' : oca_config_ini.fromDate,
        'toDate' : oca_config_ini.toDate,
        'contractType' : oca_config_ini.contractType,
    })

content = json.loads(page.text)

myOptionChain = option_chain.OptionChain(content)

# Example
date: option_chain.ContractListForExpDate
for date in myOptionChain.puts.dates.values():
    strike: option_chain.Contract
    for strike in date.strikes.values():
        if strike.strikePrice > oca_config_ini.minStrike \
            and strike.strikePrice < oca_config_ini.maxStrike:
            print(strike.description
                  + " bid: " + str(strike.bid)
                  + " ask: " + str(strike.ask))
