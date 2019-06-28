import sqlite3
import pandas as pd
import datetime

def df_from_db() :
    cnx = sqlite3.connect(r'../../database/newbit.db')  # 각자 주소에 맞게 변경해주세요
    df = pd.read_sql_query("SELECT * FROM news", cnx)     # create the dataframe from a query

    # 다음 컬럼을 String에서 다시 리스트로 변환해야 이미지 생성 프로세스 가능
    df['category'] = df['category'].apply(lambda x: x if x == '' else x.split(','))  # str에서 list로 변환
    df['tokenized_doc'] = df['tokenized_doc'].apply(lambda x: x.split(','))  # str에서 list로 변환
    df['tokenized_title'] = df['tokenized_title'].apply(lambda x: x.split(','))  # str에서 list로 변환
    df['date'] = df['date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))  # str에서 datetime으로 변환

    return df
