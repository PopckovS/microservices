Запросы для нашей тестовой БД
---
---

Запросы
---
```

# Получение записей по id
query MyQuery {
 main_news(where: {main_category: {id: {_eq: 3}}}) {
   content
   category_id_id
   id
 }
}
```


Мутации
---
```
# Вставка новой записи без категории
mutation {
  insert_main_news(objects: {
    title: "Тест запись", 
    content: "Тест текст"
  }) {
    returning {
      id
    }
  }
}

# Вставка новой записи с категорий
mutation {
  insert_main_news(objects: {
    title: "Тест запись", 
    content: "Тест текст", 
    category_id_id: 1
  }) {
    returning {
      id
    }
  }
}


```


Мой IP

    172.25.49.217

    http://172.25.49.217:9006/addNews


    title = f'Заголовок: {args.title}'
    content = f'Контент: {args.content}'

    return addNewsOutput(title=title, content=content).to_json()


Мутация на вставку данных Действие вариант №1 

Запрос для нее
```
type Mutation {
  addNews(
    title: String!
    content: String!
  ): addNewsOutput
}

type addNewsOutput {
  title: String!
  content: String!
}
```

Мутация
```
mutation {
  addNews(
    content: "Текст для хука", 
    title: "Заголовок для хука"
  ) {
    content
    title
  }
}
```


Мутация на вставку данных Действие вариант №2





