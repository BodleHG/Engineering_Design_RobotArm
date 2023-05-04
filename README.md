# 미로봇 환경설정
## 1. 미로봇 드라이버 설치
- ```mirobot driver\CH340 driver (USB serial port driver) _XP_WIN7_WIN8\DRVSETUP64``` 폴더 안의 ```SETUP.EXE``` 파일 실행
  - ![image](https://user-images.githubusercontent.com/89232601/236123192-c6828d1d-dc30-4cd1-b592-8f275fd94d5c.png)

- Install 버튼 클릭 후 설치 완료 시 종료
  - ![image](https://user-images.githubusercontent.com/89232601/236123304-fd205aaa-5d88-4396-abed-ba4ed4a823a7.png)

- 윈도우 검색에서 ```장치 관리자``` 검색 후 실행
  - ![image](https://user-images.githubusercontent.com/89232601/236123811-b8ededc6-8bdd-411f-9054-c36f54ecd82c.png)

- 포트(COM & LPT) 항목에서 CH340에 해당하는 포트번호 확인(미로봇이 켜져있어야 함, 해당 이미지의 경우 COM5)
  - ![image](https://user-images.githubusercontent.com/89232601/236123998-5b1ee528-8af6-4d84-875f-59f1cf21e22b.png)

- 깃허브 파일을 다운받은 폴더로 이동 후, 주소창에 cmd 입력
  - ![image](https://user-images.githubusercontent.com/89232601/236124510-a87ee886-bd1a-4702-a214-f755f677c335.png)

- 터미널이 실행되면 다음 명령어 순차적으로 입력
  1. (가상환경 생성) ```python -m venv venv ```
     - ![image](https://user-images.githubusercontent.com/89232601/236124694-1cfa44f8-c072-47d7-9663-5e0830699b14.png)
  2. (가상환경 실행) ```venv\Scripts\activate```
     - ![image](https://user-images.githubusercontent.com/89232601/236124806-3c7ccf6c-c525-46ff-aed9-d74f67de258b.png)
  3. (코드 실행에 필요한 패키지 설치) ```pip install -r requirements.txt```
      - ![image](https://user-images.githubusercontent.com/89232601/236124982-2fa30b90-9c38-4bbf-8c1b-8dd1c94ad4c3.png)

  4. (미로봇 코드 폴더로 이동) ```cd mirobotApi```
      - ![image](https://user-images.githubusercontent.com/89232601/236125104-0dae8d40-d429-4150-9d2a-27d9801fb586.png)

  5. (미로봇 제어 코드 실행) ```python run.py keyboard```

- - -
# TODO
1. mirobotApi 폴더 내의 config.py 파일 수정(메모장, vscode 활용)
   - config.py 파일을 수정하지 않고 실행 시 오류 발생 

2. 프로그램을 통해 미로봇을 제어해보며, 어떤 파라미터 값이 제어 시 사용자 입장에서 접근성이 가장 높은지 조원과 토의하며 설정(코드 종료 방법 : 1 입력, 강제종료 : Ctrl + c)

3. 평가지 작성이 끝나면, 조교에게 제출

**제한 시간 : 1시간 30분**

**총 20점(참여도(10) / 창의성(4) / 실현 가능성(3) / 효율성(3), 조별점수), 참여도가 낮다고 판단시 조교가 임의로 질문 혹은 발표를 시킬 수 있음**

**역할 분배 자유, 구글링, chatgpt 사용 가능**