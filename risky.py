import temp
import pandas as pd
import numpy as np
import matplotlib
import io
import requests
from scipy.stats import norm

'''sample = pd.DataFrame({"BLUE": [8.70, 8.91, 8.71, 8.43, 8.73],
                       "ORANGE": [10.66, 11.08, 10.71, 11.59, 12.11]})'''

url="https://raw.githubusercontent.com/rajathkotyal/RiskyBusiness/master/data.csv"
s=requests.get(url).content
port = pd.read_csv(io.StringIO(s.decode('utf-8')),header=0, index_col=0, parse_dates=True, na_values=-99.99)
cols = ['Lo 10', 'Hi 10']
rets= port[cols]
rets.index = pd.to_datetime(rets.index, format="%Y%m")
print(rets.tail(10))

'''temp.returns(dataset = rets)
temp.product(dataset = rets)
temp.month_annualize(month_risk = 0.01)
annual_volatility = temp.annual_volatility(dataset = rets)
print(annual_volatility)

temp.returns_month(dataset = rets)
temp.annualized_ret(dataset = rets)
temp.sharpe(dataset = rets  , riskfree_rate = 0.03)
temp.drawdown(rets['Hi 10'])
temp.skewness(rets)
temp.kurtosis(rets)

z = temp.var_historic(rets)
print(z)

temp.plotvar(rets)
