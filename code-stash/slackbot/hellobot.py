import os
import requests

from logzero import logger


user_email = "example@abc.com"

pay_load = {"token": os.environ["SLACK_BOT_TOKEN"], "email": user_email}

user_identity = requests.post(
    "https://slack.com/api/users.lookupByEmail", data=pay_load
)

if user_identity.ok:
    logger.debug(f"user id: {user_identity.json()['user']['id']}")
    msg_load = {
        "token": os.environ["SLACK_BOT_TOKEN"],
        "channel": user_identity.json()["user"]["id"],
        "text": "Hi! knock, knock!",
    }
    send_msg = requests.post("https://slack.com/api/chat.postMessage", data=msg_load)
    if send_msg.ok:
        logger.info(f"Message sent to {user_email} successfully.")
    else:
        logger.error(send_msg.text)
else:
    logger.error(user_identity.text)
