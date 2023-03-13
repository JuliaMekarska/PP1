def bonus(years):
    if years <= 5:
        b = 100 * years
    elif years > 5 and years <= 8:
        b = 100 * 5 + 200  * (years - 5)
    else:
        b = 100 * 5 + 200 * 3 + 50 * (years - 8)

    return b
        