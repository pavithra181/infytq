def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    for rabbit_count in range(heads,1,-1):
        if 2*chicken_count+4*rabbit_count==legs:
            print(chicken_count,rabbit_count)
            break
        chicken_count=chicken_count+1
    if chicken_count+rabbit_count>heads:
        print(error_msg)

solve(38,131)
