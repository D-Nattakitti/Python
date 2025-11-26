# บันทึกไฟล์: plot_pm25_bangkok_this_month.py
# ใช้: python plot_pm25_bangkok_this_month.py
# หรือรันใน Jupyter / Colab (อย่าลืมติดตั้งแพ็กเกจก่อน: pip install pandas matplotlib requests python-dateutil)

import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
import math

# ====== ปรับได้: ตั้งเมืองและพารามิเตอร์ ======
CITY = "Bangkok"
PARAM = "pm25"   # parameter name ใน OpenAQ
# =================================================

# วันที่: เดือนนี้ ตั้งแต่วันแรกถึงตอนนี้ (เวลาเป็น UTC ISO format)
now_utc = datetime.now(timezone.utc)
start_of_month = now_utc.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
date_from = start_of_month.isoformat()
date_to = now_utc.isoformat()

# OpenAQ v3 measurements endpoint (ตัวอย่าง)
BASE_URL = "https://api.openaq.org/v3/measurements"

# API parameters: filter by city, parameter, date range, page size (limit)
params = {
    "city": CITY,
    "parameter": PARAM,
    "date_from": date_from,
    "date_to": date_to,
    "limit": 10000,   # เพิ่มให้เยอะพอ (max per request ขึ้นกับ API)
    "page": 1,
    # ถ้าข้อมูลเยอะเกินไป อาจต้องวน pagination
}

rows = []
print("Requesting data from OpenAQ...", CITY, date_from, "->", date_to)

while True:
    r = requests.get(BASE_URL, params=params, timeout=30)
    r.raise_for_status()
    j = r.json()
    results = j.get("results", [])
    if not results:
        break
    rows.extend(results)

    meta = j.get("meta", {})
    found = meta.get("found", None)
    limit = meta.get("limit", None)
    page = meta.get("page", None)
    # ถ้าไม่มี pagination หรือ ดึงครบแล้ว -> break
    if found is None or limit is None or page is None:
        break
    # ถ้ายังไม่ครบ ให้ไปหน้าต่อ
    if (page * limit) >= found:
        break
    params["page"] = page + 1

print(f"Got {len(rows)} measurements")

if len(rows) == 0:
    raise SystemExit("No PM2.5 data returned for that city/date range. Try another city or check API.")

# แปลงเป็น DataFrame
df = pd.DataFrame(rows)
# ที่ field ของ OpenAQ มักจะมี 'value' และ 'date' -> 'date' object contains 'utc' (ISO)
df['datetime_utc'] = pd.to_datetime(df['date'].apply(lambda d: d.get('utc') if isinstance(d, dict) else d))
df = df.set_index('datetime_utc')

# แปลง timezone เป็น Asia/Bangkok (UTC+7) เพื่ออ่านง่าย
df.index = df.index.tz_convert("Asia/Bangkok")

# คำนวณค่าเฉลี่ยรายวัน (daily mean)
daily = df['value'].resample('D').mean()

# ทำกราฟ
plt.figure(figsize=(12,5))
daily.plot(kind='bar', alpha=0.7)
plt.plot(daily.index, daily.values, marker='o', linestyle='-', linewidth=1)

# เส้นมาตรฐานไทย (ตัวอย่าง 37.5 µg/m³)
thai_standard = 37.5
plt.axhline(thai_standard, color='red', linestyle='--', linewidth=1, label=f"Thai standard {thai_standard} µg/m³")

plt.title(f"Daily mean PM2.5 in {CITY} — {start_of_month.strftime('%Y-%m-%d')} to {now_utc.strftime('%Y-%m-%d')}")
plt.ylabel("PM2.5 (µg/m³)")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
