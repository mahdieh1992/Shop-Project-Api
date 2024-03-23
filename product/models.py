from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=500)
    parent=models.ForeignKey('self',related_name='child',null=True,blank=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name   

    def get_children(self):
        """
            get children
        """
        return Category.objects.filter(parent=self)

