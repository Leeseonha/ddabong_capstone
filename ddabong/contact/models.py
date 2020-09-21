from django.db import models

# Create your models here.
class Post(models.Model):
    B_TYPES = (
        ('A','A형'),
        ('B','B형'),
        ('AB','AB형'),
        ('O','O형'),
        ('Weak-A','Weak-A형'),
        ('Weak-B','Weak-B형'),
        ('RH-','RH-형'),
        ('RH+','RH+형'),
        ('Cis-AB','Cis-AB형'),
        ('MkMk','MkMk형'),
    )

    Regions = (
        ('Gangwon','강원'),
        ('Gyeonggi','경기'),
        ('Gyeongnam','경남'),
        ('Gyeongbuk ','경북'),
        ('Gwangju','광주'),
        ('Daegu','대구'),
        ('Busan','부산'),
        ('Seoul ','서울'),
        ('Incheon','인천'),
        ('Jeonnam','전남'),
        ('Jeonbuk','전북'),
        ('Jeju','제주'),
        ('Chungnam','충남'),
        ('Chungbuk','충북'),
    )

    Post_type = (
        ('Donor','공여자'),
        ('recipient','수혜자'),
    )

    post_type = models.CharField(max_length= 50, choices= Post_type)
    title = models.CharField(max_length= 200)
    pub_date = models.DateTimeField('date published')
    b_type = models.CharField(max_length=50, choices = B_TYPES)
    body = models.TextField()
    region = models.CharField(max_length= 50, choices=Regions)