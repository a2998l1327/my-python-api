from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ⚠️ 重要：設定 CORS
# 這裡先允許所有來源 (*)，方便我們第一次測試連線
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "success", "message": "API Server 已啟動！"}

@app.get("/api/hello")
def say_hello():
    return {
        "status": "success",
        "message": "Hello! 這是來自 Python API 的問候",
        "detail": "你已經成功串接前端與後端了！"
    }