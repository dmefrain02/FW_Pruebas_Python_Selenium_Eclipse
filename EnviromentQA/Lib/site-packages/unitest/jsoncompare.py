import json
import re

from typing import Dict, List, Optional

TIMESTAMP_REGEX = "(\d{4}-\d?\d-\d?\d)T((?:2[0-3]|[01]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9])Z$"  # Regex to detect timestamps
INTEGER = "[0-9]+$"


def _expand_list_values(json_list: list, ignore_types: List[type] = [], ignore_regex: Optional[dict] = None) -> list:
    elements = []
    for value in json_list:
        value_type = type(value)
        if value_type == dict:  # Value is a dict, extract it
            elements.append(filter_values(value, ignore_types=ignore_types, ignore_regex=ignore_regex))
        elif value_type == list:
            elements.append(_expand_list_values(value, ignore_types=ignore_types, ignore_regex=ignore_regex))
        else:
            if value_type not in ignore_types:  # Value is not explicitely ignored
                if ignore_regex is not None and value_type == str and re.match(ignore_regex, value):
                    continue  # Ignore string due to regex
                elif ignore_regex is not None and value_type == int and re.match(ignore_regex, str(value)):
                    continue  # Ignore int due to regex
                else:
                    elements.append(value)  # Assign extracted type from value

    return elements


def filter_values(dictionary: Dict, ignore_types: List[type] = [], ignore_regex: Optional[dict] = None) -> Dict[str, type]:
    """
    Extract types from (eventually nested) dictionary.

    :param dictionary: Input dictionary to extract types from.
    :param ignore_types: Optional list of types to be ignored when found.
    :param ignore_regex: Optional regex string to be ignored when matched.
    :return: A dictionary with types instead of proper values.
    """
    dict_types = {}
    for key, value in dictionary.items():
        value_type = type(value)
        if value_type == dict:  # Value is a dict, extract it
            dict_types[key] = filter_values(value, ignore_types=ignore_types, ignore_regex=ignore_regex)
        elif value_type == list:
            dict_types[key] = _expand_list_values(value, ignore_types=ignore_types, ignore_regex=ignore_regex)
        else:
            if value_type not in ignore_types:  # Value is not explicitely ignored
                if ignore_regex is not None and value_type == str and re.search(ignore_regex, value):
                    continue  # Ignore string due to regex
                if ignore_regex is not None and key in ignore_regex:
                    continue
                elif ignore_regex is not None and value_type == int and re.search(ignore_regex, str(value)):
                    continue  # Ignore string due to regex
                else:
                    dict_types[key] = value  # Assign extracted type from value
    return dict_types


def dict_diff(actual: Dict, expected: Dict, ignore_types: List[type] = [], ignore_regex: Optional[dict] = None) -> Dict[str, type]:
    """
    Compute differences in two dictionary composition types.

    :param actual: The dictionary to be compared.
    :param expected: The reference dictionary.
    :param ignore_types: Optional list of types to be ignored when found.
    :param ignore_regex: Optional regex string to be ignored when matched.
    :return: A dictionary containing only differing keys and motivation as value.
    """
    # Adapt value from input dict
    actual_types = filter_values(actual, ignore_types=ignore_types, ignore_regex=ignore_regex)
    # Adapt value from expected dict
    expected_types = filter_values(expected, ignore_types=ignore_types, ignore_regex=ignore_regex)

    def _get_diff(actual_types: Dict, expected_types: Dict) -> Dict[str, type]:
        """
        Get differences from two given 'typed' dictionaries.
        :param actual: The types of the dictionary to be compared.
        :param expected: The types of the reference dictionary.
        :return: Diffs of the two compared dictionary types.
        """
        diffs = {}

        for k, v in actual_types.items():
            if k not in expected_types:  # Key found in actual but not in expected
                diffs[k] = f"Unexpected key {k}."
            elif v != expected_types[k]:
                if isinstance(v, dict):
                    if isinstance(expected_types[k], dict):
                        d = _get_diff(v, expected_types[
                            k])  # Just 2 different dataframes, recursively check for differences
                        if d:
                            diffs[k] = d  # Found diffs in subdictionaries
                    else:
                        diffs[
                            k] = f"Found type dict but expected {expected_types[k]}"  # A type was expected but nested dict was found
                elif isinstance(expected_types[k], dict):
                    diffs[k] = f"Found type {v} but expected dict"  # A nested dict was expected but type was found
                elif isinstance(v, list):
                    if isinstance(expected_types[k], list):
                        list_diffs = []
                        if len(v) == len(expected_types[k]):
                            for ix in range(len(v)):
                                if v[ix] != expected_types[k][ix]:
                                    list_diffs.append(
                                        f"List element {v[ix]} different from expected {expected_types[k][ix]}")
                        else:
                            diffs[
                                k] = f"Found list length {len(v)} mismatch expected list length {len(expected_types[k])}"
                        if len(list_diffs) > 0:
                            diffs[k] = list_diffs  # Found diffs in subdictionaries
                    else:
                        diffs[
                            k] = f"Found type list but expected {expected_types[k]}"  # A type was expected but nested dict was found
                elif isinstance(expected_types[k], list):
                    diffs[k] = f"Found type {v} but expected list"  # A nested list was expected but type was found
                else:
                    diffs[k] = f"Found type {v} but expected {expected_types[k]}"  # Values have different type
            elif isinstance(v, dict):
                d = _get_diff(v, expected_types[k])  # Just 2 different dataframes, recursively check for differences
                if d:
                    diffs[k] = d  # Found diffs in subdictionaries

        for k in expected_types:
            if k not in actual_types:
                diffs[k] = f"Missing expected key {k}"  # An expected key wasn't found
        return diffs

    return _get_diff(actual_types, expected_types)


# Diff
def json_compare(actual, expected, ignore_regex1=[TIMESTAMP_REGEX, INTEGER]):
    ignore_regex = '(?:% s)' % '|'.join((str(regex) for regex in ignore_regex1))
    expected = json.load(open(expected, "r"))  # Sample dictionary to be validated
    differenceJson = dict_diff(actual, expected, ignore_regex=ignore_regex)
    result = bool(differenceJson)

    if result:
        print("Diffs found : ", result)
    assert result is False


def json_compare_dictionary(actual, expected, ignore_regex1=[TIMESTAMP_REGEX, INTEGER]):
    ignore_regex = '(?:% s)' % '|'.join((str(regex) for regex in ignore_regex1))
    differenceJson = dict_diff(actual, expected, ignore_regex=ignore_regex)
    result = bool(differenceJson)

    if result:
        print("Diffs found : ", result)
    assert result is False


def schema_extract_types(dictionary: Dict, ignore_types: List[type] = [], ignore_regex: Optional[str] = None) -> Dict[str, type]:
    """
    Extract types from (eventually nested) dictionary.

    :param dictionary: Input dictionary to etract types from.
    :param ignore_types: Optional list of types to be ignored when found.
    :param ignore_regex: Optional regex string to be ignored when matched.
    :return: A dictionary with types instead of proper values.
    """
    dict_types = {}
    for key, value in dictionary.items():
        value_type = type(value)
        if value_type == dict:  # Value is a dict, extract it
            dict_types[key] = schema_extract_types(value, ignore_types=ignore_types, ignore_regex=ignore_regex)
        else:
            if value_type not in ignore_types:  # Value is not explicitely ignored
                if ignore_regex is not None and value_type == str and re.search(ignore_regex, value):
                    continue  # Ignore string due to regex
                else:
                    dict_types[key] = type(value)  # Assign extracted type from value
    return dict_types


def schema_dict_diff(actual: Dict, expected: Dict, ignore_types: List[type] = [], ignore_regex: Optional[str] = None) -> Dict[str, type]:
    """
    Compute differences in two dictionary composition types.

    :param actual: The dictionary to be compared.
    :param expected: The reference dictionary.
    :param ignore_types: Optional list of types to be ignored when found.
    :param ignore_regex: Optional regex string to be ignored when matched.
    :return: A dictionary containing only differing keys and motivation as value.
    """
    # Extract types from actual dict
    actual_types = schema_extract_types(actual, ignore_types=ignore_types, ignore_regex=ignore_regex)
    # Extract types from expected dict
    expected_types = schema_extract_types(expected, ignore_types=ignore_types, ignore_regex=ignore_regex)

    def schema_get_diff(actual_types: Dict, expected_types: Dict) -> Dict[str, type]:
        """
        Get differences from two given 'typed' dictionaries.
        :param actual: The types of the dictionary to be compared.
        :param expected: The types of the reference dictionary.
        :return: Diffs of the two compared dictionary types.
        """
        diffs = {}

        for k, v in actual_types.items():
            if k not in expected_types:  # Key found in actual but not in expected
                diffs[k] = f"Unexpected key {k}."
            elif v != expected_types[k]:
                if isinstance(v, dict):
                    if isinstance(expected_types[k], dict):
                        d = schema_get_diff(v, expected_types[k])  # Just 2 different dataframes, recursively check for differences
                        if d:
                            diffs[k] = d  # Found diffs in sub-dictionaries
                    else:
                        diffs[k] = f"Found type dict but expected {expected_types[k]}"  # A type was expected but nested dict was found
                elif isinstance(expected_types[k], dict):
                    diffs[k] = f"Found type {v} but expected dict"  # A nested dict was expected but type was found
                else:
                    diffs[k] = f"Found type {v} but expected {expected_types[k]}"  # Values have different type
            elif isinstance(v, dict):
                d = schema_get_diff(v, expected_types[k])  # Just 2 different dataframes, recursively check for differences
                if d:
                    diffs[k] = d  # Found diffs in sub-dictionaries

        for k in expected_types:
            if k not in actual_types:
                diffs[k] = f"Missing expected key {k}"  # An expected key wasn't found
        return diffs

    return schema_get_diff(actual_types, expected_types)


# Diff
def json_compare_schema(actual, expected, ignore_regex=TIMESTAMP_REGEX):
    expected = json.load(open(expected, "r"))  # Sample dictionary to be validated
    differenceJson = schema_dict_diff(actual, expected, ignore_regex=TIMESTAMP_REGEX)
    result = bool(differenceJson)

    if result:
        print("Diffs found : ", result)

    assert schema_dict_diff(actual, expected, ignore_regex=TIMESTAMP_REGEX) == {}
    assert result is False
