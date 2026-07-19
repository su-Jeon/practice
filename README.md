# 학습 진행 상황 : https://su-jeon.github.io/start-ai/

# practice

Python 기초를 익히기 위한 연습 저장소입니다.

## excel-merger

`data/` 폴더의 엑셀 파일들을 모두 읽어 하나로 합치고, 구분별·항목별 집계를 내어
`output/통합결과.xlsx` 로 저장하는 연습용 도구입니다.

**익힌 것**
- pandas — `read_excel`, `concat`, `groupby`, `to_excel`
- glob — `*.xlsx` 패턴으로 폴더 내 파일 자동 탐색
- os.path — `join`으로 OS 무관한 경로 처리, `__file__` 기준 경로의 동작
- 함수 분리 — 찾기 / 읽기 / 합치기 / 저장하기로 역할을 나눔
- 예외 처리 — `try/except`로 파일 하나가 실패해도 전체가 중단되지 않게 처리

**겪은 문제**
- 스크립트를 하위 폴더에 두어 `__file__` 기준 경로가 전부 어긋남
  → 에러 없이 잘못된 위치에 저장되어, 결과를 확인하기 전까지 몰랐음
- 환경에 Python이 두 개 설치되어 있어 라이브러리를 찾지 못함
  → 인터프리터 확인이 먼저라는 것을 배움
