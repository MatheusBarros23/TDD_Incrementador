import pytest
from src.incrementador import *


@pytest.mark.parametrize("num, res_esp", [([2,3], [3,4]), (3, 4)])
def test_incre(num, res_esp):
    i = Incrementador()
    res = i.inc(num)
    assert res == res_esp

@pytest.mark.parametrize("num", [([-2]), ([-3]),([2.0980]),(["t"])])
def test_incre_natural(num):
    i = Incrementador()
    with pytest.raises(IncError): #um assert para erros!!
        res = i.inc(num)