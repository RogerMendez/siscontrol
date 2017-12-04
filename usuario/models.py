# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
#from django.db.models.signals import post_save
#from django.dispatch import receiver


class Perfil(models.Model):
	user = models.OneToOneField(User, related_name='user', on_delete = models.CASCADE)
	photo = models.ImageField(upload_to = 'Profile Photo', blank=True, null=True, verbose_name='Fotografia')

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)

