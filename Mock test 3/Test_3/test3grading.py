
total = 0
pts = 5
print('TEST 3')
print('-------------')


try:
    import F1
    assert str(F1.C(17)) == "*****************"
    assert str(F1.C(0)) == ""
    assert str(F1.C(-4)) == ""
    total += pts
    print('F1:', pts, 'pts')
except:
    print('F1:', 0, 'pts')

try:
    import F2
    assert F2.C("255.255.255.0").m() == True
    assert F2.C("255.255.256.0").m() == False
    total += pts
    print('F2:', pts, 'pts')
except:
    print('F2:', 0, 'pts')

try:
    import F3
    assert F3.C(["5555","66","5555","777"]).m() == True
    assert F3.C(["5555","66","555","777"]).m() == False
    total += pts
    print('F3:', pts, 'pts')
except:
    print('F3:', 0, 'pts')

try:
    import F4
    assert F4.C([22,33,44,55,66]).m() == 11
    assert F4.C([22,33,55,66]).m() == -1
    total += pts
    print('F4:', pts, 'pts')
except:
    print('F4:', 0, 'pts')

try:
    import F5
    assert F5.C([6,29,38,7,192,111,8]).m() == True
    assert F5.C([6,29,38,7,191,111,8]).m() == False
    total += pts
    print('F5:', pts, 'pts')
except:
    print('F5:', 0, 'pts')

try:
    import F6
    assert F6.C("blue ball").m() == {"b":2,"l":3,"u":1,"e":1, " ":1, "a":1}
    total += pts
    print('F6:', pts, 'pts')
except:
    print('F6:', 0, 'pts')

try:
    import F7
    assert F7.C().m(90,92,2) == 3
    total += pts
    print('F7:', pts, 'pts')
except:
    print('F7:', 0, 'pts')

try:
    import F8
    assert F8.C().m(36,37,3) == 2
    total += pts
    print('F8:', pts, 'pts')
except:
    print('F8:', 0, 'pts')


print('TOTAL:', total, 'pts')

