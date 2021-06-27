import pandas as pd
import calendar

import datetime

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)

account_st = pd.read_csv("python_scripts/Account_Statement_Export_2015_2021.csv")
account_st["date"]= pd.to_datetime(account_st["date"],dayfirst = True)

account_st["date"][account_st.shape[0]-1].to_pydatetime()

start_year = account_st["date"][0].to_pydatetime().year


end_year = account_st["date"][account_st.shape[0]-1].to_pydatetime().year

if (end_year-start_year)==0:
    end_month = account_st["date"][account_st.shape[0]-1].to_pydatetime().month
    start_month = account_st["date"][0].to_pydatetime().month
    
else:
    end_month = 12
    start_month = 1

print("Monthly Stats")

for year in range(start_year, end_year+1):
    for month in range(start_month, end_month+1):
        start_date = f'{year}-{month}-01'
        end_date = last_day_of_month(datetime.date(year, month, 1))

        # account_st.query('date >= @start_date and date <= @end_date')

        total_spent = account_st.query('date >= @start_date and date <= @end_date')["DrAmount"].sum()
        total_received = account_st.query('date >= @start_date and date <= @end_date')["CrAmount"].sum()

        print ( f"{calendar.month_name[month]}-{year}, {int(total_spent/1000)}, {int(total_received/1000)}")
        
print("\nYearly Stats")

for year in range(start_year, end_year+1):
    start_date = f'{year}-01-01'
    end_date = last_day_of_month(datetime.date(year, 12, 1))

    total_spent = account_st.query('date >= @start_date and date <= @end_date')["DrAmount"].sum()
    total_received = account_st.query('date >= @start_date and date <= @end_date')["CrAmount"].sum()

    print ( f"{year}, {round(total_spent/100000,2)}, {round(total_received/100000,2)}, {round((total_received-total_spent)/100000,2)}")