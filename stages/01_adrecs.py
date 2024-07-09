# Imports
# -------
import re
import os
import gzip
import pandas as pd
import urllib.request

class ADRECS(object):

    def __init__(self):

        # self.retrieve_data()
        self.process_data()

    def retrieve_data(self):

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
                        lines = file_in.readlines()
                        headers = lines.pop(0)
                        headers = re.split(r'\t+', str(headers))
                        df = pd.DataFrame(lines, columns=headers)
                        print (df)
                        break
                    # reaction_data = pd.read_csv(file, delimiter='\t')
                    # reaction_data.to_parquet(file)
            except Exception as e:
                print ('Conversion Failed: %s' % e)

if __name__ == '__main__':

    adrecs = ADRECS()
