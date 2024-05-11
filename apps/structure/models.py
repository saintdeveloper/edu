from django.db import models
from django.db import models
from apps.common.models import BaseModel

class Room(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Subject(BaseModel):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title
    

class Notification(BaseModel):
    users = models.ManyToManyField('users.Account', blank=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.id}'


class Chat(BaseModel):
    sender = models.ForeignKey('users.Account', on_delete=models.SET_NULL, null=True, related_name='sender_chat')
    reciver = models.ForeignKey('users.Account', on_delete=models.SET_NULL, null=True, related_name='reciver_chat')
    is_read = models.BooleanField(default=False)
    message = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return f'{self.sender.username} -> {self.reciver.username}'
    
class StudentGroup(BaseModel):
    title = models.CharField(max_length=225)
    room = models.ForeignKey(Room , on_delete=models.CASCADE, blank=True, null=True, related_name='room_groups')
    teacher = models.ForeignKey('users.Account', on_delete=models.SET_NULL, blank=True, null=True, related_name='teacher_groups')
    students = models.ManyToManyField('users.Account',blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True, related_name='subject_groups')
    duration = models.CharField(max_length=225, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    lesson_start = models.TimeField(blank=True, null=True)
    lesson_end = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Lesson(BaseModel):
    title = models.CharField(max_length=225)
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, blank=True, null=True)
    file = models.FileField()

    def __str__(self):
        return self.title

class Attendance(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey('users.Account', on_delete=models.SET_NULL,  blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson
    
class Task(BaseModel):
    title = models.CharField(max_length=225)
    grade = models.FloatField(default=0)
    deadline = models.DateTimeField()
    teacher = models.ForeignKey('users.Account', on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    file = models.FileField(upload_to='tasks/')

    def __str__(self):
        return self.title
    
class TaskSubmittion(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey("users.Account", on_delete=models.CASCADE)
    file = models.FileField(upload_to="task_submitions")

    def __str__(self):
        return self.task.title
    
class Payment(BaseModel):
    student = models.ForeignKey("users.Account", on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.username}-{self.price}"
    









