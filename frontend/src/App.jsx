import { useState } from "react";
import axios from "axios";

function App() {
  const [topic, setTopic] = useState("");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);

  const generate = async () => {
    if (!topic.trim()) return;
    setLoading(true);
    setResponse(null);

    try {
      const res = await axios.post("http://127.0.0.1:8000/generate", { topic });
      setResponse(res.data);
    } catch (err) {
      console.error(err);
      alert("Error generating animation. Check backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "30px", maxWidth: "900px", margin: "0 auto" }}>
      <h1 style={{ textAlign: "center", marginBottom: "20px" }}>🎬 AnimatioGPT</h1>
      <p style={{ textAlign: "center", color: "#555" }}>
        Enter a topic and generate an interactive animation with script and quiz!
      </p>

      {/* Input Section */}
      <div style={{ display: "flex", marginTop: 20, gap: 10 }}>
        <input
          style={{ flex: 1, padding: "10px", fontSize: "16px", borderRadius: "5px", border: "1px solid #ccc" }}
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="Enter topic (e.g. Black Holes)"
        />
        <button
          onClick={generate}
          disabled={loading}
          style={{
            padding: "10px 20px",
            fontSize: "16px",
            borderRadius: "5px",
            border: "none",
            backgroundColor: "#4f46e5",
            color: "#fff",
            cursor: loading ? "not-allowed" : "pointer",
          }}
        >
          {loading ? "Generating..." : "Generate"}
        </button>
      </div>

      {/* Response Section */}
      {response && (
        <div style={{ marginTop: 30, display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20 }}>
          {/* Animation Placeholder */}
          <div style={{ padding: 20, border: "1px solid #ccc", borderRadius: 8, minHeight: 200 }}>
            <h2 style={{ marginTop: 0 }}>🎥 Animation</h2>
            <p style={{ color: "#777" }}>
              Animation would render here using the blueprint from backend.
            </p>
          </div>

          {/* Script */}
          <div style={{ padding: 20, border: "1px solid #ccc", borderRadius: 8, minHeight: 200 }}>
            <h2 style={{ marginTop: 0 }}>📜 Script</h2>
            <p>{response.script}</p>
          </div>

          {/* Quiz Section */}
          <div style={{ padding: 20, border: "1px solid #ccc", borderRadius: 8, gridColumn: "span 2" }}>
            <h2 style={{ marginTop: 0 }}>❓ Quiz</h2>
            <ul>
              {response.questions.map((q, idx) => (
                <li key={idx} style={{ marginBottom: 10 }}>
                  {q}
                </li>
              ))}
            </ul>
          </div>

          {/* Blueprint JSON (Optional Debug) */}
          <div style={{ padding: 20, border: "1px solid #eee", borderRadius: 8, gridColumn: "span 2", background: "#fafafa" }}>
            <h2 style={{ marginTop: 0 }}>🗂 Blueprint (Debug)</h2>
            <pre style={{ fontSize: "14px", overflowX: "auto" }}>
              {JSON.stringify(response.blueprint, null, 2)}
            </pre>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
