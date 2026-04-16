from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# FastAPI 範例
origins = [
    "https://your-project.vercel.app",
    "https://your-project.netlify.app",    # 新增
    "https://your-project.pages.dev",      # 新增
    "http://localhost:5173",               # 本地測試用
]

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