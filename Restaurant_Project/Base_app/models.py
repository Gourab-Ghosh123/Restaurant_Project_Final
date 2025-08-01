from django.db import models

# Create your models here.


class Item_list(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name = models.CharField(max_length = 15)
    description = models.TextField(blank = False)
    Price = models.IntegerField()
    Category = models.ForeignKey(Item_list , related_name='Name', on_delete = models.CASCADE)
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Item_name
    

class AboutUs(models.Model):
    Description = models.TextField(blank = False)


class Feedback(models.Model):
    Username = models.CharField(max_length = 15)
    Description = models.TextField(blank = False)
    rating = models.IntegerField()
    Image = models.ImageField(upload_to='Items/', blank=True)

    def __str__(self):
        return self.Username
    


class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.Name
    