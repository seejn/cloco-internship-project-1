def UserSerializer(obj):
    fields = ["id", "email", "username", "fullname", "contact", "address", "last_login", "date_joined"]
    values = [obj.id, obj.email, obj.username, obj.get_fullname(), obj.contact, obj.address, obj.last_login, obj.date_joined]

    # data = dict(zip(fields,values))
    data = {k:v for k,v in zip(fields,values)}
    return data