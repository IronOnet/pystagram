# post endpoint (CRUD) 
    create_post(user_id, content) 
    read_post(user_id, post_id) 
    # Photo
        upload_photo(user_id, encoded_photo): /photos/upload 
        read_photo(photo_id): /photos/{id}
        delete_photo(photo_id): /photos/{id}
    # Video 
        upload_video(user_id, video_payload): /videos/upload 
        read_video(user) 
        delete_video(video_id): /videos/{id}
# user endpoint (CRUD) 
    - create_user(user_data) 
    - update_user(user_id) /users/{id}
    - read_user(user_id) :/ users/{id} 
# comment endpoint (CRUD)
    add_comment(user_id, post_id, text) 
    read_comment(post_id, comment_id)
    reply_comment(post_id, comment_id)

# Following endpoint:  
    - follow_user(user_id): /following/{id} 
    - unfollow_user(user_id): /following/{id}
    - get_followers(user_id): /following/

# Bookmarks endpoint: 
    - create_bookmark(post_id, user_id) 
    - delete_bookmark(post_id)

# User profiles endpoints 
    - get_user_profile(user_id) 
    - update_user_profile(profile_id) :/profiles/{id} 
    - delete_user_profile(profile_id): /profiles/{id}
