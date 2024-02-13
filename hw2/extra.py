"""Module for hw2."""
import os
from datetime import date
from typing import Any

TWO_DAYS = 2
WEEK = 7
MONTH = 30
HALFYEAR = 180


def check_paths(input_path: str, output_path: str) -> None:

    if not os.path.exists(input_path):
        raise ValueError('Input file does not exist.')
    if os.stat(input_path).st_size == 0:
        raise ValueError('Input file is empty.')
    
    _, input_extension = os.path.splitext(input_path)
    _, out_extension = os.path.splitext(output_path)

    if input_extension != '.json':
        raise TypeError('Input file does not have JSON extension.')
    if out_extension != '.json':
        raise TypeError('Output file does not have JSON extension.')


def process_last_login(clients: dict[str, dict[str, Any]]) -> dict:

    last_login_stats = {
        'less_than_two_days': 0,
        'less_than_one_week': 0,
        'less_than_one month': 0,
        'less_than_half_year': 0,
        'more_than_half_year': 0,
    }

    count_logins = 0
    for client in clients.values():
        if 'last_login' not in client:
            continue
        client_last_login = client['last_login']
        last_login = get_last_login(client_last_login)
        last_login_stats[last_login] += 1
        count_logins += 1
    try:
        return {
            last_login: count_login / count_logins * 100
            for last_login, count_login in last_login_stats.items()
    }
    except ZeroDivisionError:
        return last_login_stats


def get_last_login(date_str: str) -> str:

    last_login_date = date.fromisoformat(date_str)
    delta = date.today() - last_login_date
    match delta:
            case delta if delta.days <= TWO_DAYS:
                return 'less_than_two_days'
            case delta if delta.days <= WEEK:
                return 'less_than_one_week'
            case delta if delta.days <= MONTH:
                return 'less_than_one month'
            case delta if delta.days <= HALFYEAR:
                return 'less_than_half_year'
            case _:
                return 'more_than_half_year'


def process_regions(clients: dict[str, dict[str, Any]]) -> dict:

    regions = {}
    
    count_regions = 0
    for client in clients.values():
        if 'region' not in client:
            continue
        region = client['region']
        regions[region] = regions[region] + 1 if region in regions else 1
        count_regions += 1

    return {
        region_name: count_region / count_regions * 100
        for region_name, count_region in regions.items()
}
