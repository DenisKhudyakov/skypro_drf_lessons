import re

from rest_framework import serializers


class LessonsValidator:
    """Класс валидатор, который проверяет, youtube.com в ссылке на видео"""

    def __init__(self, url):
        self.url = url

    def __call__(self, value):
        value = self.url
        if re.search("youtube.com", value):
            raise serializers.ValidationError("Запрещенная ссылка на видео")


if __name__ == "__main__":
    url = "https://youtube.com/watch?v=dQw4w9WgXcQ"
    validator = LessonsValidator(url)
    validator(url)
