import json
from mypy_extensions import TypedDict

class Contract(object):
    def __init__(self, json: json):
        self.putCall = json["putCall"]
        self.symbol = json["symbol"]
        self.description = json["description"]
        self.exchangeName = json["exchangeName"]
        self.bid = float(json["bid"])
        self.ask = float(json["ask"])
        self.last = float(json["last"])
        self.mark = float(json["mark"])
        self.bidSize = int(json["bidSize"])
        self.askSize = int(json["askSize"])
        self.bidAskSize = json["bidAskSize"]
        self.lastSize = int(json["lastSize"])
        self.highPrice = float(json["highPrice"])
        self.lowPrice = float(json["lowPrice"])
        self.openPrice = float(json["openPrice"])
        self.closePrice = float(json["closePrice"])
        self.totalVolume = int(json["totalVolume"])
        self.tradeDate = json["tradeDate"]
        self.tradeTimeInLong = json["tradeTimeInLong"]
        self.quoteTimeInLong = json["quoteTimeInLong"]
        self.netChange = float(json["netChange"])
        self.volatility = float(json["volatility"])
        self.delta = float(json["delta"])
        self.gamma = float(json["gamma"])
        self.theta = float(json["theta"])
        self.vega = float(json["vega"])
        self.rho = float(json["rho"])
        self.openInterest = int(json["openInterest"])
        self.timeValue = json["timeValue"]
        self.theoreticalOptionValue = json["theoreticalOptionValue"]
        self.theoreticalVolatility = json["theoreticalVolatility"]
        self.optionDeliverablesList = json["optionDeliverablesList"]
        self.strikePrice = float(json["strikePrice"])
        self.expirationDate = json["expirationDate"]
        self.lastTradingDay = json["lastTradingDay"]
        self.multiplier = json["multiplier"]
        self.settlementType = json["settlementType"]
        self.deliverableNote = json["deliverableNote"]
        self.isIndexOption = json["isIndexOption"]
        self.percentChange = json["percentChange"]
        self.markChange = json["markChange"]
        self.markPercentChange = json["markPercentChange"]
        self.mini = json["mini"]
        self.nonStandard = json["nonStandard"]
        self.inTheMoney = json["inTheMoney"]


class ContractListForExpDate(object):
    class StrikeDict(TypedDict):
        strike: float
        contract: Contract

    strikes: StrikeDict = {}

    def __init__(self, json: json):
        for k, v in json.items():
            self.strikes[float(k)] = Contract(v[0])


class ExpDateMap(object):
    class DateDict(TypedDict):
        date: str
        contractListForExpDate: ContractListForExpDate

    dates: DateDict = {}

    def __init__(self, json: json):
        for k, v in json.items():
            self.dates[k.split(':')[0]] = ContractListForExpDate(v)


class OptionChain(object):
    interval = 0.0
    isDelayed = False
    isIndex = False
    interestRate = 0.0
    underlyingPrice = 0.0
    volatility = 0.0
    daystoExpiration = 0.0
    numberOfContracts = 0

    def __init__(self, json: json):
        self.symbol = json["symbol"]
        self.status = json["status"]
        self.underlying = json["underlying"]
        self.strategy = json["strategy"]
        self.interval = json["interval"]
        self.isDelayed = json["isDelayed"]
        self.isIndex = json["isIndex"]
        self.interestRate = json["interestRate"]
        self.underlyingPrice = json["underlyingPrice"]
        self.daystoExpiration = json["daysToExpiration"]
        self.numberOfContracts = json["numberOfContracts"]
        self.calls = ExpDateMap(json["callExpDateMap"])
        self.puts = ExpDateMap(json["putExpDateMap"])

