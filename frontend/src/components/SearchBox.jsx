export default function SearchBox({
  url,
  setUrl,
  analyzeVideo,
  loading,
}) {
  return (
    <div className="bg-white rounded-xl shadow-md p-8 mb-8">

      <h1 className="text-4xl font-bold text-center mb-8">
        🎬 YouTubeドーパミンチェッカー 🤪
      </h1>

      <input
        type="text"
        placeholder="YouTube URLを入力"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="w-full border rounded-lg p-4 text-lg"
      />

      <button
        onClick={analyzeVideo}
        disabled={loading}
        className="mt-6 w-full bg-blue-600 hover:bg-blue-700 text-white rounded-lg p-4 text-lg font-bold"
      >
        {loading ? "解析中..." : "ドーパミン検出開始"}
      </button>

    </div>
  );
}