from dylan.payoff import VanillaPayoff, call_payoff, put_payoff
from dylan.engine import BinomialPricingEngine, EuropeanBinomialPricer
from dylan.marketdata import MarketData
from dylan.option import Option

def EurpeanBinomialPricer(pricing_engine, option, data):
    """
    The binomial option pricing model for an American option.

    Args:
        pricing_engine (PricingEngine): a pricing method via the PricingEngine interface
        option (Payoff):                an option payoff via the Payoff interface
        data (MarketData):              a market data variable via the MarketData interface

    """

    expiry = option.expiry
    strike = option.strike
    (spot, rate, volatility, dividend) = data.get_data()
    steps = pricing_engine.steps
    nodes = steps + 1
    h = expiry / steps 
    u = np.exp((rate * h) + volatility * np.sqrt(h)) 
    d = np.exp((rate * h) - volatility * np.sqrt(h))
    pu = (np.exp(rate * h) - d) / (u - d)
    pd = 1 - pu
    disc = np.exp(-rate * expiry)
    spotT = 0.0
    payoffT = 0.0
    
    for i in range(nodes):
        spotT = spot * (u ** (steps - i)) * (d ** (i))
        payoffT += option.payoff(spotT)  * binom.pmf(steps - i, steps, pu)  
    price = disc * payoffT 
     
    return price
    
def AmericanBinomialPricer(pricing_engine, option, data):
    expiry = option.expiry
    strike = option.strike
    (spot, rate, volatility, dividend) = data.get_data()
    steps = pricing_engine.steps
    nodes = steps + 1
    h = expiry/steps
    u = np.exp((rate * h) + volatility * np.sqrt(h))
    d = np.exp((rate* h) - volatility * np.sqrt(h))
    pu = (np.exp(rate * h) - d)/ (u - d)
    pd = 1 - pu
    disc = np.exp(-rate * expiry)

    V = [[0.0 for k in range(i + 1)] for j in range (steps + 1)]
    
    for i in range(nodes):
        
        V[i][k] = max(spot * (u ** (steps - i)) * (d**(i)) - strike, 0.0)
        
    for i in range(steps - 1, -1, -1):
        for k in range(i + 1):
            V1 = (disc * V[i+1][k+1] + pd * V[i+1][k])
            V2 = max(spot - strike, 0)
            V[i][k] = max(V1,V2)
    return V[0][0]


                         
            
            
            
    
    
    
        
        
        
        
    
        