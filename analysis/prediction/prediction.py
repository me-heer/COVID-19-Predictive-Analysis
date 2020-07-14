import numpy as np 
import pandas as pd 
import pickle
import os

def ml_algorithm():
    output = ""
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'nation_level_daily.csv')
    df = pd.read_csv(file_path,parse_dates=['Date'])
    output += "Successfully read csv files. \n"
    dates = pd.date_range(start="2020-01-30",end="2020-07-07")
    confirmed = pd.DataFrame()
    confirmed['ds'] = dates
    confirmed['y'] = df[['Daily Deceased']]
    output += "Importing fbprophet... \n"
    from fbprophet import Prophet
    output += "Success. \n"
    output += "Creating model... \n"
    model = Prophet(interval_width=0.95)
    output += "Success. \n"
    output += "Fitting model... \n"
    model.fit(confirmed)
    output += "Success. \n"
    output += "Creating a future dataframe..."
    future = model.make_future_dataframe(periods=1) #periods are in days, change the number to change the output.
    output += "Success. \n"
    output += "Predicting... \n"
    forecast = model.predict(future)
    output += "Success. \n"
    output += "Saving model... \n"
    filename = os.path.join(module_dir, 'offline_model.sav')
    #filename = 'offline_model.sav'
    pickle.dump(model,open(filename,'wb'))
    output += "Success. \n"
    return output

#from fbprophet.plot import plot_plotly
#import plotly.offline as py
#py.init_notebook_mode()

#fig = plot_plotly(model, forecast)  # This returns a plotly Figure
#py.iplot(fig)