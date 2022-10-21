from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,  # 모델이 만들어질 때
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # 모델이 업데이트 될 때
    )

    class Meta:
        abstract = True  # 데이터 베이스에 저장 x
