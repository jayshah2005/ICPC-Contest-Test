import sys
from math import ceil

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    totals = {'S': 0, 'M': 0, 'L': 0}
    capacities = {'S': 6, 'M': 8, 'L': 12}
    
    idx = 1
    for _ in range(n):
        size = input_data[idx]
        slices = int(input_data[idx+1])
        totals[size] += slices
        idx += 2
        
    total_boxes = 0
    for size, total_slices in totals.items():
        cap = capacities[size]
        if total_slices > 0:
            total_boxes += ceil(total_slices / cap)
            
    print(total_boxes)

if __name__ == '__main__':
    solve()