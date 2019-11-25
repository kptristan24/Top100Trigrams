#!/bin/python3

import pytest
import fileinput
import sys
import io
import collections

# Testing Module
import ngrams

@pytest.fixture
def multiple_file_list():
    files = ["tests/multifile1.txt", "tests/multifile2.txt", "tests/multifile3.txt"]
    return fileinput.input(files)

@pytest.fixture
def small_file():
    return fileinput.input("tests/exodus.txt")

@pytest.fixture
def large_file():
    return fileinput.input("tests/kjb.txt")

@pytest.fixture
def formatting_and_characters_test_file():
    return  fileinput.input("tests/format_and_characters.txt")

@pytest.fixture
def contractions_test_file():
    return  fileinput.input("tests/contractions.txt")

def test_multiple_file_inputs_accepted(multiple_file_list, small_file):

    #Verifies one and many files are accepted
    assert ngrams.get_ngrams(multiple_file_list)
    assert ngrams.get_ngrams(small_file)

def test_stdin_accepted(monkeypatch):

    # Use monkeypatch to mock stdin
    monkeypatch.setattr('sys.stdin', io.StringIO('one one one\ntwo two two'))
    assert ngrams.get_ngrams(sys.stdin)

def test_100_length_list(large_file, capsys):
    ngrams.rank_occurrences(ngrams.get_ngrams(large_file))
    captured = capsys.readouterr()

    # -2 lines for header and trailer
    assert len(captured.out.splitlines()) - 2 == 100

def test_ignore_line_endings(formatting_and_characters_test_file):
    output = ngrams.get_ngrams(formatting_and_characters_test_file)
    assert output[3][('i', 'love', 'sandwiches')] == 2

def test_ignore_punctuation(formatting_and_characters_test_file):
    output = ngrams.get_ngrams(formatting_and_characters_test_file)
    assert output[3][('punc', 'punc', 'punc')] == 4

def test_contractions_count(contractions_test_file):
    output = ngrams.get_ngrams(contractions_test_file)
    assert output[3][('it', 'wont', 'do')] == 2

def test_ignore_capitalization(formatting_and_characters_test_file):
    output = ngrams.get_ngrams(formatting_and_characters_test_file)
    assert output[3][('one', 'two', 'three')] == 3

def test_handles_unicode(formatting_and_characters_test_file):
    output = ngrams.get_ngrams(formatting_and_characters_test_file)
    assert output[3][('süssig', 'süssig', 'süssig')] < 2
