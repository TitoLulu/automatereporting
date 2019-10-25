#import required libraries
import pandas as  pd
import numpy as np 
import requests
from datetime import datetime, timedelta
from apiclient import discovery
from google.oauth2 import service_account
from googleapiclient.discovery import build
import httplib2

#get yesterday's date
today = datetime.today()
yesterday = today - timedelta(days=1)
yesterday =yesterday.strftime('%Y-%m-%d')#format it

#Define the url with the desired endpoint
base_url ='https://newsapi.org/v2/everything'

#define the query string parameters to the data we need
params = {
    'q':'artificial intelligence',
    'to':yesterday,
    'from':yesterday,
    'apikey':'962acc6f664a4d6d8bf498496a06d790',
    'lan':'en',
    'pageSize':100
}

#construct the api call and make a GET request per the docs
response = requests.get(base_url, params=params)

#Store the results in a variable as json
total_results = response.json()

#Add the data to a df
#Create a list for each field
content, title, url, name, date =[],[],[],[],[]

#loop through the json and add the data to the list
for each in total_results['articles']:
    #check for articles that only have titles and no content
    #add Nan if we don't find any
    if 'content' in each:
        content.append(each['content'])
    else:
        content.append(np.nan)

    title.append(each['title'])
    url.append(each['url'])
    name.append(each['source']['name'])
#put the lists into a df and transpose them
df = pd.DataFrame([title, content,url, name, date]).T

#add column  names
df.columns =['title','content','url','site','date']

#Put the data into the google sheet
#define the scopes
scopes =['https://www.googleapis.com/auth/spreadsheets']
credentials = service_account.Credentials.from_service_account_file('C://Users//tmagero//Downloads//idyllic-tendril-256907-d68af7caf5e8.json'
,scopes=scopes)



#Build the service

service = discovery.build(
    'sheets',
    'v4',
    credentials=credentials
)

#Format the df to pass into the sheets api
#this will create a df wih the headers as the first row
with_headers = pd.DataFrame(np.vstack([df.columns, df]))

#put each column into a list
values = [with_headers[each_col].tolist() for each_col in with_headers]

#Define the preadsheet id
spreadsheet_id ='1JUA4JdXUpAkiMHcb4J7EXQJWWDMbmgQ5vxJ-P4Qk-bA'
sheet_name = 'Sheet1'

#Define the  range for data
range_ = sheet_name + '!A2:E'

#how the input data should be interpreted
value_input_option ='RAW' #store values as they are

#How the input data should be inserted
insert_data_option ='INSERT_ROWS' #rows are inserted as opposed to overwriting

#Define the data fields and set mahor dimension to columns
#the default is rows which will transpose each column as a row which you don't want

data = {'values':values,
'majorDimension':'COLUMNS'}

# Build the request and execute the api call
request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, 
                                                 range=range_, 
                                                 valueInputOption=value_input_option, 
                                                 insertDataOption=insert_data_option, 
                                                 body=data).execute()

# Print out the number of rows to verify
print('Number of rows inserted {}'.format(request['updates']['updatedRows']))



