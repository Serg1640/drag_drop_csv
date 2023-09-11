import numpy as np
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
df1['T7'] = df1['T7'].astype(float)
df1['T6'] = df1['T6'].astype(float)
df1['T5'] = df1['T5'].astype(float)
df1['T4'] = df1['T4'].astype(float)
df1['T3'] = df1['T3'].astype(float)
df1['T2'] = df1['T2'].astype(float)
df1['T1'] = df1['T1'].astype(float)
df1['M3'] = df1['M3'].astype(float)
df1['M2'] = df1['M2'].astype(float)
df1['ВентГл'] = df1['ВентГл'].astype(float)
df1['ДВ1_Гц'] = df1['ДВ1_Гц'].astype(float)
df1['ВентВытяж'] = df1['ВентВытяж'].astype(float)
df1['НасосПолив'] = df1['НасосПолив'].astype(float)
df1['b3_mm'] = df1['b3_mm'].astype(float)

# заполнение отсутствующих данных в столбцах О2 (если значение равно 0) средним значением от предыдущей и следующей
# ячейки
df1.loc[(df1.O2 == 0), 'O2'] = (df1['O2'].shift() + df1['O2'].shift(-1))/2



# заполнение отсутствующих данных в столбце Т7 (если значение равно 0) средним значением от предыдущей и следующей
# ячейки
df1.loc[(df1.T7 == 0), 'T7'] = (df1['T7'].shift() + df1['T7'].shift(-1))/2

df1.to_excel('01.0412.xlsx', index=False)


