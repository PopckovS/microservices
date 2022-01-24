from GraphTypes import InsertNewsOneArgs, InsertNewsOneOutput
from flask import Flask, request, jsonify
import os
from HasuraClient import HasuraClient

"""
Если запускать самостоятельно то требуется задать 2 переменных окружения:
    FLASK_PORT=9006 HASURA_URL=http://localhost:9004/v1/graphql python3 server.py
"""

HASURA_URL = os.environ['HASURA_URL']
# заголовки для авторизации в Hasura
# HASURA_HEADERS = {"X-Hasura-Admin-Secret":  ""}

client = HasuraClient(
    url=HASURA_URL,
    # headers=HASURA_HEADERS
)

app = Flask(__name__)


# InsertMainNewsOneDerived
@app.route('/InsertNewsOne', methods=['POST'])
def InsertNewsOne():
    """ Web hook для создания одной новой новости """

    # получаем данные от hasura
    args = InsertNewsOneArgs.from_request(request.get_json())

    # уникальная бизнес логика
    title = f'Заголовок: {args.title}'
    content = f'Контент: {args.content}'

    # отправляем данные в hasura и получаем ответ
    result = client.insert_main_news_one(args.cat, content, title)

    # если запрос был успешен то, отправляем данные обратно в hasura
    if result.get("errors"):
        return {"message": result["errors"][0]["message"]}, 400
    else:
        user = result["data"]["insert_main_news_one"]
        return InsertNewsOneOutput(**user).to_json()


@app.route('/')
def main():
    return f"Hello, World! {os.environ['FLASK_PORT']}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['FLASK_PORT'], debug=True)
