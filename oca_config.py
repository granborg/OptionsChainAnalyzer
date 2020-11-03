class OcaConfig(object):
    consumerKey = ''
    callbackUrl = ''
    ticker = ''
    fromDate = ''
    toDate = ''
    contractType = ''

    minStrike = 0.0
    maxStrike = 0.0

    def __init__(self, configFileName):
        config = open(configFileName).read()
        self.assignParams(config)
        self.checkParamsAreAssigned()


    def assignParams(self, config):
        for line in config.split('\n'):
            if line.startswith('#'):
                continue

            split = line.split('=')
            if split[0] == 'consumerKey':
                self.consumerKey = split[1]
            elif split[0] == 'callbackUrl':
                self.callbackUrl = split[1]
            elif split[0] == 'ticker':
                self.ticker = split[1]
            elif split[0] == 'fromDate':
                self.fromDate = split[1]
            elif split[0] == 'toDate':
                self.toDate = split[1]
            elif split[0] == 'contractType':
                self.contractType = split[1]
            elif split[0] == 'minStrike':
                self.minStrike = float(split[1])
            elif split[0] == 'maxStrike':
                self.maxStrike = float(split[1])
            else:
                raise Exception("Invalid config parameter: " + split[0])


    def checkParamsAreAssigned(self):
        if self.consumerKey == '':
            self.raiseMissingParamException('consumerKey')
        if self.callbackUrl == '':
            self.raiseMissingParamException('callbackUrl')
        if self.ticker == '':
            self.raiseMissingParamException('ticker')
        if self.fromDate == '':
            self.raiseMissingParamException('fromDate')
        if self.toDate == '':
            self.raiseMissingParamException('toDate')
        if self.contractType == '':
            self.raiseMissingParamException('contractType')
        if self.minStrike == '':
            self.raiseMissingParamException('minStrike')
        if self.maxStrike == '':
            self.raiseMissingParamException('maxStrike')


    def raiseMissingParamException(self, param):
        raise Exception("Config file does not have a value for " + param + "!")