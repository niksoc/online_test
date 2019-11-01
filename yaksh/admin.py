from yaksh.models import Question, Quiz, QuestionPaper, Profile, LanguageOption, StudentActivityLog
from yaksh.models import (TestCase, StandardTestCase, StdIOBasedTestCase,
                          Course, AnswerPaper)
from django.contrib import admin


class AnswerPaperAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name', 'user__last_name', 'user__username',
                     "question_paper__quiz__description", "user_ip"]


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name', 'user__last_name', 'user__username',
                     "roll_number", "institute", "department"]


class StudentActivityLogAdmin(admin.ModelAdmin):
    list_display = ('module', 'course', 'level', 'student', 'timestamp', 'label', 'value')
    search_fields = ('type', 'student__first_name', 'student__last_name', 'quiz')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Question)
admin.site.register(TestCase)
admin.site.register(StandardTestCase)
admin.site.register(StdIOBasedTestCase)
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(QuestionPaper)
admin.site.register(AnswerPaper, AnswerPaperAdmin)
admin.site.register(LanguageOption)
admin.site.register(StudentActivityLog, StudentActivityLogAdmin)
