import pytest
phrase = input("Set a phrase: ")

def test_1():
    assert len(phrase) < 15, f"фраза короче чем 15 симфолов"