import json
import os

def load_json(file_path):
    """
    JSONファイルを読み込み、Pythonの辞書やリストとして返す関数
    """
    # ファイルの存在確認
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"ファイルが見つかりません: {file_path}")

    try:
        with open(file_path, "r", encoding="shift_jis") as f:
            data = json.load(f)  # JSON → Pythonオブジェクト
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"JSONの形式が不正です: {e}")
    except Exception as e:
        raise RuntimeError(f"予期しないエラー: {e}")

# 実行例
if __name__ == "__main__":
    # 読み込むJSONファイルのパス
    json_file = "sample.json"

    try:
        data = load_json(json_file)

        # データ全体を表示
        print("=== JSON全体 ===")
        print(data)

        # 特定のキーの値を呼び出す例
        if isinstance(data, dict) and "name" in data:
            print(f"名前: {data['name']}")

        # ネストされたデータの呼び出し例
        if isinstance(data, dict) and "address" in data:
            city = data["address"].get("city", "不明")
            print(f"都市: {city}")

    except Exception as e:
        print(f"エラー: {e}")
