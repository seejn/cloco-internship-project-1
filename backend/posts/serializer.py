def PostSerializer(obj):
    fields = ["id", "title", "content", "post_image", "is_deleted", "like_count", "created_at"]
    values = [obj.id, obj.title, obj.content, obj.post_image, obj.is_deleted, obj.like_count, obj.created_at]

    # data = dict(zip(fields,values))
    data = {k:v for k,v in zip(fields,values)}
    return data
