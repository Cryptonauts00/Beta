import traceback
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
from sty import fg, bg, rs

from api.cbbiinfo_api import cbbi_fetch
from utils import send_error_notification


class BaseMetric(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def _calculate(self, df: pd.DataFrame, ax: list) -> pd.Series:
        pass

    def _fallback(self, df: pd.DataFrame) -> pd.Series:
        df = df.merge(cbbi_fetch(self.name), on='Date', how='left')
        df['Value'].ffill(inplace=True)

        return df['Value']

    def calculate(self, df: pd.DataFrame, ax: list) -> pd.Series:
        try:
            return self._calculate(df, ax)
        except Exception as ex:
            traceback.print_exc()

            send_error_notification(ex)

            print(fg.black + bg.yellow + f' Requesting fallback values for {self.name} (from CBBI.info) ' + rs.all)
            return self._fallback(df)
