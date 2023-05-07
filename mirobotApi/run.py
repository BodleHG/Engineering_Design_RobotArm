import argparse
from wlkata_mirobot import WlkataMirobot, WlkataMirobotTool
from keymanager import Keymanager
from config import *
import asyncio
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mirobot Control")
    parser.add_argument("mode", choices=["keyboard", "remote"])    
    
    args = parser.parse_args()
    
    print("미로봇 상태를 초기화합니다...")
    
    try:
        arm = WlkataMirobot(portname=PORTNAME)
        print(f"포트 연결이 감지되었습니다. 현재 포트 : {PORTNAME}")
    
        # Mirobot Arm Multi-axis executing
        print("Mirobot Homing...")

        arm.home()

        print("Homing finish")
            
        print("이펙터가 감지되었습니다. 현재 이펙터 : FLEXIBLE CLAW")
        arm.set_tool_type(WlkataMirobotTool.FLEXIBLE_CLAW)
        arm.pump_suction()
        time.sleep(1)
        arm.pump_blowing()
        time.sleep(1)
        arm.pump_off()

        if args.mode == "keyboard":
            print("현재 키보드 제어 모드입니다. 키보드를 통해 제어해주세요.")
            # Keymanager(arm)._setJointAngle()
            asyncio.run(Keymanager(arm)._setAxis())
            
        # elif args.mode == "remote":
        #     print("Remote Control Mode")   
        #     Remotemanager(arm).remoteRecv() 
    except:
        print("포트 연결이 감지되지 않았습니다. 프로그램을 종료합니다.")
    