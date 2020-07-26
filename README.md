# RiskyBusiness
A Python Library containing various functions to analyse the risk of a business.

### Current Stage : Development

## The functions as of now include :
1. Sharpe Ratio
2. Returns & Volatility 
3. Risk by Return Ratio
4. Compounded Percentage 
5. Annual Drawdown

## Installation  

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install riskybusiness.

pypi URL : https://pypi.org/project/riskybusiness/

```bash
pip install riskybusiness
```

## Usage 

```python
import riskybusiness as rb
rb.FunctionName(dataset = Your_Dataset)
```
> Make sure the dataset is loaded using pandas with the necessary columns.

A sample program to load data is displayed in risky.py.

Clone the repository to run :
```bash
> cd cloned_directory
> python3 risky.py
```
> This will output a sample of all the functions present in the library.

## Contributing 
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)



