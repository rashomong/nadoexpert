kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor,eng)))    # 세로로 합친다.

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))    # * 을 붙여주면 첫번째 것들을 모음

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)