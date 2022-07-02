import json;import datetime;from datetime import timedelta;import os, zipfile;
import requests
import time
import pytz
from pytz import timezone
import datetime


base_url = 'https://api.what-sticks-health.com'


def add_activity_util(payload, login_token):
  print('added activity')
  print(payload)
  print(login_token)
  url_add_activity=base_url + "/add_activity"
  headers = {'x-access-token':login_token, 'Content-Type': 'application/json'}
  response = requests.request("POST", url_add_activity, headers=headers, data=str(json.dumps(payload)))
  print(response.status_code)

def delete_row_util(act_type, payload, login_token):
  print('delete_row util')

  if act_type=='User Activity':# User activity deltee

    url_delete_activity_user = base_url + '/delete_user_activity'
    headers = {'x-access-token':login_token, 'Content-Type': 'application/json'}
    response = requests.request('DELETE',url_delete_activity_user, headers=headers, data=str(json.dumps(payload)))


  elif act_type== 'Polar':# Polar actiivty delete
    url_delete_activity_polar = base_url + '/delete_polar_activity'
    headers = {'x-access-token':login_token, 'Content-Type': 'application/json'}
    response = requests.request('DELETE',url_delete_activity_polar, headers=headers, data=str(json.dumps(payload)))

  elif act_type == 'Oura Sleep':# Oura sleep delete
    url_delete_oura_sleep = base_url + f'/delete_oura_sleep'
    headers = {'x-access-token':login_token, 'Content-Type': 'application/json'}
    response = requests.request('DELETE',url_delete_oura_sleep, headers=headers, data=str(json.dumps(payload)))

  if response.status_code == 200:
    print('deleted record type:', act_type)
    print(payload)
  print(response.status_code)

def table_api_util(login_token):

  url_get_activities=base_url + '/kivy_table01'
  headers = {'x-access-token':login_token, 'Content-Type': 'application/json'}
  response = requests.request('GET',url_get_activities, headers=headers)
  response_dict = json.loads(response.text)

  row_data_list=[
    [i[0],convert_datetime(i[1]),i[2], make_date_string(i[1]),h] for h,i in enumerate(response_dict['content'])
    ]
  print('****row_data_list created****')
  return row_data_list


def convert_datetime(date_time_str):
    try:
        date_time_obj = datetime.datetime.strptime(date_time_str, '%a, %d %b %Y %H:%M:%S %Z')
    except ValueError:
        # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
        print("""There is an error converting datetimes in
        scroll_table_data.py or with API call to kivy_table01""")
    return date_time_obj.strftime("%m/%d/%Y %-I:%M %p")
    # return date_time_obj.strftime("%b%-d '%-y %-I:%M%p")


def make_date_string(date_time_str):
    date_time_obj = datetime.datetime.strptime(date_time_str, '%a, %d %b %Y %H:%M:%S %Z')
    return date_time_obj.strftime('%Y%m%d')
