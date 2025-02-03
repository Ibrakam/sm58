from db import get_db
from db.models import PostPhoto, UserPost, Comment, Hashtag


"""
UserPost

1. добавление поста add_post_db(user_id, main_text, hashtag) 
2. получение постов get_all_or_exact_post(post_id=0)
3. удаление пота delete_post_db(post_id)
4. изменение поста update_post_db(post_idm new_hashtag)
"""


"""
Comment

1. добавлние коммента add_comment_db(user_id, post_id, text)
2. получение комментов get_all_or_exact_comments(comment_id=0)
3. удаление коммента delete_comment_db(comment_id)
4. изменение коммента update_comment_db(comment_id, new_text)
"""


"""
Hashtag

1. добавление хэштега add_hashtag_db(hashtag_text)
2. получение хэштега get_all_or_exact_hashtags(hashatg_text=None)
3. удаление хэштега delete_hashtag_db(hashtag_id)
4. PostPhoto: добавление фото add_photo_db(post_id, photo_file)
"""