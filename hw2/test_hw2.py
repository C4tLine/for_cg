"""Testing module for hw2."""

import json

import pytest

import hw2

TEST_PROCESS_DATA = (
    (
        'input/data_hw2.json',
        'output/output_data_hw2.json',
        'expected/expected_data_hw2.json',
    ),
    (
        'input/clients.json',
        'output/output_clients.json',
        'expected/expected_clients.json',
    ),
    (
        'input/clients2.json',
        'output/output_clients2.json',
        'expected/expected_clients2.json',
    ),
    (
        'input/unfinished.json',
        'output/output_unfinished.json',
        'expected/expected_unfinished.json',
    )
)

TEST_EXIST_FILE = (
    (
        'input/gdz.json',
        'output/output.json',
    ),
    (
        'input/reshalka.json',
        'output/output.json',
    )
)

TEST_EMPTY_FILE = (
    (
        'input/empty.json',
        'output/output.json',
    ),
    (
        'input/nothing.json',
        'output/output.json',
    )
)

TEST_EXTENSION = (
    (
        'input/input.txt',
        'output/output.json',
    ),
    (
        'input/clients.json',
        'output/output.txt',
    )
)

TEST_WRONG_JSON = (
    (
        'input/wrong.json',
        'output/output.json',
    ),
    (
        'input/broken.json',
        'output/output.json',
    )
)

@pytest.mark.parametrize('input_path, output_path, expected_path', TEST_PROCESS_DATA)
def test_process_data(input_path: str, output_path: str, expected_path: str) -> None:
    hw2.process_data(input_path, output_path)

    with open(expected_path, 'r') as expected_file:
        expected = json.load(expected_file)

    with open(output_path, 'r') as output_file:
        output = json.load(output_file)

    assert output == expected


@pytest.mark.parametrize('input_path, output_path', TEST_EXIST_FILE)
def test_exist_file(input_path: str, output_path: str) -> None:
    
    with pytest.raises(ValueError):
        hw2.process_data(input_path, output_path)


@pytest.mark.parametrize('input_path, output_path', TEST_EMPTY_FILE)
def test_empty_file(input_path: str, output_path: str) -> None:
    
    with pytest.raises(ValueError):
        hw2.process_data(input_path, output_path)


@pytest.mark.parametrize('input_path, output_path', TEST_EXTENSION)
def test_extension(input_path: str, output_path: str) -> None:

    with pytest.raises(TypeError):
        hw2.process_data(input_path, output_path)
    

@pytest.mark.parametrize('input_path, output_path', TEST_WRONG_JSON)
def test_wrong_json(input_path: str, output_path: str) -> None:

    with pytest.raises(ValueError):
        hw2.process_data(input_path, output_path)
