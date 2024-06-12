import os
from django.core.management.base import BaseCommand
from toolsApp.models import Image
from django.core.files import File
from pathlib import Path

class Command(BaseCommand):
    help = 'Load images into the ImageModel'

    def handle(self, *args, **kwargs):
        image_folder = Path('img-seperated')
        images = list(image_folder.glob('*'))  # List all files in the directory

        for image in images:
            image_name = image.stem  # Filename without the extension
            with image.open('rb') as img_file:
                django_file = File(img_file)  # Wrap the file object in Django's File class
                Image.objects.create(name=image_name, picture=django_file)
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded {image_name}'))



# import os
# from django.core.management.base import BaseCommand
# from imageloader.models import ImageModel
# from django.core.files import File
# from pathlib import Path

# class Command(BaseCommand):
#     help = 'Load images into the ImageModel and update picture field only, preserving the name field.'

#     def handle(self, *args, **kwargs):
#         image_folder = Path('img-seperated')
#         images = list(image_folder.glob('*'))  # List all files in the directory

#         for image in images:
#             image_name = image.stem  # Filename without the extension
#             try:
#                 existing_record = ImageModel.objects.get(name=image_name)
#                 with image.open('rb') as img_file:
#                     django_file = File(img_file)  # Wrap the file object in Django's File class
#                     existing_record.picture.save(image.name, django_file, save=True)
#                     self.stdout.write(self.style.SUCCESS(f'Updated picture for {image_name}'))
#             except ImageModel.DoesNotExist:
#                 self.stdout.write(self.style.WARNING(f'No existing record found for {image_name}, skipping...'))

# Save this script in imageloader/management/commands/load_images.py
