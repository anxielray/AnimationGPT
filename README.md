# AnimatioGPT - System Overview

AnimatioGPT is a system designed to generate interactive animations from user prompts, accompanied by scripts and interactive quizzes. It consists of a frontend interface and a backend composed of three sub-systems.

---

## 1. Frontend (User Interface Layer)

The frontend is the primary interface for users to interact with AnimatioGPT.

### Responsibilities
- Accept user input (topic, question, scenario)
- Display generated animation video
- Display script and interactive Q&A overlay
- Provide playback control and interaction

### Recommended Technologies
| Technology | Purpose |
|------------|---------|
| React / Next.js | Component-based UI |
| Three.js / WebGL | Real-time 3D animation rendering |
| TailwindCSS / Chakra UI | Responsive design |
| Socket.io / WebRTC | Stream animation in real-time |

---

## 2. Backend (Core System)

The backend is the brain of AnimatioGPT and consists of three main sub-systems:

### (A) AI Interpreter + Script/Q&A Generator
- Interprets user input
- Generates animation blueprint
- Produces narration scripts
- Creates quiz/checkpoint questions

#### Example Output (JSON)

```json
{
  "title": "How Black Holes Work",
  "scenes": [
    { "id": 1, "type": "3D", "objects": ["star","light"], "actions": ["collapse"] },
    { "id": 2, "type": "narration", "voice": "female", "text": "A black hole forms..." }
  ],
  "scriptText": "...full narration...",
  "quizQuestions": [
    {"q": "What causes a black hole?", "answers": ["Star collapse","Fusion","",""], "correct": "Star collapse"}
  ]
}
```

## (B) Animation Engine

- Converts blueprint into actual animations
- Handles object positioning, transitions, camera movement, and lighting
- Adds voiceovers and captions

### Technology Options

| Technology         | Benefits                              |
|-------------------|---------------------------------------|
| Blender + Python   | High realism, automated rendering     |
| Three.js / WebGPU  | Real-time rendering, interactivity    |
| Unity / Unreal     | Asset libraries, physics, advanced animation |

---

## (C) Interactive Animation Generator

- Embeds interactive features into animations
- Adds in-video checkpoints and questions
- Supports branching paths based on user responses
- Integrates overlays for text, hints, and highlights

### Example Interactive Output

```json
{
  "videoURL": "animation-file.mp4",
  "captions": "...",
  "interactiveEvents": [
    { "time": 50, "type": "question", "content": "Why do stars collapse?" }
  ]
}
```

## 3. System Workflow

```text
[User Input]
     ↓
Frontend → Backend
     ↓
AI Interpreter → generates script, scenes, questions
     ↓
Animation Engine → renders video frames
     ↓
Interactive Layer → adds quiz & interactive features
     ↓
Frontend → displays final animation + script + interactive content
```

## 4. Future Enhancements

| Feature                     | Description                        |
|------------------------------|------------------------------------|
| Voice Cloning               | Personalized narrators             |
| Motion-Captured Characters  | Realistic animations               |
| 2D vs 3D Modes              | User chooses animation style       |
| Storyboard Preview          | Edit before full render            |

---

## 5. Next Steps / Team Focus

- Define API endpoints and request/response schema
- Choose backend technology stack
- Build MVP for single-topic animation generation
- Integrate interactive quiz overlay
