export default function Comments({ comments }) {

  return (

    <div className="bg-white rounded-xl shadow-md p-8">

      <h2 className="text-2xl font-bold mb-6">

        💬 人気コメント TOP5

      </h2>

      {comments.map((comment, index) => (

        <div
          key={index}
          className="border rounded-lg p-5 mb-4"
        >

          <p className="mb-4 whitespace-pre-wrap">

            {comment.text}

          </p>

          <p className="font-bold">

            👍 {comment.likes.toLocaleString()}

          </p>

        </div>

      ))}

    </div>

  );

}