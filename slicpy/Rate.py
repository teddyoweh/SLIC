class Rate(object):

    RATE = {
        'type':'',
        'rate':'',

    }
    def __init__(self):
        pass
    def set_hourly_rate(self,rate):
        self.RATE['type'] = 'hourly'
        self.RATE['rate'] = rate
    def set_daily_rate(self,rate):
        self.RATE['type'] = 'daily'
        self.RATE['rate'] = rate
    def set_weekly_rate(self,rate):
        self.RATE['type'] = 'weekly'
        self.RATE['rate'] = rate
    def set_monthly_rate(self,rate):
        self.RATE['type'] = 'monthly'
        self.RATE['rate'] = rate
    def set_yearly_rate(self,rate):
        self.RATE['type'] = 'yearly'
        self.RATE['rate'] = rate
    def get_rate(self):
        return self.RATE

    