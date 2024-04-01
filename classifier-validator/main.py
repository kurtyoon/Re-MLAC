import pandas as pd
from datetime import datetime

import requests
import os

from utils.utility import from_dataframe
from utils.utility import tic, toc
from utils.utility import category
from dotenv import load_dotenv

load_dotenv()
DATA_PATH = os.getenv('DATA_PATH')
PRED_PATH = os.getenv('PRED_PATH')
PRED_URL = os.getenv('PRED_URL')

for label in category:
    tic()
    data = pd.read_csv(f'{DATA_PATH}/{label.lower()}.csv')
    length = len(data)

    for idx in range(length):
        row = data.iloc[idx]

        ip = row['srcip']
        port = row['sport'].astype(str)
        timestamp = str(datetime.now())
        index = int(row['index'])

        request_data = {
            'ip': ip,
            'port': port,
            'timestamp': timestamp,
            'body': [],
            'packet_info': from_dataframe(row)
        }

        response = requests.get(PRED_URL, json=request_data)
        attack_type = response.json().get('attack_type')
        pred = pd.DataFrame({
            'index': [index],
            'origin': [label],
            'predict': [attack_type]
        })
        pred.to_csv(f'{PRED_PATH}/{label.lower()}.csv', mode='a', header=False, index=False)
    toc()
    