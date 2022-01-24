"""
Содержит GraphQL запросы для отправки в Hasura
"""

insert_main_news_one = """
mutation ($cat: Int!, $content: String!, $title: String!){
  insert_main_news_one(object: {
    category_id_id: $cat, 
    content: $content, 
    title: $title
  }) {
      id
  }
}
"""
