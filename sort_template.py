def sort_by_template(nums, template):
    order = {num: i for i, num in enumerate(template)}
    return sorted(nums, key=lambda x: (order.get(x, float('inf')), x))



n = int(input())
nums = list(map(int, input().split()))
m = int(input())
template = list(map(int, input().split()))

result = sort_by_template(nums, template)
print(*result)