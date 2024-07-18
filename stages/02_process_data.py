# Imports
# -------
import re
import pathlib
import pandas as pd

extensions = ['txt.gz', 'xlsx']
extensions_re = re.compile(r'\.(' + '|'.join(re.escape(ext) for ext in extensions) + r')$')

files = filter( lambda item: item.is_file(), pathlib.Path('download').rglob('*') )

brick_dir = pathlib.Path('brick')
brick_dir.mkdir(exist_ok=True)

files_w_neg1_NA = [
        'ADReCS_ADR_Severity_Grade_v3.3.txt.gz',
        'ADReCS_ADR_Frequency_v3.3.txt.gz'
      ]

for file in files:
    out_basename = re.sub(extensions_re, '.parquet', file.name )
    out_file = brick_dir / file.relative_to('download').with_name( out_basename )

    if file.match('*.xlsx'):
        reaction_data = pd.read_excel(file)
        reaction_data.to_parquet(out_file)

    elif file.match('*.txt.gz'):
        df = pd.read_csv(file, sep='\t', encoding='utf-8', low_memory=False)
        if(file.name in files_w_neg1_NA):
            df = df.replace({'-1': pd.NA, -1.0: pd.NA})
        if(file.name == 'ADReCS_ADR_Severity_Grade_v3.3.txt.gz'):
            for c in df.filter(regex=r'^BADD_', axis=1).columns:
                df[c] = df[c].astype('category')
        df.to_parquet(out_file)

    else:
        raise Exception('Unknown File Found: %s' % file)


