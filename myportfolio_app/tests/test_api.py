import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.apps import apps


@pytest.mark.django_db
def test_project_list_api():
    Project = apps.get_model("myportfolio_app", "Project")

    client = APIClient()

    Project.objects.create(title="Project 1", description="Description 1")
    Project.objects.create(title="Project 2", description="Description 2")

    response = client.get("/api/projects/")

    assert response.status_code == status.HTTP_200_OK

    assert len(response.data["results"]) == 2

    assert response.data["results"][0]["title"] == "Project 1"
    assert response.data["results"][1]["title"] == "Project 2"


@pytest.mark.django_db
def test_article_list_api():
    Article = apps.get_model("myportfolio_app", "Article")

    client = APIClient()

    Article.objects.create(title="Article 1", description="Description 1")
    Article.objects.create(title="Article 2", description="Description 2")

    response = client.get("/api/articles/")

    assert response.status_code == status.HTTP_200_OK

    assert len(response.data["results"]) == 2

    assert response.data["results"][0]["title"] == "Article 1"
    assert response.data["results"][1]["title"] == "Article 2"