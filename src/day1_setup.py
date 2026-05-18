# verifying all libraries install correctly on the system..
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

print("yfinance version:", yf.__version__)
print("matplotlib version:", plt.matplotlib.__version__)
print("pandas version:", pd.__version__)
print("streamlit version:", st.__version__)
print("All libraries are installed and imported successfully!")