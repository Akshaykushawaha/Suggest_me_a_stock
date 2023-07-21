import yfinance as yf
import matplotlib.pyplot as plt

# Get the data for the Apple stock
def grap(stockSymbol):
    data = yf.download(stockSymbol, start="2022-01-01", end="2023-01-01")
    # Plot the closing price
    plt.plot(data["Close"])
    # Add a title and labels to the axes
    plt.title(stockSymbol + " Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    # Show the plot
    plt.savefig("./graphs/"+stockSymbol+".png")