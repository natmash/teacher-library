from controlcenter import Dashboard, widgets, app_settings
from .models import Book, Checkout, Student

class TopBooksList(widgets.ItemList):
    title = 'Top Books'
    model = Book
    list_display = ('pk','title')
    list_display_links = ('pk')
    sortable = False
    limit = 10

class CheckedOutList(widgets.ItemList):
    def time_seconds(self, obj):
        return obj.start.strftime("%b %d, %Y %H:%M")

    def values(self):
        vals = Checkout.objects.filter(end=None)
        return vals

    time_seconds.admin_order_field = 'start'
    time_seconds.short_description = 'Precise Time'

    list_display = ('student', 'book', 'time_seconds',)
    title = 'Checked Out'
    model = Checkout
    limit = 25

class StudentList(widgets.ItemList):
    title = 'Top Students'
    model = Student

    def values(self):
        vals = Student.objects.order_by('-total_checkouts')
        return vals

    list_display = ('name', 'total_checkouts')

class ClassroomLibraryDashboard(Dashboard):
    widgets = (
        TopBooksList,
        CheckedOutList,
        StudentList
    )
