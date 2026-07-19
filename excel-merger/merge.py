import os
import glob
import pandas as pd 


def 엑셀파일_찾기(폴더경로):
    """폴더 안의 모든 엑셀 파일 경로를 리스트로 돌려준다."""
    
    # 폴더가 없으면 알려주고 빈 리스트 반환
    if not os.path.exists(폴더경로):
        print(f"[오류] 폴더가 없습니다: {폴더경로}")
        return []
    
    파일목록 = glob.glob(os.path.join(폴더경로, "*.xlsx"))
    
    # 엑셀이 하나도 없으면 알려주기
    if len(파일목록) == 0:
        print(f"[알림] 엑셀 파일이 없습니다: {폴더경로}")
        return []
    
    return 파일목록

def 엑셀_읽어오기(파일목록):
    """엑셀 파일들을 읽어서 표 리스트로 돌려준다. 파일명은 '구분' 열로 붙인다."""
    
    표목록 = []
    
    for 파일경로 in 파일목록:
        파일이름 = os.path.basename(파일경로)
        구분명 = 파일이름.replace(".xlsx", "")
        
        try:
            df = pd.read_excel(파일경로)
        except Exception as e:
            print(f"[건너뜀] {파일이름} — 읽기 실패: {e}")
            continue
        
        if df.empty:
            print(f"[건너뜀] {파일이름} — 내용이 비어 있음")
            continue
        
        df["구분"] = 구분명
        표목록.append(df)
        print(f"  읽음: {구분명} ({len(df)}행)")
    
    return 표목록

def 표_합치기(표목록):
    """여러 표를 하나로 이어붙인다."""
    
    if len(표목록) == 0:
        print("[오류] 합칠 표가 없습니다.")
        return None
    
    합본 = pd.concat(표목록, ignore_index=True)
    return 합본
def 결과_저장하기(합본, 저장폴더, 파일명="통합결과.xlsx"):
    """합본을 엑셀로 저장한다. 폴더가 없으면 만든다."""
    
    os.makedirs(저장폴더, exist_ok=True)
    저장경로 = os.path.join(저장폴더, 파일명)
    
    try:
        합본.to_excel(저장경로, index=False)
    except PermissionError:
        print(f"[오류] 파일이 열려 있습니다. 엑셀을 닫고 다시 실행하세요: {저장경로}")
        return None
    
    print(f"저장 완료: {저장경로}")
    return 저장경로
현재폴더 = os.path.dirname(os.path.abspath(__file__))
데이터폴더 = os.path.join(현재폴더, "data")
출력폴더 = os.path.join(현재폴더, "output")

print("=" * 40)
print("엑셀 파일 통합 도구")
print("=" * 40)

파일들 = 엑셀파일_찾기(데이터폴더)
print(f"찾은 파일: {len(파일들)}개")

표들 = 엑셀_읽어오기(파일들)

합본 = 표_합치기(표들)

if 합본 is not None:
    print("\n===== 통합 결과 =====")
    print(합본)
    
    print("\n===== 구분별 합계 =====")
    print(합본.groupby("구분")["금액"].sum())
    
    print("\n===== 계정별 합계 =====")
    print(합본.groupby("계정")["금액"].sum())
    
    결과_저장하기(합본, 출력폴더)
else:
    print("처리할 데이터가 없어 종료합니다.")
