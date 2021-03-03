import sys
import pandas_flavor as pf

from .my_parser import translator


@pf.register_dataframe_method
def mutate(df, local_dict=None, global_dict=None, level=2, **kwargs):
    locals_dict = (
        sys._getframe(level).f_locals if local_dict is None else local_dict
    )
    globals_dict = (
        sys._getframe(level).f_globals if global_dict is None else global_dict
    )
    _dataframe = df.copy()
    for key, value in kwargs.items():
        trans = translator(_dataframe.columns)
        locals_dict["_dataframe"] = _dataframe

        _dataframe = eval(
            f"_dataframe.assign({str(key)}=lambda _df: {trans.translate(value)})",
            locals_dict,
            globals_dict,
        )

    return _dataframe
