from random import SystemRandom
import string
from django.utils.text import slugify


def random_letters(k: int) -> str:
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))


def slugify_new(text: str, k: int = 5) -> str:
    return slugify(text) + '-' + random_letters(k)
