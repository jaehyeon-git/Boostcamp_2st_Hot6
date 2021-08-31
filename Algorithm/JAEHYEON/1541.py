s = input().split('-') # -를 기준으로 자르기

sum = 0 # 합 담을 변수

# 첫번째 list 원소의 경우 처음 - 값이 나오기 전 값이므로
# 다 더해준다.
for i in s[0].split('+'):
    sum += int(i)

# 이후부터는 - 값이 적용됨으로 값을 전부 빼주면 된다.
for i in s[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)
