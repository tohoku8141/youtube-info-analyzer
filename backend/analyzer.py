def calculate_metrics(
    transcript: str,
    summary: str,
    duration_seconds: float,
    information_density: int
):
    """
    各種評価値を計算する
    """

    transcript_length = len(transcript)
    summary_length = len(summary)

    # -----------------------------
    # 簡潔度
    # -----------------------------

    conciseness = summary_length / transcript_length

    # %

    conciseness_percent = round(conciseness * 100, 1)

    # -----------------------------
    # 話す速さ
    # -----------------------------

    speech_speed = transcript_length / duration_seconds

    speech_speed = round(speech_speed, 2)

    # -----------------------------
    # 話す速さを100点換算
    # （4文字/秒を100点として上限）
    # -----------------------------

    speech_score = min(speech_speed / 4 * 100, 100)

    # -----------------------------
    # 簡潔度を100点換算
    #
    # 要約率が小さいほど高得点
    # -----------------------------

    conciseness_score = conciseness

    conciseness_score *= 100 

    conciseness_score = max(0, min(100, conciseness_score))

    # -----------------------------
    # 総合情報量
    # -----------------------------

    total_score = (

        information_density * 0.4

        + speech_score * 0.4

        + conciseness_score * 0.2

    )

    total_score = round(total_score)

    # -----------------------------
    # ランク
    # -----------------------------

    if total_score >= 95:
        rank = "S+"

    elif total_score >= 90:
        rank = "S"

    elif total_score >= 80:
        rank = "A"

    elif total_score >= 70:
        rank = "B"

    elif total_score >= 60:
        rank = "C"

    elif total_score >= 50:
        rank = "D"

    else:
        rank = "E"

    return {

        "transcript_length": transcript_length,

        "summary_length": summary_length,

        "conciseness": conciseness_percent,

        "speech_speed": speech_speed,

        "information_density": information_density,

        "score": total_score,

        "rank": rank

    }
