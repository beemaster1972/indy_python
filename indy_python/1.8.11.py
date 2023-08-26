total_secs = int(input())
h = total_secs // 3600
m = total_secs%3600//60
s = total_secs%60
print(f'{h}:{m:02}:{s:02}')