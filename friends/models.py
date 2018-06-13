from django.db import models


class Friends(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=80)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=32)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name
        

class Connections(models.Model):
    person = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name='person')
    connected_to = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name='connected_to')


class FriendRequest(models.Model):
    from_person = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name='from_person')
    to_person = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name='to_person')
    accepted = models.BooleanField(default=False)


class Messages(models.Model):
    msg_from = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name='msg_from')
    msg_to = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name='msg_to')
    content = models.TextField()
    date = models.DateField()
    time = models.TimeField()


