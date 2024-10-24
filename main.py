import os
import threading
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from fastapi import FastAPI

# 환경 변수 로드
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

# Slack Bolt 앱 초기화
slack_app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)

# FastAPI 앱 초기화
api_app = FastAPI()

# Slack 명령 핸들러
@slack_app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

# 메시지 이벤트 핸들러
@slack_app.event("message")
def handle_message_events(body, say):
    say("Hello from the Slack bot!")

# FastAPI 엔드포인트 예시 (테스트용)
@api_app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running on port 8013"}

# Socket Mode를 별도 스레드에서 실행
def run_socket_mode():
    handler = SocketModeHandler(slack_app, SLACK_APP_TOKEN)
    handler.start()

# FastAPI 서버 실행
if __name__ == "__main__":
    # Socket Mode 실행을 별도 스레드에서 시작
    thread = threading.Thread(target=run_socket_mode)
    thread.start()

    # FastAPI 서버 실행 (포트 8013)
    import uvicorn
    uvicorn.run(api_app, host="0.0.0.0", port=8013)