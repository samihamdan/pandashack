from functools import partial
import pandas as pd
import pandas_flavor as pf

from .dataframe_extention import mutate as dataframe_mutate


def grouped_pipe(df_grouped, func):
    df_ungrouped = df_grouped.apply(lambda x: x)

    return pd.concat(
        [df_ungrouped.loc[index, :].pipe(func)
         for label, index in df_grouped.groups.items()
         ])


@pf.register_groupby_method
def assign(df_grouped, **kwargs):
    return grouped_pipe(df_grouped, partial(pd.DataFrame.assign, **kwargs))


@pf.register_groupby_method
def mutate(df_grouped, **kwargs):
    return grouped_pipe(df_grouped, partial(dataframe_mutate, **kwargs))
