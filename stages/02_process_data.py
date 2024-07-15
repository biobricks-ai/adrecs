# Imports
# -------
import os
import gzip
import pandas as pd

_, _, files = next(os.walk('cache'))
files = [ os.path.join('cache', file) for file in files ]

for file in files:

  try:

      if file.endswith('xlsx'):
          reaction_data = pd.read_excel(file)
          reaction_data.to_parquet(file.split('.')[0] + '.parquet')

      elif file.endswith('gz'):
          with gzip.open(file, 'rb') as file_in:
              lines = file_in.read().decode("utf-8").split('\n')
              data = [ line.split('\t') for line in lines ]
              headers = data.pop(0)
              df = pd.DataFrame(data, columns=headers)
              df.to_parquet(file.split('.')[0] + '.parquet')

  except Exception as e:
      print ('ADRECS File Conversion Failed: %s' % e)

