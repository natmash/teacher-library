from django.contrib import admin
from django import forms

from TeacherLibrary.models import Book, Student, Checkout
from django.contrib.auth.models import Group, User
from django.db.models import F

import datetime

from django.utils.html import format_html
from django.core.urlresolvers import reverse

from django.contrib import messages


def checkout(modeladmin, request, queryset):
    for book in queryset :
        if book.available == False :
            messages.error(request, book.title + ' is already checked out.')

        student = Student.objects.first()
        student.total_checkouts += 1
        student.save()

        checkout = Checkout()
        checkout.book = book
        checkout.start = datetime.datetime.now()
        checkout.student = student
        checkout.save()
    queryset.update(times_checked_out=F('times_checked_out') + 1, available=False)

def checkin(modeladmin, request, queryset):
    for book in queryset :
        if book.available :
            messages.error(request, book.title + ' is already checked in.')
        checkouts = Checkout.objects.filter(book=book, end = None)
        checkouts.update(end=datetime.datetime.now())
    queryset.update(available=True)

checkin.short_description = "Check-in Book"
checkout.short_description = "Checkout Book"

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'times_checked_out','available', 'student')
    empty_value_display = 'No Books Yet Available'
    actions = [checkout, checkin]
    search_fields = ['title']

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('book', 'student', 'start', 'end')
    search_fields = ['book']

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super(CheckoutAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Book, BookAdmin)
admin.site.register(Student)
admin.site.register(Checkout, CheckoutAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)