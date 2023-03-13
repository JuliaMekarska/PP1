
total = 0
print('TEST 1')
print('-------------')


try:
    pts = 3
    from F1 import f1
    assert f1(11,6,-4) == True
    assert f1(5,4,14) == False
    assert f1(-5,-4,-14) == True
    total += pts
    print('F1 ok:', pts, 'pts')
except:
    pass


try:
    pts = 4
    from F2 import f2
    assert f2(4) == "*/*/*/*"
    assert f2(1) == "*"
    assert f2(9) == "*/*/*/*/*/*/*/*/*"
    total += pts
    print('F2 ok:', pts, 'pts')
except:
    pass


try:
    pts = 4
    from F3 import f3
    assert f3(-7,8) == 3
    assert f3(-1,11) == 0
    assert f3(-6,-2) == 3
    total += pts
    print('F3 ok:', pts, 'pts')
except:
    pass


try:
    pts = 4
    from F4 import f4
    x1,x2,x3=0,0,0
    for i in range(1000):
        x = f4()
        assert x in [3,7,11]
        x1 += 1 if x==3 else 0
        x2 += 1 if x==7 else 0
        x3 += 1 if x==11 else 0
    assert x1>0 and x2>0 and x3>0
    total += pts
    print('F4 ok:', pts, 'pts')
except:
    pass


try:
    pts = 4
    from F5 import f5
    assert f5(314569) == 2
    assert f5(2274) == 3
    assert f5(2828287282828) == 12
    total += pts
    print('F5 ok:', pts, 'pts')
except:
    pass


try:
    pts = 5
    from F6 import f6
    assert f6(2,8) == 15
    assert f6(3,4) == 19
    assert f6(5,5) == 41
    total += pts
    print('F6 ok:', pts, 'pts')
except:
    pass


try:
    pts = 6
    from F7 import f7
    assert f7(5) == 3
    assert f7(9) == 21
    assert f7(12) == 89
    total += pts
    print('F7 ok:', pts, 'pts')
except:
    pass


print('TOTAL:', total, 'pts')

