from rpy2 import robjects
from rpy2.robjects.pandas2ri import rpy2py_dataframe as to_df
from pandas.testing import assert_frame_equal
import pandashack  # noqa
from seaborn import load_dataset


df_iris = load_dataset('iris')


def test_groupby_mutate_compare_to_r():
    py_grouped = (df_iris
                  .copy()
                  .groupby('species')
                  .mutate(new='sepal_length.mean() + sepal_width')
                  )
    r = robjects.r
    r_grouped = to_df(r("""
    library('tidyverse')
    data('iris')

    iris %>%
        group_by(Species) %>%
        mutate(new = mean(Sepal.Length) + Sepal.Width)
    """))
    r_grouped.index = py_grouped.index
    r_grouped.columns = py_grouped.columns
    py_grouped.species = py_grouped.species.astype("category")
    assert_frame_equal(r_grouped, py_grouped)
