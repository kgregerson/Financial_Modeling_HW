def LookbackOption(pricing_engine, option, data):
    expiry = option.expiry
    strike = option.strike
    (spot, rate, volatility, dividend) = data.get_data()
    steps = pricing_engine.steps
    h = expiry/steps
    payoff = []
    for i in range(steps):
        S = [spot]
        for i in range(int(steps)):
            X = np.random.normal()
            S.append(S[i]*np.exp((rate - (0.5 * volatility * volatility)* (1/365) + volatility * X * np.sqrt(1/365))))
        m = np.min(S)
        M = np.max(S)
        ST = S[expiry]
        payoff.append(M-m) #some payoff function here
    mean = np.mean(payoff)
    premium = mean * (1+rate)^-expiry
    
    return(premium)