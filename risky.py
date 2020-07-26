import init
import pandas as pd
import numpy as np
import matplotlib

sample = pd.DataFrame({"BLUE": [8.70, 8.91, 8.71, 8.43, 8.73],
                       "ORANGE": [10.66, 11.08, 10.71, 11.59, 12.11]})

port = pd.read_csv('/Users/rajath/Downloads/pf.csv',header=0, index_col=0, parse_dates=True, na_values=-99.99)
cols = ['Lo 10', 'Hi 10']
rets= port[cols]
rets.index = pd.to_datetime(rets.index, format="%Y%m")

init.returns(dataset = rets)
init.product(dataset = rets)
init.month_annualize(month_risk = 0.01)
init.annual_volatility(dataset = rets)

init.returns_month(dataset = rets)
init.annualized_ret(dataset = rets)
init.sharpe(dataset = rets  , riskfree_rate = 0.03)
init.drawdown(rets['Hi 10'])
