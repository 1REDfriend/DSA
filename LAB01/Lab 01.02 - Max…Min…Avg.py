"""Lab 01.02 - Max…Min…Avg"""
import json
from decimal import Decimal

def main() :
    """main"""
    num = json.loads(input())
    man_num = float("inf")
    mox_num = 0
    averge = 0

    for i in num :
        if float(i) <= man_num :
            man_num = i
        if float(i) >= mox_num :
            mox_num = i
        averge += i
    averge /= len(num)

    averge = str(Decimal(str(round(averge, 2))))
    mox_num = str(Decimal(str(round(mox_num, 2))))
    man_num = str(Decimal(str(round(man_num, 2))))

    if mox_num[-1] == "0" and mox_num[-2] == "." :
        mox_num = mox_num[:-2]
    if man_num[-1] == "0" and man_num[-2] == "." :
        man_num = man_num[:-2]
    if averge[-1] == "0" and averge[-2] == "." :
        averge = averge[:-2]

    print(f"({mox_num}, {man_num}, {averge})")
main()