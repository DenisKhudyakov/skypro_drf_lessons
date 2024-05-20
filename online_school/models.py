from django.db import models

from config import settings

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    """Модель курса, параметры курса: названеие, превью, описание"""

    title = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание")
    # upload_to - путь до папки, в которую будут сохраняться изображения
    preview_image = models.ImageField(
        upload_to="course_images", verbose_name="Превью", **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Владелец курса",
    )

    def __str__(self):
        return f"{self.title}, {self.description[:50]}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель лекции, параметры лекции: название, превью, ссылка на видео-курс"""

    name = models.CharField(max_length=100, verbose_name="Название лекции")
    description = models.CharField(
        max_length=50, verbose_name="Описание лучшей лекции", **NULLABLE
    )
    preview_image = models.ImageField(
        upload_to="lesson_images", verbose_name="Превью", **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="lessons",
        **NULLABLE,
    )
    video_link = models.URLField(verbose_name="Ссылка на видео-курс", **NULLABLE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Владелец лекции",
    )

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"
