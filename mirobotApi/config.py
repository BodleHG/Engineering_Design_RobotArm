# 미로봇 시리얼 통신 설정
# 예시
# PORTNAME :str = "COM0"
PORTNAME :str = "?"

# 로봇암 제어 키 설정
# String 문자열 형태로 입력

# 예시 리스트의 키 이외의 키도 적용 가능
KEY_EXAMPLE = ["a", "b", "c", "d", "down", "up", "left", "right", "space", "ctrl", "alt"]

# 예시
# KUP_1, KDOWN_1 = "a", "d"

### 키 설정
KUP_1, KDOWN_1 = "?", "?"

KUP_2, KDOWN_2 = "?", "?"

KUP_3, KDOWN_3 = "?", "?"

KUP_4, KDOWN_4 = "?", "?"

KUP_5, KDOWN_5 = "?", "?"

KUP_6, KDOWN_6 = "?", "?"

ENDEF_1, ENDEF_2 , ENDEF_3= "?", "?", "?"
### 

### 로봇암 속도 설정
# 예시
# JOINT_ANGLE = 20
# SPEED = 2000
JOINT_ANGLE = 0
SPEED = 0
# 최대 각도 설정

# 아래 코드는 건드릴 필요 X
########################################################

MIN_1, MAX_1 = -85 , 145

MIN_2, MAX_2 = -25 , 55

MIN_3, MAX_3 = -155 , 45

MIN_4, MAX_4 =  -330 , 330

MIN_5, MAX_5 =  -190 , 25

MIN_6, MAX_6 = -345 , 345