from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Level, Student, FeeCategory, Fee
from dateutil import parser
from datetime import datetime
from dateutil.relativedelta import relativedelta
import ipdb

class LevelAdmin(admin.ModelAdmin):
    list_display = (u'id', u'level')
    ordering = ('id',)
admin.site.register(Level, LevelAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        u'first_name',
        u'last_name',
        u'father_name',
        u'mother_name',
        u'phone',
        u'address',
        u'date_of_birth',
        u'age',
        u'level',
    )

    def phone(self,obj):    	
    	return "%s-%s" % (obj.mobile_code, obj.seven_digit_phone)

    def age(self, obj):
    	today_date = datetime.now().date()
    	birth_date = obj.date_of_birth
    	# ipdb.set_trace()
    	difference = relativedelta(today_date, birth_date)
    	return "%s years " % str(difference.years) + "%s months" % difference.months
	def level(self, obj):
		return obj.level.level
    # fields = list_display + (('mobile_code','mobile_phone'),)
    list_filter = (u'level',)
    search_fields = ('first_name',)
    ordering = ('id',)

admin.site.register(Student, StudentAdmin)

class FeeCategoryAdmin(admin.ModelAdmin):
    list_display = (u'id', u'fee_category', u'fee_amount', u'description')
admin.site.register(FeeCategory, FeeCategoryAdmin)


class FeeAdmin(admin.ModelAdmin):
    list_display = (u'id', u'student', u'fee_category', u'date_of_payment','fee_amount','fee_paid','fee_for_month_of')
    list_filter = ('student', 'fee_category', u'date_of_payment',)
    search_fields = ('student__first_name','student__last_name')
    def fee_amount(self, obj):
    	return obj.fee_category.fee_amount
    def fee_for_month_of(self, obj):
        return obj.get_month_display()
	
    save_as = True


admin.site.register(Fee, FeeAdmin)

