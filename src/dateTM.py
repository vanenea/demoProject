from datetime import date
from dateutil.relativedelta import relativedelta



if __name__ == '__main__':
    today = date.today()
    print(today.strftime("%y/%m/%d"))
    tomorrow = today + relativedelta(months=-1)
    print(tomorrow.strftime("%y/%m/%d"))

