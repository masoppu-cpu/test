import psycopg2
from flask import Flask, render_template, jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask! 🍋"

@app.route('/test')
def test():
    return render_template('test.html')  # ← HTMLを表示！

@app.route('/get_posts')
def get_posts():
    conn = psycopg2.connect(
    dbname="ana",
    user="ana",
    password="0000",
    host="localhost",  # またはリモートならIP
    port="5432"        # PostgreSQLのデフォルトポート
    )

    # カーソル作成
    cur = conn.cursor()

    # クエリ実行（例：全件取得）
    cur.execute("SELECT * FROM posts;")
    rows = cur.fetchall()

    # 結果を表示
    for row in rows:
        print(row)

    # 後片付け
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route('/hello')
def get_hello():
    print("来てるよ")
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
