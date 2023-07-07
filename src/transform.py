from __future__ import annotations

import contextlib
import itertools

import pandas as pd
from config import csv_encodings
from config import csv_separators
from config import dataset_folder_name
from config import dataset_value_dictionary
from config import dataset_years


class CSVReader:
    def __init__(self, folder_name: str, years: list[int], value_dictionary: dict[str, tuple[str, int]]):
        self.folder_name = folder_name
        self.years = years
        self.value_dictionary = value_dictionary

    def read_csv(self, year_index: int, file_number: int) -> pd.DataFrame:
        csv_file = f'{self.folder_name}/{self.years[year_index]}_{file_number}.csv'
        print(csv_file)

        for encoding, separator in itertools.product(csv_encodings, csv_separators):
            with contextlib.suppress(UnicodeDecodeError, KeyError, pd.errors.ParserError):
                df = pd.read_csv(csv_file, encoding=encoding, sep=separator)
                df = df.fillna(0)

                for column, (data_type, slice_size) in self.value_dictionary.items():
                    if slice_size is not None:
                        df[column] = df[column].astype(str).str.slice(0, slice_size)
                    df[column] = df[column].astype(data_type)

                df = self.trim_all_columns(df)

                return df
        raise ValueError('Failed to read CSV file with all encodings and separators')

    def clean_cep_column(self, df: pd.DataFrame, column_name: str = 'CEPConsumidor') -> pd.DataFrame:
        df[column_name] = df[column_name].str.replace('0.0', '')
        df[column_name] = df[column_name].str.replace('.', '0')
        df[column_name] = df[column_name].str[:-3] + '-' + df[column_name].str[-3:]
        return df

    def trim_all_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
        return df


def transform(year_index: int = 0, trimester_index: int = 1) -> pd.DataFrame:
    csv_reader = CSVReader(dataset_folder_name, dataset_years, dataset_value_dictionary)
    df = csv_reader.read_csv(year_index, trimester_index)
    df = csv_reader.clean_cep_column(df)

    return df
