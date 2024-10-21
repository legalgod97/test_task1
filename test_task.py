import os
import openai

# Замените этот ключ на свой API-ключ от OpenAI
openai.api_key = "YOUR_API_KEY"

def main():
  while True:
    query = input('Введите ваш запрос. Для выхода из приложения напишите "exit"')

    if query == "exit":
      print('До свидания!')
      break

    # Используем OpenAI ChatCompletion для получения ответа
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": query}
      ]
    )

    # Выводим ответ в консоль
    print(response.choices[0].message.content)
    print() # Добавляем пустую строку для разделения ответов

if __name__ == "__main__":
  main()