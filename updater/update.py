from datetime import datetime, timedelta
import urllib.request, json 
from urllib.error import HTTPError
import analysis.prediction.prediction as predict

def get_latest_updated_date(last_updated_date):
    last_updated_date = last_updated_date
    i = 0
    while True:
        check_date = last_updated_date + timedelta(i)
        str_date = datetime.strftime(check_date,'%Y-%m-%d')
        print("Date: {}".format(str_date))
        try:
            url = "https://api.covid19india.org/v4/data-" + str_date + ".json"
            print("URL: {}".format(url))
            with urllib.request.urlopen(url) as url:
                print("Loading...")
                data = json.loads(url.read().decode())
                print("Loading Complete.")
                #print(data)
        except HTTPError as err:
            if err.code == 404:
                print("It didn't update on this date.")
                break
            else:
                raise
        i += 1
    i -= 1
    check_date = last_updated_date + timedelta(i)
    str_date = datetime.strftime(check_date,'%Y-%m-%d')
    print("The latest data available is on date: {}" .format(str_date))
    return str_date
    #print("UPDATE COMPLETE")

def update_models(last_updated_date):
    date = get_latest_updated_date(last_updated_date)
    output = ""
    output += predict.ml_algorithm(date)
    output += "Updated Successfully."
    return output