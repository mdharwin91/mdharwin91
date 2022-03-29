import datetime
current_date = datetime.datetime.today()
flt_month = {
    'JAN' : '01',
    'FEB' : '02',
    'MAR' : '03',
    'APR' : '04',
    'MAY' : '05',
    'JUN' : '06',
    'JUL' : '07',
    'AUG' : '08',
    'SEP' : '09',
    'OCT' : '10',
    'NOV' : '11',
    'DEC' : '12',
    
}
line_2 = "CM1596/02.XXXXX.BLR"

fnd_dte = line_2.split('/')[1]
fnd_dte = fnd_dte.split('.')[0]
if len(fnd_dte) == 5:
    flt_day = fnd_dte[0:2]
    flt_mon = fnd_dte[2:5]
    flt_yr = str(current_date.year)
    flight_date = flt_yr+"-"+flt_month[flt_mon]+"-"+flt_day
    
if len(fnd_dte) == 2:
    flt_day = fnd_dte[0:2]
    flt_mon = str(current_date.month).zfill(2)
    flt_yr = str(current_date.year)
    flight_date = flt_yr+"-"+flt_mon+"-"+flt_day
if len(fnd_dte) == 9:
    flt_day = fnd_dte[0:2]
    flt_mon = fnd_dte[2:5]
    flt_yr = fnd_dte[5:9]
    flight_date = flt_yr+"-"+flt_month[flt_mon]+"-"+flt_day

print(flight_date)