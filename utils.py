import json;import datetime;from datetime import timedelta;import os, zipfile;
import requests
import time
import pytz
from pytz import timezone
import datetime


base_url = 'https://api.what-sticks-health.com'



def table_api_util(login_token):

  url_get_activities=base_url + '/kivy_table01'
  headers = {'x-access-token':login_token, 'Content-Type': 'application/json'}
  response = requests.request('GET',url_get_activities, headers=headers)
  print('url_get_activities:::', url_get_activities)
  response_dict = json.loads(response.text)

  # print('response_list:::',type(response_dict['content']))
  # print('response_list:::', response_dict['content'][0])

  row_data_list=[
    [i[0],convert_datetime(i[1]),i[2], make_date_string(i[1]),h] for h,i in enumerate(response_dict['content'])
    ]
  print('****row_data_list created****')
  # print(row_data_list[0:3])
  return row_data_list

def convert_datetime(date_time_str):
    try:
        date_time_obj = datetime.datetime.strptime(date_time_str, '%a, %d %b %Y %H:%M:%S %Z')
    except ValueError:
        # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
        print("""There is an error converting datetimes in
        scroll_table_data.py or with API call to kivy_table01""")
    # return date_time_obj.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time_obj.strftime("%b%-d '%-y %-I:%M%p")#<------Potential hangup!***************!

def make_date_string(date_time_str):
    date_time_obj = datetime.datetime.strptime(date_time_str, '%a, %d %b %Y %H:%M:%S %Z')
    return date_time_obj.strftime('%Y%m%d')
