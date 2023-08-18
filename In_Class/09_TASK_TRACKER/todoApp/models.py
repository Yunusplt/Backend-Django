from django.db import models

# Create your models here.


class Todo(models.Model):
    PRIOR_DEGREE=(
        (1,"High"),
        (2,"Medium"),
        (3,"Low")
    )

    task=models.CharField(max_length=50)
    description=models.TextField(null=True)
    priority=models.IntegerField(choices=PRIOR_DEGREE, default=2) 
    created_date=models.DateTimeField(auto_now_add=True)             #! auto_now_add ilkkez olusturulurken
    update_date=models.DateTimeField(auto_now=True)
    is_done=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.priority} - {self.task} - {self.created_date}"
    
    class Meta:
        ordering=["priority"]                                        #! öncelige göre sirala...