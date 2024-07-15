# Imports
# -------
import os
import urllib.request

os.makedirs('downloads', exist_ok=True)

data_links = {
  'drug_information.xlsx': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/Drug_information_v3.3.xlsx',
  'adr_terminology.xlsx': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADR_ontology_v3.3.xlsx',
  'drug_adr_interactions.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/Drug_ADR_v3.3.txt.gz',
  'drug_adr_interactions_matrix.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/Drug_ADR_Matrix_v3.3.txt.gz',
  'adr_severity_grade.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADReCS_ADR_Severity_Grade_v3.3.txt.gz',
  'adr_frequency.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADReCS_ADR_Frequency_v3.3.txt.gz',
  'drug_adr_relations_with_quantitative_features.txt.gz': 'http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADReCS_Drug_ADR_relations_quantification_v3.3.txt.gz',
}

_ = [ urllib.request.urlretrieve(link, os.path.join('downloads', data)) for data, link in data_links.items() ]
