from django.db import models
from common.models import BaseModel
from pages.models import Pages


class Block(BaseModel):
    pages = models.ForeignKey(Pages, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(
        choices=[
            ("Text_block", "Text_block"),
            ("Video_block", "Video_block"),
            ("File_block", "File_block"),
            ("Image_block", "Image_block"),
        ],
        max_length=20,
    )

    title_uz = models.CharField(max_length=255, null=True, blank=True)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    image = models.ManyToManyField(
        "Image",
    )
    file = models.ManyToManyField(
        "File",
    )
    video = models.ManyToManyField(
        "Video",
    )


class Image(BaseModel):
    # block = models.ForeignKey(Block, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="block/image/")


class Video(BaseModel):
    # block = models.ForeignKey(Block, on_delete=models.CASCADE)
    type = models.CharField(
        choices=[("Video", "Video"), ("Link", "Link")], max_length=20
    )
    link = models.CharField(max_length=255, null=True, blank=True)
    video_file = models.FileField(upload_to="block/video/", null=True, blank=True)


class File(BaseModel):
    # block = models.ForeignKey(Block, on_delete=models.CASCADE)
    file = models.FileField(upload_to="block/file/")
