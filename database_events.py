import urllib.request as urllib2
import json
import csv
import math
import datetime
import pyodbc
from datetime import datetime,timedelta

page = 1
num_results = 5000
pages = 1


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-7DALFVFS\SQLEXPRESS;'
                      'Database=Tickets;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

while page <= math.ceil(pages):

    content = urllib2.urlopen('https://api.seatgeek.com/2/events?taxonomies.name=concert&page=' +str(page)+ '&per_page='+str(num_results)+ '&client_id=MTcxMjY3NDF8MTU2MTEzMDkxNS44Nw').read()
    dict = json.loads(content)
    pretty_print = json.dumps(dict, indent=2)

    event_dict = {}

    total = dict.get('meta').get('total')
    pages = total/num_results

    # print(page)
    # print(pages)

    # prints all the performers
    for key in dict.get('events'):
        inner_dict = json.loads(json.dumps(key,indent=2))
        # event_dict[inner_dict.get('title')] =
        arr = [inner_dict.get('id'),inner_dict.get('announce_date'),inner_dict.get('score'),inner_dict.get('datetime_local'),
        inner_dict.get('stats').get('visible_listing_count'),inner_dict.get('stats').get('average_price'),inner_dict.get('stats').get('median_price'),
        inner_dict.get('stats').get('visible_listing_count'),inner_dict.get('stats').get('lowest_price'),inner_dict.get('stats').get('highest_price'),
        inner_dict.get('venue').get('postal_code'),inner_dict.get('venue').get('id'),inner_dict.get('venue').get('city'),inner_dict.get('venue').get('capacity')
        ,inner_dict.get('venue').get('state'),inner_dict.get('venue').get('metro_code')
        ,inner_dict.get('venue').get('address')
        ,inner_dict.get('venue').get('slug')
        ,inner_dict.get('venue').get('score')
        ,inner_dict.get('venue').get('name')
        ,inner_dict.get('venue').get('url')]

        performer_arr = []

        # prints all the performers
        if not(inner_dict.get('performers') is None):
            for performer in inner_dict.get('performers'):
                performer_arr.append(performer.get('slug'))
                performer_arr.append(performer.get('id'))
                performer_arr.append(performer.get('score'))
                if not performer.get('genres') is None:
                    performer_arr.append(performer.get('genres')[0].get('name'))
                else:
                    performer_arr.append("")

        # print(inner_dict.get('title'))

        # limits to the first 3 performers
        if (len(performer_arr) > 12):
            performer_arr = performer_arr[:12]

        arr.extend(performer_arr)

        event_dict[inner_dict.get('title')] = arr

        id = str(performer_arr[1])
        # print(inner_dict.get('id'))

        days_before = datetime.strptime(inner_dict.get('datetime_local')[:10],"%Y-%m-%d")


        days = (days_before.date()-datetime.today().date()).days

        # command = "exec dbo.insert_data_event_DB (?,?,?,?,?,?,?,?,?,?)"
        command = "insert into Event(Event_ID,Venue_ID,Artist_ID,Days_Before,Low_Price,Average_Price,Median_Price,High_Price,Listing_Count,Performer_2,Performer_3,URL)"
        values="\nvalues("+str(inner_dict.get('id'))+"," +str(inner_dict.get('venue').get('id'))+","+ id+","+ str(days)+","
        values+=("-1" if inner_dict.get('stats').get('lowest_price') == None else str(inner_dict.get('stats').get('lowest_price')))
        values+=","+str(("-1" if inner_dict.get('stats').get('average_price') == None else str(inner_dict.get('stats').get('average_price'))))
        values+=","+("-1" if inner_dict.get('stats').get('median_price') == None else str(inner_dict.get('stats').get('median_price')))
        values+=","+("-1" if inner_dict.get('stats').get('high_price') == None else str(inner_dict.get('stats').get('high_price')))
        values+=","+("-1" if inner_dict.get('stats').get('listing_count') == None else str(inner_dict.get('stats').get('listing_count')))
        #2 peformer and 3 performers
        #print("-1" if len(performer_arr) < 5 else str(performer_arr[5]))
        values+=","+("-1" if len(performer_arr) < 5 else str(performer_arr[5]))
        values+=","+("-1" if len(performer_arr) < 9 else str(performer_arr[9]))

        values+=",\'"+inner_dict.get('url')+"\')"
        print(command+values)

        cursor.execute(command+values)
        cursor.commit()



        # days = datetime.timedelta(days_before.date()-datetime.today())
        # print(str(days))
        # print(str(days).__class__)

        # lowest_price = inner_dict.get('stats').get('lowest_price') != null ? inner_dict.get('stats').get('lowest_price') : None

        # command = "insert into Event(Event_ID,Venue_ID,Artist_ID,Days_Before,Low_Price,Average_Price,Median_Price,High_Price,Listing_Count,URL)"
        # days_before = datetime.strptime(inner_dict.get('datetime_local')-datetime.date
        # values = "\nvalues("+str(inner_dict.get('id'))+","+str(inner_dict.get('venue').get('id'))+","+id+","+str(days)+","+str(inner_dict.get('stats').get('lowest_price'))+","+str(inner_dict.get('stats').get('average_price'))+","+str(inner_dict.get('stats').get('median_price'))+","+str(inner_dict.get('stats').get('highest_price'))+","+str(inner_dict.get('stats').get('visible_listing_count'))+",\'"+inner_dict.get('url')+"\')"
        # print(command+""+values)
        # cursor.execute(command+values)
        cursor.commit()




    page += 1

conn.commit()
conn.close()
