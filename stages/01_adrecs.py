# Imports
# -------
import re
import os
import gzip
import click
import pandas as pd
import urllib.request

@click.command()
@click.option('--download_data', default=False, help='Run the downloading of the ADRECS data')
@click.option('--process_data', default=False, help='Process the Data into parquet files')

class ADRECS(object):

    def __init__(self, parameters={}):

        self.parameters = parameters

    def download_data(self):

        os.makedirs('data', exist_ok=True)

        data_links = {
          'drug_information.xlsx': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/Drug_information_v3.3.xlsx',
          'adr_terminology.xlsx': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADR_ontology_v3.3.xlsx',
          'drug_adr_interactions.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/Drug_ADR_v3.3.txt.gz',
          'drug_adr_interactions_matrix.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/Drug_ADR_Matrix_v3.3.txt.gz',
          'adr_severity_grade.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADReCS_ADR_Severity_Grade_v3.3.txt.gz',
          'adr_frequency.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADReCS_ADR_Frequency_v3.3.txt.gz',
          'drug_adr_relations_with_quantitative_features.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADReCS_Drug_ADR_relations_quantification_v3.3.txt.gz',
        }

        _ = [ urllib.request.urlretrieve(link, os.path.join('data', data)) for data, link in data_links.items() ]

    def process_data(self):

        _, _, files = next(os.walk('data'))
        files = [ os.path.join('data', file) for file in files ]

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
                        df.to_parquet('../brick/' + file.split('.')[0] + '.parquet')
            except Exception as e:
                print ('Conversion Failed: %s' % e)

def controller(
    download_data,
    process_data,
  ):

  adrecs = ADRECS()

  if download_data:
      adrecs.download_data()
  elif process_data:
      adrecs.process_data()
  else:
      pass

if __name__ == '__main__':

  controller()
