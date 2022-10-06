# 9498
"""
점수를 입력받아 90~100점은 A, 80~89점은 B, 70~79점은 C, 60~69점은 D, 나머지는 F
"""
while True:
    score = int(input())
    if score > 100 or score < 0 :
        continue
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
    break

