

def maximum(arr):
    max = 0
    ans = ''
    for s in arr:
        if s["salary"] > max:
            max = s["salary"]
            ans = s
    return ans

employees = [{"name" : "Deepak","salary" : 3000},{"name" : "Deepak","salary" : 4000},{"name" : "Deepak","salary" : 6000}]

print(maximum(employees))