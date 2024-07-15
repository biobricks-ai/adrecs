# Imports
# -------
import os
import gzip
import pandas as pd

_, _, files = next(os.walk('downloads'))
files = [ os.path.join('downloads', file) for file in files ]

os.makedirs('brick', exist_ok=True)

for file in files:

  out_file = os.path.join('brick', file.split('/')[1].split('.')[0] + '.parquet')

  try:

      if file.endswith('xlsx'):
          reaction_data = pd.read_excel(file)
          reaction_data.to_parquet(out_file)

      elif file.endswith('gz'):
          with gzip.open(file, 'rb') as file_in:
              lines = file_in.read().decode("utf-8").split('\n')
              data = [ line.split('\t') for line in lines ]
              headers = data.pop(0)
              df = pd.DataFrame(data, columns=headers)
              df.to_parquet(out_file)

  except Exception as e:
      print ('ADRECS File Conversion Failed: %s' % e)

