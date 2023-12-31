from project import check_correck_arg,sel_age,sel_program

import pytest

def test_check_correck_arg():
     with pytest.raises(SystemExit):
         check_correck_arg()


def test_sel_program():
    assert sel_program("over_wight_|")=="Program_2"
    assert sel_program("over_wight_||")=="Program_2"
    assert sel_program("over_wight_|||")=="Program_2"
    assert sel_program("fit")=="Program_1"
    assert sel_program("Excessive obesity_|")=="Program_3"
    assert sel_program("Excessive obesity_||")=="Program_3"
    assert sel_program("Excessive obesity_|||")=="Program_4"

def test_sel_age():

    assert sel_age(1995)=="28 year"
    assert sel_age(1996)=="27 year"
    assert sel_age(1997)=="26 year"
    assert sel_age(1998)=="25 year"
    assert sel_age(1999)=="24 year"
    assert sel_age(2000)=="23 year"
    assert sel_age(2001)=="22 year"
    assert sel_age(2002)=="21 year"
    assert sel_age(2003)=="20 year"
    assert sel_age(2004)=="19 year"
