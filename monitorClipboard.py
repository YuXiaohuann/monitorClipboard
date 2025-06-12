import pyperclip
import re
import time

# 正则表达式匹配 http://ip:port 或 https://ip:port
URL_PATTERN = re.compile(r'https?://([\d.:A-Za-z]+)')

def clean_clipboard():
    content = pyperclip.paste()

    match = URL_PATTERN.match(content)
    if match:
        ip_port = match.group(1)
        # 如果以 '/' 结尾，去掉它
        if ip_port.endswith('/'):
            ip_port = ip_port[:-1]
        print(f"检测到网址: {content}")
        print(f"已替换为: {ip_port}")
        pyperclip.copy(ip_port)
        return True
    return False

def monitor_clipboard(interval=1):
    print("开始监控剪贴板，按 Ctrl+C 停止...")
    try:
        while True:
            clean_clipboard()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n监控结束。")

if __name__ == "__main__":
    monitor_clipboard()