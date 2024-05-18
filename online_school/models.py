from django.db import models

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    """Модель курса, параметры курса: названеие, превью, описание"""

    title = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание")
    # upload_to - путь до папки, в которую будут сохраняться изображения
    preview_image = models.ImageField(
        upload_to="course_images", verbose_name="Превью", **NULLABLE
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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    video_link = models.URLField(verbose_name="Ссылка на видео-курс", **NULLABLE)

    def __str__(self):
        return f"{self.name}, {self.description[:20]}"

    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"
