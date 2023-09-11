# import numpy as np
import pandas as pd
import os

os.chdir(r'C:\Users\Sergey\Documents\pythonProject\dataAnalysis')

# открытие рабочего файла, выгруженного из SCADA
df = pd.read_excel('01.04.xlsx')

# Удаление дублирующих наименований столбцов из оригинального файла
df1 = df[df['T7'] != 'T7'].drop_duplicates()

# удаление всех строк со значением NaN
df1.dropna()

# конвертация значений столбцов Т7, T6, T5, T4, T3, T2, T1, M3, M2, ВентГл, ДВ1_Гц, ВентВытяж, НасосПолив,
# b3_mm во float
df1['T7'] = df1['T7'].astype(float)  # датчик температуры приточного воздуха, С
df1['T6'] = df1['T6'].astype(float)  # датчик температуры вытяжного воздуха, С
df1['T5'] = df1['T5'].astype(float)  # датчик температуры рециркуляционного воздуха, С
df1['T4'] = df1['T4'].astype(float)  # датчик температуры воздуха в барокамере, С
df1['T3'] = df1['T3'].astype(float)
df1['T2'] = df1['T2'].astype(float)  # датчик температуры сырья, С
df1['T1'] = df1['T1'].astype(float)  # датчик температуры сырья, С
df1['M3'] = df1['M3'].astype(float)  # заслонка приточного воздуха
df1['M2'] = df1['M2'].astype(float)  # заслонка рециркуляционного воздуха
df1['ВентГл'] = df1['ВентГл'].astype(float)
df1['ДВ1_Гц'] = df1['ДВ1_Гц'].astype(float)
df1['ВентВытяж'] = df1['ВентВытяж'].astype(float)
df1['НасосПолив'] = df1['НасосПолив'].astype(float)
df1['b3_mm'] = df1['b3_mm'].astype(float)

# заполнение отсутствующих данных в столбцах О2 (если значение равно 0) средним значением от предыдущей и следующей
# ячейки
df1.loc[(df1.O2 == 0), 'O2'] = (df1['O2'].shift() + df1['O2'].shift(-1)) / 2

# заполнение отсутствующих данных в столбцах Т7, T6, T5, T4, T3, T2, T1  (если значение равно 0) средним значением от
# предыдущей и следующей ячейки
df1.loc[(df1.T7 == 0), 'T7'] = (df1['T7'].shift() + df1['T7'].shift(-1)) / 2
df1.loc[(df1.T6 == 0), 'T6'] = (df1['T6'].shift() + df1['T6'].shift(-1)) / 2
df1.loc[(df1.T5 == 0), 'T5'] = (df1['T5'].shift() + df1['T5'].shift(-1)) / 2
df1.loc[(df1.T5 == 0), 'T4'] = (df1['T4'].shift() + df1['T4'].shift(-1)) / 2
df1.loc[(df1.T5 == 0), 'T3'] = (df1['T3'].shift() + df1['T3'].shift(-1)) / 2
df1.loc[(df1.T5 == 0), 'T2'] = (df1['T2'].shift() + df1['T2'].shift(-1)) / 2
df1.loc[(df1.T5 == 0), 'T1'] = (df1['T1'].shift() + df1['T1'].shift(-1)) / 2

"""
Анализ данных из файла excel
"""

# нахождение минимального значения кислорода
row_min = df1[df1.O2 == df1.O2.min()]

print('Строка при минимальной концентрации кислорода: \n'
      '', row_min.to_string(), '\n')

# получение строки с максимальным значением кислорода
row_max = df1[df1.O2 == df1.O2.max()]

print('Строка при максимальной концентрации кислорода: \n'
      '', row_max.to_string())


df1.to_excel('01.0412.xlsx', index=False)
