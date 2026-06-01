import json
import os
from fastapi import FastAPI, HTTPException
from model import Course

# FastAPI 앱 객체 생성
app = FastAPI()

# 데이터가 저장된 JSON 파일 경로 지정
DB_FILE = "courses.json"

# JSON 파일 읽기
def read_courses():
    # 파일이 존재하지 않으면 빈 리스트 반환
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# JSON 파일 쓰기
def write_courses(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 1. GET /courses 구현
# Postman에서 GET 요청 보내면 현재 저장된 전체 수강기록을 리턴
@app.get("/courses")
async def get_courses():
    data = read_courses()
    return data

# 2. POST /courses 구현 ---
@app.post("/courses")
async def add_course(course: Course):
    try:
        # 1. 기존 파일에 있던 수강기록 리스트를 읽어옴
        data = read_courses()
        
        #  model_dump() 대신 파이썬 표준 dict() 함수 사용
        new_course_dict = dict(course)
        
        # 2. 리스트 끝에 추가
        data.append(new_course_dict)
        
        # 3. 새 과목이 추가된 전체 리스트를 JSON 파일에 저장
        write_courses(data)
        
        # 4. 성공 응답 반환
        return {"msg": "Course added successfully", "added_course": course}
        
    except Exception as e:
        # 예외 처리: 서버 강제 종료 방지
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# 서버 실행 설정
if __name__ == "__main__":
    import uvicorn
    # 도커 환경 실행 위해 127.0.0.1 대신 0.0.0.0 사용
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)