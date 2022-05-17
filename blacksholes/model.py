from scipy.stats import norm
import numpy as np

def bs_call(S,K,T,r,sigma):
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))


class BlackSholesModel:
    def __init__(self, r, S, K, t, sigma):
        # risk-free interest rate 
        self.r = r
        # spot price of the asset
        self.S = S
        # strike price of the asset
        self.K = K
        # time to maturity
        self.t = t
        # volatility of the asset
        self.sigma = sigma

        self.d1 = None
        self.d2 = None
    
    def get_d1(self):
        """
        Returns the conditional probability. 
        If the spot price at maturity date is above the strike price, what is relation between
        the expected value to the current spot value
        """

        if self.d1:
            return self.d1

        self.d1 = (np.log(self.S/self.K) + (self.r + self.sigma**2/2) * self.t) / (self.sigma * np.sqrt(self.t))

        return self.d1


    def get_d2(self):
        """
        Returns the probability that the option is ITM, i.e. buy the security below its market value
        """

        if self.d2:
            return self.d2

        self.d2 = self.get_d1() - self.sigma * np.sqrt(self.t)

        return self.d2



    def get_call_price(self, round_d):
        """
            Returns the estimated price of a call option 
        """

        d1 = self.get_d1()
        d2 = self.get_d2()

        try:
            price = self.S * norm.cdf(d1, 0, 1) - self.K * np.exp(-self.r * self.t) * norm.cdf(d2, 0, 1)

            return round(price, round_d), True
        except Exception as e:
            print("Failed to calculate the call price: " + e)

            return None, False

    def get_put_price(self, round_d):
        """
            Returns the estimated price of a put option 
        """

        d1 = self.get_d1()
        d2 = self.get_d2()

        try:
            price = self.K * np.exp(-self.r * self.t) * norm.cdf(-d2, 0, 1) - self.S * norm.cdf(-d1, 0, 1)

            return round(price, round_d), True
        except Exception as e:
            print("Failed to calculate the put price: " + e)

            return None, False
