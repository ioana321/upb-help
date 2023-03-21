from django import template

register = template.Library()

@register.filter(name="search_odd")
def search_odd(day, hour):
    from college.models import Activity
    activities = Activity.objects.filter(day=day, week='Odd')
    activity = activities.filter(start_hour=hour).first()
    if activity:
        return activity
    else:
        activity2 = activities.filter(start_hour=hour-1).first()
        if activity2 and activity2.end_hour != hour and (activity2.end_hour == hour+1 or activity2.end_hour == hour+2):
            return activity2
        else:
            activity3 = activities.filter(start_hour=hour-2).first()
            if activity3 and activity3.end_hour == hour+1:
                return activity3
            else:
                return 0

@register.filter(name="search_even")
def search_even(day, hour):
    from college.models import Activity
    activities = Activity.objects.filter(day=day, week='Even')
    activity = activities.filter(start_hour=hour).first()
    if activity:
        return activity
    else:
        activity2 = activities.filter(start_hour=hour-1).first()
        if activity2 and activity2.end_hour != hour and (activity2.end_hour == hour+1 or activity2.end_hour == hour+2):
            return activity2
        else:
            activity3 = activities.filter(start_hour=hour-2).first()
            if activity3 and activity3.end_hour == hour+1:
                return activity3
            else:
                return 0

@register.filter(name="increment")
def increment(hour):
    return hour+1

