from src.math_operations import add, multi
def test_add():
  assert add(2,3)==5
  assert add(-1,1)==0

def test_multi():
  assert multi(1,4)==4
  assert multi(9,3)==27
  assert multi(3426,7625)==26123250
  
