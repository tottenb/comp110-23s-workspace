__author__ = "730578942"


from csv import DictReader 


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    #loop through the keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Displays only the first n selected rows of a table."""
    result: dict[str, list[str]] = {}

    if num > len(table):
        return table
    else:
        for key in table:
            sub_list: list[str] = []
            data_to_get: list[str] = table[key]
            idx: int = 0
            while idx < num:
                sub_list.append(data_to_get[idx])
                idx += 1
            result[key] = sub_list
        return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Displays only the selected columns of a table."""
    result: dict[str, list[str]] = {}
    
    for i in column_names:
        result[i] = table[i]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Takes two tables and combines them into one."""
    result: dict[str, list[str]] = {}

    for i in table_1:
        result[i] = table_1[i]
    for i in table_2:
        if i in result:
            result[i] += table_2[i]
        else:
            result[i] = table_2[i] 
    return result


def count(x: list[str]) -> dict[str, int]:
    """Function will return a dictionary where the keys are the elements of the input list and the values are the counts."""
    dic: dict[str, int] = {}

    for i in x:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic








