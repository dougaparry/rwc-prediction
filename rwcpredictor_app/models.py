# from django.db import models
# from djangp.utils import timezone
# from django.core.files import File
# import datetime
#
# class Match(models.Model):
#     match_number = models.IntegerField(default=0)
#     match_date = models.DateTimeField()
#     match_time = models.DateTimeField()
#     match_location = models.CharField(max_length=200)
#     winner = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return self.match_number
#
#     def get_match_number(self):
#         return self.match_number
#
# class Team(models.Model):
#     match = models.ManyToManyField(Match)
#     team_name = models.CharField(max_length=200)
#     team_logo = models.ImageField(upload_to="thumbs/",blank=True,null=True,default='')
#     team_win_probability = FloatField(default=0)
#
#     def image(self):
#         return '<a href="/mdia/{0}"><img src="/media/{0}"></a>'.format(self.thumbnail)
#     image.allow_tags = True
#
#     def __unicode__(self):
#         return self.team_name
#
#
# # Create your models here.
