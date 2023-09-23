from django.db import models


class RememberDice(models.Model):
    position = models.CharField(max_length=10)
    throw_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'position = {self.position}, time = {self.throw_time}'

    @staticmethod
    def stat(my_dict, pk, res):
        my_dict[pk] = res
        return my_dict
