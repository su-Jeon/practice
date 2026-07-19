import pandas as pd
import os

현재폴더 = os.path.dirname(os.path.abspath(__file__))
데이터폴더 = os.path.join(현재폴더, "data")
os.makedirs(데이터폴더, exist_ok=True)

지점별 = {
    "강남지점": {"계정": ["매출", "매출원가", "판관비"], "금액": [50000, 30000, 12000]},
    "홍대지점": {"계정": ["매출", "매출원가", "판관비"], "금액": [38000, 22000, 9000]},
    "부산지점": {"계정": ["매출", "매출원가", "판관비"], "금액": [41000, 25000, 11000]},
}

for 지점, 데이터 in 지점별.items():
    df = pd.DataFrame(데이터)
    df.to_excel(os.path.join(데이터폴더, f"{지점}.xlsx"), index=False)
    print("생성:", 지점)
