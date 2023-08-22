total_minutes = int(input())
hours = total_minutes // 60
minutes = total_minutes - hours*60
print(hours%24, minutes)
