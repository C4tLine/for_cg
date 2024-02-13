"""Testing module for hw2."""

import json

import pytest

from hw2 import hw2

TEST_VALUES = 'input_path, output_path, expected_path'

TEST_PROCESS_DATA = (
    (
        'hw2/input/data_hw2.json',
        'hw2/output/output_data_hw2.json',
        'hw2/expected/expected_data_hw2.json',
    ),
    (
        'hw2/input/clients.json',
        'hw2/output/output_clients.json',
        'hw2/expected/expected_clients.json',
    ),
    (
        'hw2/input/clients2.json',
        'hw2/output/output_clients2.json',
        'hw2/expected/expected_clients2.json',
    ),
    (
        'hw2/input/unfinished.json',
        'hw2/output/output_unfinished.json',
        'hw2/expected/expected_unfinished.json',
    )
)

TEST_EXIST_FILE = (
    'hw2/input/gdz.json',
    'hw2/output/result.json',
)

TEST_EMPTY_FILE = (
    'hw2/input/empty.json',
    'hw2/output/result.json',
)

TEST_INPUT_EXTENSION = (
    'hw2/input/input.txt',
    'hw2/output/output_clients.json',
)

TEST_OUTPUT_EXTENSION = (
    'hw2/input/clients.json',
    'hw2/output/output.txt',
)

TEST_WRONG_JSON = (
    'hw2/input/wrong.json',
    'hw2/output/result.json',
)

@pytest.mark.parametrize(TEST_VALUES, TEST_PROCESS_DATA)
def test_process_data(input_path: str, output_path: str, expected_path: str) -> None:
    hw2.process_data(input_path, output_path)

    with open(expected_path, 'r') as expected_file:
        expected = json.load(expected_file)

    with open(output_path, 'r') as output_file:
        output = json.load(output_file)

    assert output == expected


@pytest.mark.parametrize(TEST_VALUES, TEST_EXIST_FILE)
def test_exist_file(input_path: str, output_path: str) -> None:
    
    with pytest.raises(ValueError):
        hw2.process_data(input_path, output_path)


@pytest.mark.parametrize(TEST_VALUES, TEST_EMPTY_FILE)
def test_empty_file(input_path: str, output_path: str) -> None:
    
    with pytest.raises(ValueError):
        hw2.process_data(input_path, output_path)


@pytest.mark.parametrize(TEST_VALUES, TEST_INPUT_EXTENSION)
def test_input_extension(input_path: str, output_path: str) -> None:

    with pytest.raises(TypeError):
        hw2.process_data(input_path, output_path)


@pytest.mark.parametrize(TEST_VALUES, TEST_OUTPUT_EXTENSION)
def test_output_extension(input_path: str, output_path: str) -> None:

    with pytest.raises(TypeError):
        hw2.process_data(input_path, output_path)
    

@pytest.mark.parametrize(TEST_VALUES, TEST_WRONG_JSON)
def test_wrong_json(input_path: str, output_path: str) -> None:

    with pytest.raises(ValueError):
        hw2.process_data(input_path, output_path)
