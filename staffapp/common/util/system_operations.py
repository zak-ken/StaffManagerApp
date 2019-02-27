"""
This module handles system operations, e.g. delete drive files, moving drive files, updating and replacing drive files.
"""

from os import remove
from django.conf import settings


def delete_image(image_path=None):
    """
    :param image_path: Mandatory
    This function deletes the image from storage.
    """
    if not image_path:
        return None
    full_path = '{}{}'.format(settings.MEDIA_ROOT, image_path)
    remove(full_path)
