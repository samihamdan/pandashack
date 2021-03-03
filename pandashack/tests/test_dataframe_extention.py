from seaborn import load_dataset
import pandashack  # noqa: F401
from pandas.testing import assert_frame_equal

df_iris = load_dataset('iris')


def test_simple_mutate():
    df_assign = df_iris.copy().assign(
        new=lambda df: df.sepal_length / df.petal_width)
    df_mutate = df_iris.copy().mutate(
        new='sepal_length / petal_width'
    )
    assert_frame_equal(df_assign, df_mutate)


def test_mutate_with_methods():
    df_assign = df_iris.copy().assign(
        new=lambda df: df.sepal_length.mean() / df.petal_width)
    df_mutate = df_iris.copy().mutate(
        new='sepal_length.mean() / petal_width'
    )
    assert_frame_equal(df_assign, df_mutate)


def test_mutate_with_variables():
    a = 3
    df_assign = df_iris.copy().assign(
        new=lambda df: df.sepal_length * a / df.petal_width)
    df_mutate = df_iris.copy().mutate(
        new='sepal_length *@a / petal_width'
    )
    df_mutate_2 = df_iris.copy().mutate(
        new='sepal_length *a / petal_width'
    )
    assert_frame_equal(df_assign, df_mutate)
    assert_frame_equal(df_mutate, df_mutate_2)


def test_mutate_col_eq_var_use_var():
    petal_width = 5
    df_assign = df_iris.copy().assign(
        new=lambda df: df.sepal_length.mean() / petal_width)
    df_mutate = df_iris.copy().mutate(
        new='sepal_length.mean() / @petal_width'
    )
    assert_frame_equal(df_assign, df_mutate)


def test_mutate_col_eq_var_use_col():
    df_assign = df_iris.copy().assign(
        new=lambda df: df.sepal_length.mean() / df.petal_width)
    df_mutate = df_iris.copy().mutate(
        new='sepal_length.mean() / `petal_width`'
    )
    df_mutate_2 = df_iris.copy().mutate(
        new='sepal_length.mean() / petal_width'
    )
    assert_frame_equal(df_assign, df_mutate)
    assert_frame_equal(df_mutate, df_mutate_2)
