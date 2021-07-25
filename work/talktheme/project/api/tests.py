from django.test import TestCase
from .apis.talktheme.draw import drawTalkTheme

# Create your tests here.

result = drawTalkTheme()
print(result)