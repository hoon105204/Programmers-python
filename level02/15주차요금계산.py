# https://school.programmers.co.kr/learn/courses/30/lessons/92341
from datetime import datetime
import math


def solution(fees, records):
    answer = []
    timedict = {}
    pricedict = {}
    for i in range(len(records)):
        tmplist = records[i].split(' ')
        valtime, valnumb, valtype = tmplist[0], tmplist[1], tmplist[2]

        valtime = datetime.strptime(valtime, '%H:%M')
        if valtype == 'IN':
            timedict[valnumb] = valtime
            if valnumb not in pricedict.keys():
                pricedict[valnumb] = 0
        else:
            diff = valtime - timedict.pop(valnumb)
            pricedict[valnumb] += diff.total_seconds()/60

    for keyValue in timedict.keys():
        diff = datetime.strptime('23:59', '%H:%M') - timedict[keyValue]
        times = diff.total_seconds()/60
        pricedict[keyValue] += times

    for keyValue in sorted(pricedict.keys()):
        answer.append(countfee(fees,pricedict[keyValue]))

    return answer


def countfee(fees, times):
    basictime = fees[0]
    basicfee = fees[1]
    unittime = fees[2]
    unitfee = fees[3]

    answer = basicfee
    if times <= basictime:
        return answer
    else:
        answer += math.ceil((times - basictime) / unittime) * unitfee
    return answer


feesval, recordsval = [180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                                       "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN",
                                       "23:00 5961 OUT"]

print(solution(feesval, recordsval))
