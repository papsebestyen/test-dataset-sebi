from sscutils import dump_dfs_to_trepos

from .trepos import karg_table
from .raw_cols import CommonCols, EventsCols

def create_subsets(subset_name, person_ids=None, only_success=False):
    """create subsets that are described in the config of the repo"""
    karg_df = karg_table.get_full_df().loc[lambda df: df['time'].apply(lambda x: x.strip().split('-')[0] == '2020')]
    # pers_df = persons_table.get_full_df().loc[person_ids or slice(None), :]
    # ev_df = events_table.get_full_df().loc[
    #     lambda df: df[CommonCols.person_id].isin(pers_df.index)
    #     & (df[EventsCols.success] | (not only_success)),
    #     :,
    # ]
    # obj_df = objects_table.get_full_df().loc[ev_df[CommonCols.object_id].unique(), :]

    dump_dfs_to_trepos(subset_name, [(karg_df, karg_table)])
