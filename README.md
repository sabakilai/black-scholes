# Black-Scholes model

## What Is the Black-Scholes Model?

The mathematical equation estimates the theoretical value of derivatives based on other investment instruments, taking into account the impact of time and other risk factors.

### Notation


$C = SN(d1) - K e^{-rt}N(d2) $

where:

$d1 = \frac{ ln \frac{S}{K} + (r + \frac{\sigma^2}{2}) t }{\sigma \sqrt{t}}$ 

and 

$d2 = d1 - \sigma \sqrt{t}$

$ C $ - call option price 

$ N $ - Cumulative distribution function of the normal distribution

$ S $ - spot price of an asset

$ K $ - strike price

$ r $ - risk-free interest rate

$ t $ - time to maturity

$ \sigma $ - volatility of the asset


### Assumptions Made

- It works on European options that can only be exercised at expiration.
- No dividends paid out during the option’s life.
- No transaction and commissions costs in buying the option.
- The returns on the underlying are normally distributed.

[[Source]](https://medium.com/swlh/calculating-option-premiums-using-the-black-scholes-model-in-python-e9ed227afbee)


## Black-Scholes model implementation

The model is implemented inside `BlackSholesModel` class:


```python
class BlackSholesModel:
    def __init__(self, r, S, K, t, sigma)

    def get_d1(self)
        """
        Returns the conditional probability. 
        If the spot price at maturity date is above 
        the strike price, what is relation between
        the expected value to the current spot value
        """
    def get_d2(self)
        """
        Returns the probability that the option is ITM, 
        i.e. buy the security below its market value
        """

    def get_call_price(self, round_d)
        """
            Returns the estimated price of a call option
            and rounds it r to `round_d` decimals
        """

    def get_put_price(self, round_d)
        """
            Returns the estimated price of a put option
            and rounds it r to `round_d` decimals
        """
```

After initializing a class with the parameters, you can calculate the prices by calling `get_call_price()` and `get_put_price()`


## Demo 

To demonstrate the model in action, we are going to calculate the call option price for `Barclays` stock with maturity date in one month.

We will use the Yahoo Finance dataset to generate the volatility of the stock. We will use the stock data for the last year.

</br>

The dataset has the following structure:

|            |       High |        Low |       Open |      Close |     Volume |  Adj Close |
|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|
|       Date |            |            |            |            |            |            |
| 2021-05-20 | 181.000000 | 177.419998 | 180.740005 | 178.880005 | 28753461.0 | 172.961685 |
| 2021-05-21 | 180.000000 | 176.740005 | 178.880005 | 179.020004 | 32681504.0 | 173.097046 |
| 2021-05-24 | 180.979996 | 178.160004 | 180.100006 | 179.679993 | 18683315.0 | 173.735199 |
| 2021-05-25 | 181.619995 | 178.940002 | 180.320007 | 179.639999 | 26189150.0 | 173.696533 |
| 2021-05-26 | 179.572998 | 175.119995 | 178.839996 | 179.259995 | 40727970.0 | 173.329102 |
|        ... |        ... |        ... |        ... |        ... |        ... |        ... |
| 2022-05-13 | 150.544998 | 147.000000 | 147.559998 | 150.360001 | 40300228.0 | 150.360001 |
| 2022-05-16 | 152.983002 | 148.940002 | 150.600006 | 151.699997 | 48063820.0 | 151.699997 |
| 2022-05-17 | 157.080002 | 152.179993 | 152.380005 | 155.860001 | 50124597.0 | 155.860001 |
| 2022-05-18 | 157.220001 | 154.320007 | 157.020004 | 155.199997 | 30534183.0 | 155.199997 |
| 2022-05-19 | 155.684692 | 151.199997 | 155.279999 | 153.279999 | 30237812.0 | 153.279999 |

<br />

We will introduce two new columns:
- Previous close = close price from the day before
- Returns = $\frac{ClosePrice - PreviousClose}{PreviousClose}  $

<br />

New structure: 


|            |       High |        Low |       Open |      Close |     Volume |  Adj Close | previous_close |   returns |
|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|---------------:|----------:|
|       Date |            |            |            |            |            |            |                |           |
| 2021-05-20 | 181.000000 | 177.419998 | 180.740005 | 178.880005 | 28753461.0 | 172.961685 |            NaN |       NaN |
| 2021-05-21 | 180.000000 | 176.740005 | 178.880005 | 179.020004 | 32681504.0 | 173.097046 |     178.880005 |  0.000783 |
| 2021-05-24 | 180.979996 | 178.160004 | 180.100006 | 179.679993 | 18683315.0 | 173.735199 |     179.020004 |  0.003687 |
| 2021-05-25 | 181.619995 | 178.940002 | 180.320007 | 179.639999 | 26189150.0 | 173.696533 |     179.679993 | -0.000223 |
| 2021-05-26 | 179.572998 | 175.119995 | 178.839996 | 179.259995 | 40727970.0 | 173.329102 |     179.639999 | -0.002115 |
|        ... |        ... |        ... |        ... |        ... |        ... |        ... |            ... |       ... |
| 2022-05-13 | 150.544998 | 147.000000 | 147.559998 | 150.360001 | 40300228.0 | 150.360001 |     145.940002 |  0.030286 |
| 2022-05-16 | 152.983002 | 148.940002 | 150.600006 | 151.699997 | 48063820.0 | 151.699997 |     150.360001 |  0.008912 |
| 2022-05-17 | 157.080002 | 152.179993 | 152.380005 | 155.860001 | 50124597.0 | 155.860001 |     151.699997 |  0.027423 |
| 2022-05-18 | 157.220001 | 154.320007 | 157.020004 | 155.199997 | 30534183.0 | 155.199997 |     155.860001 | -0.004235 |
| 2022-05-19 | 155.684692 | 151.199997 | 155.279999 | 153.279999 | 30237812.0 | 153.279999 |     155.199997 | -0.012371 |


<br />

We will calculate the volatility $\sigma$ with the following formula

$\sigma = \sqrt{DatasetRowNumber} * ReturnsStandardDeviation$ 
[[source]](https://www.wallstreetmojo.com/volatility-formula/)

For risk free rate, we will use the UK 10 Year Gilt rate on the 19/05/2022:

$r = 0.01866$ [[source]](https://www.marketwatch.com/investing/Bond/TMBMKGB-10Y?countryCode=BX)

The spot value is the close value on the 19/05/2022:

$S = 153.279999$

The strike price is:

$K = 160$

The maturity date is 1 month so 

$t = \frac{31}{365} = 0.08493150684$

When we plug these values in our model we get the following call option price:

$C = 3.22$

<br />


## Running

### Installation

To install all the required packages run:

```
pip install -r requirements.txt
```

### Running the demo

```
jupyter notebook ipynb/
```