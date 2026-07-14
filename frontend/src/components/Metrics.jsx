export default function Metrics({ result }) {

  const cards = [
    {
      title: "簡潔度 (要約文字数/字幕文字数)",
      value: result.conciseness + "%",
    },
    {
      title: "話す速さ (字幕文字数/動画時間)",
      value: result.speech_speed + "文字/秒",
    },
    {
      title: "AIによる情報密度評価",
      value: result.information_density,
    },
  ];

  return (
    <div className="bg-white rounded-xl shadow-md p-8 mb-8">

      <h2 className="text-2xl font-bold mb-6">
        🤪 ドーパミン検出結果
      </h2>

      {/* 上段3項目 */}
      <div className="grid grid-cols-3 gap-6">

        {cards.map((card) => (
          <div
            key={card.title}
            className="border rounded-lg p-5 text-center"
          >
            <p className="text-gray-500">
              {card.title}
            </p>

            <p className="text-3xl font-bold mt-2">
              {card.value}
            </p>

          </div>
        ))}

      </div>

      {/* 総合スコア */}

      <div className="border rounded-lg p-6 mt-8 text-center">

        <p className="text-gray-500">
          総合スコア
        </p>

        <p className="text-5xl font-bold mt-3">
          {result.score}
        </p>

      </div>

      {/* ランク */}

      <div className="border rounded-lg p-6 mt-6 text-center bg-blue-50">

        <p className="text-gray-500">
          ドーパミンランク
        </p>

        <p className="text-7xl font-extrabold text-blue-600 mt-3">
          {result.rank}
        </p>

      </div>

    </div>
  );
}