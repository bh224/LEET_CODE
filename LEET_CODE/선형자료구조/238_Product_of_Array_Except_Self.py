# 238. 자신을 제외한 배열의 곱

"""
output[i]가 자신을 제외한 나머지 요소의 곱셈 결과가 되도록 출력
input = [1,2,3,4]
output = [24,12,8,6]

multi = x

자신을 제외한 자신의 왼쪽 요소와 오른쪽 요소를 곱해주면 된다
'1' 의 경우 왼쪽은 없으니까 오른쪽 2,3,4를 곱해준 값을 output의 1의 자리에 넣어주고
'2' 의 경우 왼쪽 1 과 오른쪽 3,4를 곱한 12를 output의 2의 자리에 넣어준다

1. multi 는 1부터 시작
2. 해당요소 왼쪽 요소들끼리 곱한 값(multi)를 output에 넣는다
3. 해당요소 오른쪽 요소들끼리 곱한 값(multi)를 2번의 output 요소와 곱한 뒤 새로운 output 값으로 대체한다

"""

input = [1,2,3,4]
multi = 1
output = []

# 왼쪽 요소들의 곱
for i in range(len(input)):
    output.append(multi)
    multi = multi * input[i] # 왼쪽 요소들의 곱 누적이 된다

print(output)
# 현재 output 에는 해당 요소자리에 왼쪽 요소들의 곱이 들어가있게 된다 

# 오른쪽 요소들의 곱
multi = 1 
for i in range(len(input)-1, -1, -1): # input 요소를 끝에서부터 가져온다 ex) 3,2,1,...
    output[i] = output[i] * multi # ouput 값은 위의 output(왼쪽요소 곱)과 muliti의 곱으로 대체
    multi = input[i] * multi 

print(output)