from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Title


def check_conformity_title_and_review(self):
    title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
    if len(title.reviews.filter(id=self.kwargs.get("review_id"))) == 0:
        raise serializers.ValidationError(
            "Обзор существует, но не относится к указанному произведению"
        )
