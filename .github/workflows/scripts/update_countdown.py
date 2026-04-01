import re
from datetime import date

TARGET_DATE = date(2026, 6, 7)
README_PATH = "README.md"

def calculate_days_left():
    today = date.today()
    delta = TARGET_DATE - today
    return delta.days if delta.days >= 0 else 0

def update_readme():
    days_left = calculate_days_left()
    
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = f"距离高考还有 **{days_left}** 天"
    
    start_marker = "<!-- COUNTDOWN:START -->"
    end_marker = "<!-- COUNTDOWN:END -->"
    
    pattern = re.compile(
        rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
        re.DOTALL
    )
    
    replacement = f"{start_marker}\n{new_content}\n{end_marker}"
    updated_content = pattern.sub(replacement, content)
    
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)
    
    print(f"✅ 倒计时已更新：{days_left} 天")

if __name__ == "__main__":
    update_readme()
