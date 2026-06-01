# 베이스 이미지 지정
FROM python:3.10-slim
# 컨테이너 내부 기본 작업 디렉터리 설정
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 로컬 디렉터리 코드와 데이터를 컨테이너 내부로 복사
COPY . .

# 런타임에 외부와 통신할 내부 포트 명시
EXPOSE 8000

# 컨테이너 시작될 때 자동 실행할 웹 서버 명령어 설정
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]