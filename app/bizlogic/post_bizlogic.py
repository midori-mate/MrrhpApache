
"""Post bizlogic
"""

from django.shortcuts import get_object_or_404
from app.models import *
from app.usrlib import consts, common
import pytz
from django.conf import settings
from django.utils import timezone


def get_post_obj_by_code(code):
    """Get one post by code. It occurs 404 when no post is found."""
    return get_object_or_404(
        Post,
        code=code,
        publish_at__lte=timezone.now(),
    )


def format_post(post_obj, lang, require_body=False):
    """Get one post by code. It occurs 404 when no post is found.
    This method organizes post data for display on tpl file.
    """

    # TODO: Here change UTC time in DB to Japan time. But it may be better way to do this.
    post_obj.publish_at = post_obj.publish_at.astimezone(pytz.timezone(settings.TIME_ZONE))

    # Decide which body will be displayed.
    displayed_body = ''
    if require_body:
        if post_obj.html:
            displayed_body = post_obj.html
        else:
            displayed_body = common.dp_lang(lang,
                                            post_obj.get_markdownified_body_ja(),
                                            post_obj.get_markdownified_body_en())

    return {
        'title'     : common.dp_lang(lang, post_obj.title_ja, post_obj.title_en), # Depends on lang
        'code'      : post_obj.code,                                              # As it is
        'publish_at': date_utils.format_by_lang_Ymd(lang, post_obj.publish_at),   # Change format depends on lang
        'thumbnail' : post_obj.thumbnail,                                         # As it is
        'body'      : displayed_body,                                             # Be made above.
        'tag'       : {                                                           # As it is.
            'name': common.dp_lang(lang, post_obj.tag.name_ja, post_obj.tag.name_en),
            'code': post_obj.tag.code,
        },
        'no_en_version': not post_obj.body_en,                                    # If has English body
        # TODO: Make archive datetime aware and this line available.
        # 'is_before2018': date_utils.is_before_2018(post.publish_at),
    }