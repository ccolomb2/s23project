"""Tests to check the outputs"""

from pkg import Works

REF_RIS = """TY  - JOUR
AU  - John R. Kitchin
PY  - 2015
TI  - Examples of Effective Data Sharing in Scientific Publishing
JO  - ACS Catalysis
VL  - 5
IS  - 6
SP  - 3894
EP  - 3899
DO  - https://doi.org/10.1021/acscatal.5b00538
ER  -"""

def test_ris():
    "test to see if the ris function works"
    works_object = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert works_object.ris() == REF_RIS


REF_BIBTEX = """@article{J2015,
author = {John R. Kitchin},
journal ={ACS Catalysis},
title = {Examples of Effective Data Sharing in Scientific Publishing},
volume = {5},
issue ={6},
pages = {3894-3899},
year = {2015}
}"""


def test_bibtex():
    "test to see if the bibtex function works"
    works_object = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert works_object.bibtex() == REF_BIBTEX
