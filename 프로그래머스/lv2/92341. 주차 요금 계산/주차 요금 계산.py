from collections import defaultdict


def solution(fees, records):
    def get_time_gap(intime_str, outtime_str):
        i_hh, i_mm = map(int, intime_str.split(':'))
        o_hh, o_mm = map(int, outtime_str.split(':'))
        return (o_hh - i_hh) * 60 + (o_mm - i_mm)

    
    acc_time = defaultdict(int)
    parked = dict()

    for record in records:
        t, cnum, is_in = record.split()
        if is_in[0] == 'I':
            parked[int(cnum)] = t
        else:
            in_t = parked.pop(int(cnum))
            acc_time[int(cnum)] += get_time_gap(in_t, t)

    for cnum, t in parked.items():
        acc_time[int(cnum)] += get_time_gap(t, '23:59')

    answer = []
    for cnum in sorted(acc_time.keys()):
        if acc_time[cnum] <= fees[0]:
            answer.append(fees[1])
        else:
            div, mod = divmod(acc_time[cnum] - fees[0], fees[2])
            answer.append((div + (1 if mod else 0)) * fees[3] + fees[1])

    return answer
