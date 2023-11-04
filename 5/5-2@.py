def get_BMI(cm,kg):
    return kg / ((cm/100)*(cm/100))

cm,kg = map(int,input().split())
# GPT한테 과정 설명 듣자
# 변수 출력 방법도 다 분류해서 정리하고
print("{:.2f}".format(get_BMI(cm,kg)))