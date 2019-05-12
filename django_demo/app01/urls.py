from django.conf.urls import url
from app01.views import classes,student,teachers


urlpatterns = [
    url(r'^classes.html$',classes.get_classes),
    url(r'^add_classes.html$', classes.add_classes),
    url(r'^del_classes.html$',classes.del_classes),
    url(r'^edit_classes.html$', classes.edit_classes),

    url(r'^set_teacher.html$', teachers.set_teacher),

    url(r'^students.html$', student.get_student),
    url(r'^add_students.html$', student.add_students),
    url(r'^edit_students.html$', student.edit_students),
    url(r'^del_students.html$', student.del_student),
    url(r'^add_students.html$', student.add_students),

    url(r'^ajax4.html$', student.ajax_del),

    # 测试分页
    url(r'index.html$', student.get_student2),

    # 测试form
    url(r'^form_get_teacher$', teachers.get_teacher_list),
    url(r'^form_add_teacher$', teachers.add_teacher),
    url(r'^form_edit_teacher/(\d+)$', teachers.edit_teacher),

]



















