from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os
from venv import logger

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

# ID of the channel you want to send the message to
channel_id = "D07T3RW6J67"

try:
    # Call the chat.postMessage method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id, 
        text="Hello world"
    )
    logger.info(result)

except SlackApiError as e:
    logger.error(f"Error posting message: {e}")
