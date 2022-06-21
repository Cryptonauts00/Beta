import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

from api.lookintobitcoin_api import lib_fetch
from metrics.base_metric import BaseMetric
from utils import add_common_markers


class TestMetric(BaseMetric):
    @property
    def name(self) -> str:
        return 'TestMetric'

    @property
    def description(self) -> str:
        return 'Test Metric'

    def _calculate(self, df: pd.DataFrame, ax: list) -> pd.Series:
        
        date_list = []
        val_list = []
        for i in range(0,4050):
            date_list.append(pd.Timestamp('2022-06-20'))
            val_list.append(0.6 + np.random.uniform(-0.1,0.1))

        data = {'Date': date_list,
                'test': val_list}

        df = pd.DataFrame(data)

        print("first_elem", df.iloc[0])
        print("last_elem", df.iloc[-1])

        df['TestIndex'] = df["test"] - 0.1

        print(df)

        ciao capo, il codice è in errore!

        return df['TestIndex']
