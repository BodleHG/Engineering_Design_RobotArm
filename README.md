# 개발환경 설정

- github 주소 : https://github.com/BodleHG/Engineering_Design_RobotArm

- code - Download ZIP 혹은 git clone으로 실습파일 다운로드
  - code - Download ZIP
    - ![image](https://user-images.githubusercontent.com/89232601/236130658-419839f3-a6d7-4181-bfc0-5ce3517304b2.png)
  - cmd 실행 후 ```git clone https://github.com/BodleHG/Engineering_Design_RobotArm.git``` 명령어 입력
    - ![image](https://user-images.githubusercontent.com/89232601/236131027-9c7eda36-227a-46f3-8dc9-52afb1168ec8.png)
    - 현재 위치에 파일을 저장하기 때문에 > 앞쪽의 경로를 잘 알아둬야 함

## 1. 미로봇 드라이버 설치
- ```mirobot driver\CH340 driver (USB serial port driver) _XP_WIN7_WIN8\DRVSETUP64``` 폴더 안의 ```SETUP.EXE``` 파일 실행
  - ![image](https://user-images.githubusercontent.com/89232601/236123192-c6828d1d-dc30-4cd1-b592-8f275fd94d5c.png)

- Install 버튼 클릭 후 설치 완료 시 종료
  - ![image](https://user-images.githubusercontent.com/89232601/236123304-fd205aaa-5d88-4396-abed-ba4ed4a823a7.png)

- 윈도우 검색에서 ```장치 관리자``` 검색 후 실행
  - ![image](https://user-images.githubusercontent.com/89232601/236123811-b8ededc6-8bdd-411f-9054-c36f54ecd82c.png)

- 포트(COM & LPT) 항목에서 CH340에 해당하는 포트번호 확인(미로봇이 켜져있어야 함, 해당 이미지의 경우 COM5)
  - ![image](https://user-images.githubusercontent.com/89232601/236123998-5b1ee528-8af6-4d84-875f-59f1cf21e22b.png)


## 2. 아나콘다(anaconda 설치)

- 구글에 Anaconda Download 검색 후 , 설치 파일 다운로드 및 설치
  - ![그림1](https://user-images.githubusercontent.com/89232601/236665402-925a3903-4187-46e2-ba41-39d5258fb46d.jpg)

- 윈도우 검색 창에 ```Anaconda Powershell Prompt``` 검색 후 실행
  - ![image](https://user-images.githubusercontent.com/89232601/236665573-dcdf3c4f-3a21-41c5-b177-03a7827ac481.png)

- 아나콘다 터미널 창에 ```conda create -n myenv python=3.8``` 입력
  - 아래 화면이 나오면 y 입력 후 엔터
  - ![image](https://user-images.githubusercontent.com/89232601/236665756-198c0234-c09e-4c2b-878c-995af2f474c4.png)

- 아나콘다 터미널 창에 ```conda activate myenv``` 입력
  - ![image](https://user-images.githubusercontent.com/89232601/236665971-235053ad-8bb2-4d07-bef5-30591bff3804.png)

- 깃허브 파일을 다운받은 폴더로 이동 후, 주소창의 경로 복사
  - ![image](https://user-images.githubusercontent.com/89232601/236666286-37fb6591-5048-4dfd-b3bf-e40eb6ff0757.png)


- 아나콘다 터미널 창에 ```cd ```입력 후 위에서 복사한 경로 붙여넣기 후 입력
  - ![image](https://user-images.githubusercontent.com/89232601/236666304-19657813-167b-4936-a182-5460ccd28c63.png)

- 아나콘다 터미널 창에 ```pip install -r requirements.txt``` 입력(코드 실행에 필요한 패키지 설치)
  - ![image](https://user-images.githubusercontent.com/89232601/236666373-a12f51fb-98ec-469c-9c76-7f5468d86fa3.png)

- 아나콘다 터미널 창에 ```cd mirobotApi``` 입력(미로봇 코드 폴더로 이동)
  - ![image](https://user-images.githubusercontent.com/89232601/236666442-adcd91a0-648b-499f-b273-bf02e0efd00e.png)

- 아나콘다 터미널 창에 ```python run.py keyboard``` 입력(로봇암 제어 코드 실행)
  - ![image](https://user-images.githubusercontent.com/89232601/236666673-9cb7e2a6-c078-4a82-a404-9f11cd6c95f6.png)
- - -
# TODO
1. mirobotApi 폴더 내의 config.py 파일 수정(메모장, vscode 활용)
   - config.py 파일을 수정하지 않고 실행 시 오류 발생 

2. 프로그램을 통해 미로봇을 제어해보며, 어떤 파라미터 값이 제어 시 사용자 입장에서 접근성이 가장 높은지 조원과 토의하며 설정(코드 종료 방법 : 1 입력, 강제종료 : Ctrl + c)

3. 평가지에 있는 주제에 대해 토의하여 작성

4. 평가지 작성이 끝나면, 조교에게 제출

**- 제한 시간 : 1시간 30분**

**- 총 20점(참여도(10) / 창의성(4) / 실현 가능성(3) / 효율성(3), 조별점수), 참여도가 낮다고 판단시 조교가 임의로 질문 혹은 발표를 시킬 수 있음**

**- 역할 분배 자유, 구글링, chatgpt 사용 가능**