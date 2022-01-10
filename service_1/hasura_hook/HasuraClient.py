from requests import request
import requests
from dataclasses import dataclass
import GraphQuery as graphql


@dataclass
class HasuraClient:
    """Делает запрос GraphQL к Hasura после обработки веб хуком"""
    url: str
    # headers: dict # задаем заголовки дял запроса

    def run_query(self, query: str, variables: dict, extract=False):
        """Выполняет запрос к Hasura"""
        request = requests.post(
            self.url,
            # headers=self.headers,
            json={"query": query, "variables": variables},
        )
        assert request.ok, f"Failed with code {request.status_code}"
        return request.json()

    def insert_main_news_one(self, cat, content, title):
        """Создание одной новости"""
        result = self.run_query(
            graphql.insert_main_news_one,
            {"cat": cat, "title": title, "content": content}
        )
        return result
