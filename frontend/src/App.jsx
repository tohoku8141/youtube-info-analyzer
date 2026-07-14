import { useState } from "react";

import SearchBox from "./components/SearchBox";
import VideoInfo from "./components/VideoInfo";
import Metrics from "./components/Metrics";
import Comments from "./components/Comments";

function App() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function analyzeVideo() {
    if (!url.trim()) {
      alert("YouTube URLを入力してください");
      return;
    }

    setLoading(true);
    setResult(null);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          url: url,
        }),
      });

      if (!response.ok) {
        throw new Error("解析に失敗しました");
      }

      const data = await response.json();

      setResult(data);
    } catch (err) {
      console.error(err);
      setError("解析中にエラーが発生しました。");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 py-10">

      <div className="max-w-5xl mx-auto px-5">

        <SearchBox
          url={url}
          setUrl={setUrl}
          analyzeVideo={analyzeVideo}
          loading={loading}
        />

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 rounded-lg p-4 mb-8">
            {error}
          </div>
        )}

        {result && (
          <>
            <VideoInfo result={result} />

            <Metrics result={result} />

            <Comments comments={result.comments} />
          </>
        )}

      </div>
    </div>
  );
}

export default App;