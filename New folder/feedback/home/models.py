from django.db import models

# Create your models here.

class Qestions(models.Model):
    QUESTION_CHOICES = ((
        ("Text", "Text"), ("BigText", "BigText"), ("Radio", "Radio"), ("Checkbox", "Checkbox")
    ))
    
    question=models.CharField(max_length=100)
    question_type=models.CharField(max_length=100,choices=QUESTION_CHOICES)
    
    def __str__(self):
        return self.question

class Options(models.Model):
    question=models.ForeignKey(Qestions, related_name='options', on_delete=models.CASCADE)
    option=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.option} for {self.question}"

    

class CustomerFeedback(models.Model):
    question = models.ManyToManyField(Qestions)
    timestamp = models.DateTimeField(auto_now_add=True)
    

class CustomerResponse(models.Model):
    feedback = models.ForeignKey(CustomerFeedback, on_delete=models.CASCADE)
    question = models.ForeignKey(Qestions, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    selected_options = models.ManyToManyField(Options, blank=True)
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
