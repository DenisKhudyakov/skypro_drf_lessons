from rest_framework.test import APITestCase

from online_school.models import Lesson


class LessonsTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        """Тестирование создания урока"""
        data = {
            "name": "test_lesson",
            "description": "test_description",
        }
        response = self.client.post("/school/lessons/create/", data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_list_lessons(self):

        Lesson.objects.create(name="test_lesson", description="test_description")

        """Тестирование получения списка уроков"""
        response = self.client.get("/school/lessons/list/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 3,
                        "name": "test_lesson",
                        "description": "test_description",
                        "preview_image": None,
                        "video_link": None,
                        "course": None,
                        "owner": None,
                    }
                ],
            },
        )

    def test_update_lesson(self):
        """Тестирование обновления урока"""
        lesson = Lesson.objects.create(
            name="test_lesson", description="test_description"
        )
        data = {
            "name": "test_lesson_updated",
            "description": "test_description_updated",
        }
        response = self.client.put(
            f"/school/lessons/{lesson.id}/update/", data, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        lesson = Lesson.objects.create(
            name="test_lesson", description="test_description"
        )
        response = self.client.delete(f"/school/lessons/{lesson.id}/delete/")
        self.assertEqual(response.status_code, 204)
