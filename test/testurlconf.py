from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from test.views import EmojiTestReplaceTagView, EmojiTestReplcaceUnicodeTagView

urlpatterns = patterns(
    '',
    url(r'', include('emoji.urls', app_name='emoji', namespace='emoji')),
    url(r'^all$', EmojiTestReplaceTagView.as_view(), name='emoji_test_list'),
    url(r'^replace-unicode/$', EmojiTestReplcaceUnicodeTagView.as_view(),
        name='emoji_replace_unicode_test'),
    url(r'^emoji-include-test$',
        TemplateView.as_view(template_name='emoji_include_tag.html'),
        name='emoji_include_test'),
    url(r'^emoji-load-test$',
        TemplateView.as_view(template_name='emoji_load_tag.html'),
        name='emoji_load_test'),
)
