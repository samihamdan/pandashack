import re


class translator:
    """
    0) Tokenize everything
    1) Strings are kept the same
    2) If you have something inside of ` ` it will be interpret as Column
    3) Exchange column names unless @ is infront
    4) remove @ 

    """

    def __init__(self, columns):
        self._columns = columns
        self.find_string = re.compile(r"([\"].*[\"]|[\'].*[\'])")
        self.find_quote = re.compile(r"(`.*`)")

    def translate(self, string):
        _string = " " + string + " "  # hacky for now
        translated = "".join(
            [self.translate_tocken(token) for token in self.tokenize(_string)]
        )

        translated = translated[1:-1]  # hacky getting rid of whitespace
        return translated

    def translate_tocken(self, token):
        if self.find_string.match(token) is not None:
            return token
        elif self.find_quote.match(token) is not None:
            return fr'_df["{token[1:-1]}"]'

        else:
            return self.replace_column_names(token)

    def tokenize(self, string):
        return [
            token
            for str_splitted in self.find_string.split(string)
            for token in self.split_by_quotes(str_splitted)
        ]

    def replace_column_names(self, string):
        """replaces column names with _df["column_name"]
        unless there is a @ infront of it. Then it only removes the @
        """
        find_columns = re.compile(fr'([^@\w])({"|".join(self._columns)})\b')
        return find_columns.sub(r'\1_df["\2"]', string).replace(r"@", "")

    def split_by_quotes(self, string):
        """splits by quoting signs ``which are not inside of a nested string.
        """
        if self.find_string.match(string) is None:
            return self.find_quote.split(string)
        else:
            return [string]
