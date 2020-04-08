def get_repeating_DNA(l):
    list_result = []
    i = 1
    m = 10
    while len(l)>=10:
        result_my = l[:10]
        l = l[i:]
        if i == 10:
            i = 1
        if result_my in l:
            i += 1
            list_result.append(result_my)
    return list_result

test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)