export default function VideoInfo({ result }) {

  return (

    <div className="bg-white rounded-xl shadow-md p-8 mb-8">

      <h2 className="text-2xl font-bold mb-6">
        📺 動画情報
      </h2>

      <p className="mb-3">
        <span className="font-bold">タイトル：</span>

        {result.title}
      </p>

      <p className="mb-3">
        <span className="font-bold">再生数：</span>

        {result.views.toLocaleString()} 回
      </p>

      <p className="mb-6">
        <span className="font-bold">動画時間：</span>

        {Math.floor(result.duration / 60)}分
        {Math.floor(result.duration % 60)}秒
      </p>

      <h3 className="text-xl font-bold mb-3">

        📝 AIによる要約

      </h3>

      <p className="leading-8 whitespace-pre-wrap">

        {result.summary}

      </p>

    </div>

  );

}