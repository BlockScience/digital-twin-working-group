import matplotlib.pyplot as plt

def plot_index_price_backtest(historical_data, backtest_data):
    historical_data.prices_data["index_price"].plot(kind='line')
    backtest_data["index_price"].plot(kind='line')
    plt.title("Index Price Comparison")
    plt.legend(["Actual", "Model"])
    plt.show()
        
def plot_basket_price_backtest(historical_data, backtest_data):
    historical_data.prices_data["basket_price"].plot(kind='line')
    backtest_data["basket_price"].plot(kind='line')
    plt.title("Basket Price Comparison")
    plt.legend(["Actual", "Model"])
    plt.show()
    
def find_backtest_price_deviation(historical_data, backtest_data):
    return ((backtest_data[["index_price", "basket_price"]] - historical_data.prices_data) ** 2).mean()