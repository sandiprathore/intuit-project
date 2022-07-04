from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

def get_api_data():
        import requests
        import pandas as pd
        import psycopg2
        from sqlalchemy import create_engine
        headers = {
            'accept': 'application/json',
            'authorization': 'Bearer eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..syWOqKleGgc7ZCQfb6ks6w.W5gjB6nUh9Fe_eRh0NW_ve0CD2wIEYdI9qjnhyINInZDzLHqxfOmNgbPYutJqubGJ5Sca8aIQdYDOYChqITiQHtWNuFLxDmIsjUBRnRXR_Puoo-1_uMqc94aQc_7vVUOegPlOngnAc5hxSabbygv_rSRZk78ff-lfA5qZQ_N92o0hBCHHBaP5fikjN1FGwqAOOz_b3bsMoAm8_YJl7UMVNuvmMMdLotq9JzKoWaxlRD7TAOdcbtDwVQh5kvRH9UBZwyO4PHUIy5lfSAGOaeIHwIvCq81jviehO5PUNump4Sp-UaTQpHFz3oC2mBtF0n-x5sNC-c5biTeqqgZ2ugBYFzHCT2NuVWKa0FETzqYam4VxMANe1LLePl3y4UtgZ0-M-7buYBUj7rY1-jrUX7h5eyVb4zjfPT4st0M0OFnY07xU-q24OU-m8tToRuGvis9RBHZGSrTiMBi-t-G1NxgoNR-9HeTtZ2d8v-ooo816guXa69AuwPC1HWVrkfjAh7w7_aVj8E8HYh9PsOZGrLNCeJv_PAIpOXOCKDo7Sfd7RoOE5vu9eqtDI_e8FherMlz26tEL0knL6wdc11xslNpHRfXKVVmcPQX2RDgSOGO7DmHu4FfHVxZvw23-zLojYeDFrbhGQlhqZQVhfyHPJhjaByT54mOu1EZmWNeMJxRE69VXvcEwlKTXGETgwBbPii-XXRIQpLdffSCP4DhUj-FsQ6IDTga-Bk3V6JklOXbe4QnfS8gvMsn4RFqGV-PoOlNryDNCHv5N7eK_63sE9aiPiyVlADl78THoymQhCU1QZh0JmOGCUTIq9DQ2UU3QyJuUQ1o1Dv1iccFknNM7r2TIRhEShJKM1Lq2iTPWaQ10-3r6fiqPzxVNhyRFSmX7cQI0izCEhkstntJ_BjTTp4iAg.BFPK8xSbKoefpoNkqfxOHQ',
            'content-type': 'application/json',
        }
        response = requests.get('https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365232551880/companyinfo/4620816365232551880?minorversion=12', headers=headers)
        data = response.json()
        df = pd.DataFrame(data)

        # establish connections
        conn_string = 'postgres://postgres:<password>@<host>/<database>'
        db = create_engine(conn_string)
        conn = db.connect()
        conn1 = psycopg2.connect(
            database="<database>",
        user='username',
        password='<password>',
        host='<host>',
        port= '5432'
        )

        conn1.autocommit = True
        cursor = conn1.cursor()

        # drop table if it already exists
        cursor.execute('DROP TABLE IF EXISTS <TABLE_NAME>')
        sql = '''CREATE TABLE <TABLE_NAME>(id int,
                day int, 
                airline char(20),
                destination char(20));'''
        cursor.execute(sql)

        # converting data to sql
        df.to_sql('<table_name>', conn, if_exists= 'replace')

        # fetching all rows
        sql1='''select * from table_name;'''
        cursor.execute(sql1)
        for i in cursor.fetchall():
            print(i)
        conn1.commit()
        conn1.close()

with DAG('intuit_project_api_dag',
        schedule_interval=None,
        start_date=datetime(2019, 1, 10), catchup=False) as dag:

    # task_1
    intuit_project_api_data =  PythonOperator(
            task_id='get_api_data',
            python_callable=get_api_data,
            provide_context=True
            )