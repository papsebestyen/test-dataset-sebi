import sys

import pandas as pd
sys.path.append('C:\\Users\\papse\\Documents\\Github\\SSCUB\\sscutils')

from sscutils import dump_dfs_to_trepos
from src.trepos import karg_table
from src.raw_cols import CommonCols

if __name__ == "__main__":

    droot = sys.argv[1]
    
    karg_df = pd.read_csv(f"{droot}/karacsonygergely_01.csv")

    dump_dfs_to_trepos(None, [(karg_df, karg_table)])