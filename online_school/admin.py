from django.contrib import admin

from online_school.models import Course, Lesson, Payments


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "preview_image",
        "course",
        "video_link",
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")


@admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "paid_course", "paid_lesson", "amount", "payment_method")