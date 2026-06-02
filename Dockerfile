# 베이스 이미지 지정
FROM python:3.10-slim
# 컨테이너 내부 기본 작업 디렉터리 설정
WORKDIR /app/

COPY  . /app/

RUN pip install -r requirements.txt

CMD python main.py
# 런타임에 외부와 통신할 내부 포트 명시
EXPOSE 80