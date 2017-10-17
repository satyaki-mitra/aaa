from nose.tools import *
from NAME.parser import *


def test_parse_verb():
    x = parse_sentence([('stop','the'),('noun','bear'),('verb','ran'),('direction','north')])
    assert_equal(x.verb,'ran')
    

def test_parse_object():
    x = parse_sentence([('stop','the'),('noun','bear'),('verb','ran'),('direction','north')])
    assert_equal(x.object,'north')

def test_parse_subject():
    x = parse_sentence([('stop','the'),('noun','bear'),('verb','ran'),('direction','north')])
    assert_equal(x.subject,'bear')

