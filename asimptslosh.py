#N**2
def strcounter(s):
    for sym in s:
     counter = 0
     for sub_sum in s:
            if sym == sub_sum:
                counter += 1
     print(sym,counter)
#strcounter('aaaaaaaaaannnnnnnnnssssssss')

#N*M
def str_counter(s):
    for sym in set(s):
     counter = 0
     for sub_sum in s:
            if sym == sub_sum:
                counter += 1
     print(sym,counter)
#str_counter('aaaaaaaaaannnnnnnnnssssssss')
#N
def strcounter1(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0)+1
    for sym,count in syms_counter.items():
        print(sym,count)
strcounter1('aaaaaaaaaannnnnnnnnssssssss')