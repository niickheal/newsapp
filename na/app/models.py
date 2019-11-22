from django.db import models

def upload_feed_image(instance,filename):
	return "feed_images/{filename}".format(filename=filename)

class Feed(models.Model):
	headline = models.CharField(max_length=120)
	desc = models.CharField(max_length=500)
	feed_images = models.ImageField(upload_to=upload_feed_image,null=True,blank=True)
	news_url = models.CharField(max_length=500,default=None)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __str__ (self):
		return self.headline