#!/usr/bin/python

# Slack webhooks for notifications
posting_webhook = "https://hooks.slack.com/services/<secret>"
errorlogging_webhook = "https://hooks.slack.com/services/<secret>"
slack_sleep_enabled = True  # bypass Slack rate limit when using free workplace, switch to False if you're using Pro/Ent version.
at_channel_enabled = True   # Add @channel notifications to Slack messages, switch to False if you don't want to use @channel

# Telegram Bot
telegram_api = "5286814204:AAE_BAB4QZS_I4hb0HDoTdQASfCTSq59Vfc"
telegram_chat_id = "-812845634"

# crtsh postgres credentials, please leave it unchanged.
DB_HOST = 'crt.sh'
DB_NAME = 'certwatch'
DB_USER = 'guest'
DB_PASSWORD = ''
