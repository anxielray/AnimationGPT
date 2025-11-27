from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from topic_detection import detect_topic
from typing import List

# -------------------------
# 1. FastAPI App Setup
# -------------------------
app = FastAPI(title="AnimatioGPT Backend")

# Allow CORS for frontend (adjust origin for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# 2. Request / Response Models
# -------------------------
class AnimationRequest(BaseModel):
    topic: str

class BlueprintScene(BaseModel):
    id: int
    objects: List[str]
    actions: List[str]

class AnimationResponse(BaseModel):
    status: str
    prompt_received: str
    blueprint: List[BlueprintScene]
    script: str
    questions: List[str]

# -------------------------
# 3. Mock /generate Endpoint
# -------------------------
@app.post("/generate", response_model=AnimationResponse)
async def generate_animation(request: AnimationRequest):
    topic = request.topic

    # Mock blueprint (replace later with AI interpreter output)
    blueprint = [
        BlueprintScene(id=1, objects=["earth", "apple"], actions=["fall"]),
        BlueprintScene(id=2, objects=["tree"], actions=["sway"])
    ]

    script = f"This is a generated narration script about: {topic}"
    questions = [
        f"What did you learn about {topic}?",
        f"How can {topic} be applied in real life?"
    ]

    return AnimationResponse(
        status="success",
        prompt_received=topic,
        blueprint=blueprint,
        script=script,
        questions=questions
    )

class TopicRequest(BaseModel):
    text: str

@app.post("/detect_topic")
async def detect_topic_endpoint(req: TopicRequest):
    topic = detect_topic(req.text)
    return {"detected_topic": topic}

# -------------------------
# 4. Run App
# -------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
