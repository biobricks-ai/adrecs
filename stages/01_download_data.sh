#!/usr/bin/env bash

mkdir -p . /download

wget -P download/ http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/Drug_information_v3.3.xlsx
wget -P download/ http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADR_ontology_v3.3.xlsx
wget -P download/ http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/Drug_ADR_v3.3.txt.gz
wget -P download/ http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/Drug_ADR_Matrix_v3.3.txt.gz
wget -P download/ http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADReCS_ADR_Severity_Grade_v3.3.txt.gz
wget -P download/ http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADReCS_ADR_Frequency_v3.3.txt.gz
wget -P download/ http://bioinf.xmu.edu.cn/ADReCS/download/v3.3/ADReCS_Drug_ADR_relations_quantification_v3.3.txt.gz
