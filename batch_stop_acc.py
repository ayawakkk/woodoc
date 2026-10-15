import requests
import argparse
import re

API_URL = "http://127.0.0.1:8000/telegram/batch_stop_bot"

def call_batch_stop_bot(bot_names):
    payload = {
        "bot_names": bot_names
    }
    print("发送请求:", payload)
    try:
        r = requests.post(API_URL, data=payload, timeout=300)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"success": False, "error": str(e)}

def parse_bot_names(input_str):
    if not input_str:
        return ""
    parts = re.split(r'[,\s;|]+', input_str)
    filtered_parts = [part.strip() for part in parts if part.strip()]
    return ",".join(filtered_parts)

def main():
    parser = argparse.ArgumentParser(description="批量停止 Telegram 机器人")
    parser.add_argument(
        "-b", 
        "--bots", 
        type=str, 
        required=True, 
        help="要停止的机器人名称，支持多种分隔符(逗号、空格、分号、竖线)，例如: -b 'apple,seashore;stu'"
    )
    args = parser.parse_args()
    bot_names_str = parse_bot_names(args.bots)
    print("解析后的机器人名称列表:", bot_names_str)
    if not bot_names_str:
        print("错误: 未提供有效的机器人名称")
        return
    result = call_batch_stop_bot(bot_names_str)
    print("API 返回结果:", result)

if __name__ == "__main__":
    main()
