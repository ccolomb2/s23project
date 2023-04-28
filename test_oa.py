"""
This file has some tests so we can see our package works.asdasdas
"""

from s23project import Works

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
    "test ris"
    work_obj = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert REF_RIS == work_obj.ris()


REF_BIBTEX = """author = {John R. Kitchin},
journal = {ACS Catalysis},
title = {Examples of Effective Data Sharing in Scientific Publishing},
volume = {5},
issue  = {6},
pages = {3894-3899},
year = {2015}"""


def test_bibtex():
    "test bibtex"
    work_obj = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert work_obj.bibtex() == REF_BIBTEX

test_bibtex()
    