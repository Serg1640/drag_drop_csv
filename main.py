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

# заполнение отсутствующих данных в столбце О2 (если значение равно 0) средним значением от предыдущей и следующей
# ячейки
df1.loc[(df.O2 == 0), 'O2'] = (df1['O2'].shift() + df1['O2'].shift(-1))/2


df1.to_excel('01.0412.xlsx', index=False)


