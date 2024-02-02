def final_sorting(d, k, result):
    if len(result) == k or d == {}: return result
    
    for key, value in d.items():
        if value == max(d.values()):
            result.append(key)
            d.pop(key)

            break
    
    return final_sorting(d, k, result)