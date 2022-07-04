### ========= Nation =========

Extract data from Nation table:

Important links: 
https://developers.notion.com/reference/request-limits 
https://developers.notion.com/reference/post-database-query
https://developers.notion.com/reference/request-limits
https://www.notion.so/286284d1da044717a690fcf0140cb693?v=3a51932763594212b3934262bc4e55ee
 https://developers.notion.com/ 
https://www.youtube.com/watch?v=sdn1HgxLwEg  (Ref. link)
Get database id:
https://www.notion.so/<DATABASE_ID>?v=3a51932763594212b3934262bc4e55ee  
 
Example:
https://www.notion.so/286284d1da044717a690fcf0140cb693?v=3a51932763594212b3934262bc4e55ee  

Database id is: 286284d1da044717a690fcf0140cb693

##### Notion api call:
```import requests

url = "https://api.notion.com/v1/databases/286284d1da044717a690fcf0140cb693/query"

payload = {"page_size": 100}
headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json",
    "Authorization": "Bearer <>"
}

response = requests.post(url, json=payload, headers=headers)

data = (response.json())

```


### ========= Intuit =========


#### For Accounting Info 
```import requests
headers = {
    'accept': 'application/json',
    'authorization': 'Bearer <>',
    'content-type': 'application/json',
}
response = requests.get('https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365232551880/companyinfo/4620816365232551880?minorversion=12', headers=headers)
data=response.json()
```



#### Quickbooks authentication with python

```from intuitlib.client import AuthClient
from quickbooks import QuickBooks



auth_client = AuthClient(
        client_id=<>,
        client_secret=<>,
        access_token='<>',  # If you do not pass this in, the Quickbooks client will call refresh and get a new access token. 
        environment='sandbox',
        redirect_uri='http://localhost:8000/callback',
    )

client = QuickBooks(
        auth_client=auth_client,
        refresh_token='AB116653187892SM66PPZ7S4GKKBsfv7ciJkiY8x5KZD4lLvzh',
        company_id='4620816365232551880',
    )

profit_and_loss =client.get_report(report_type='ProfitAndLoss')

```



##### Questions:
1. which data do you want extract data from this app 
2. which type of data do you want 
3. Do you have any reference how we can get the data 
4. Should we export all data in excel and then process it?