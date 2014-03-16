from django.db import models

EXPERIENCE_CHOICES = (
    ('POSITIVE', 'Positive'),
    ('NEUTRAL', 'Neutral'),
    ('NEGATIVE', 'Negative'),
)

USEFUL_CHOICES_ALWAYS = (
    ('USEFUL', 'Useful'),
    ('NEUTRAL', 'Neutral'),
    ('NOT_USEFUL', 'Not Useful'),
)

USEFUL_CHOICES = (
    ('USEFUL', 'Useful'),
    ('NEUTRAL', 'Neutral'),
    ('NOT_USEFUL', 'Not Useful'),
    ('NOT_ATTEND', 'Did Not Attend')
)

YES_SOME_NO = (
    ('YES', 'Yes'),
    ('SOME', 'Sometimes'),
    ('NO', 'No'),
)

YES_POSS_NO = (
    ('YES', 'Yes'),
    ('POSS', 'Possibly'),
    ('NO', 'No'),
)

ENOUGH = (
    ('ENOUGH', 'Enough'),
    ('TOO_MUCH', 'Too Much'),
    ('NOT_ENOUGH', 'Not Enough')
)

# Create your models here.
class FamilyResponse(models.Model):
    session_key = models.CharField(max_length=200)
    overall_experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    how_many_children = models.IntegerField()
    anything_else = models.CharField(max_length=2000)

class ChildResponse(models.Model):
    family_response = models.ForeignKey(FamilyResponse)
    child_index = models.IntegerField()
    
    team_level = models.CharField(max_length=200)
    overall_experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    
    # Useful program parts
    useful_coaches = models.CharField(max_length=10, choices=USEFUL_CHOICES_ALWAYS)
    useful_practices = models.CharField(max_length=10, choices=USEFUL_CHOICES)
    useful_short_weds = models.CharField(max_length=10, choices=USEFUL_CHOICES)
    useful_babson_skill = models.CharField(max_length=10, choices=USEFUL_CHOICES)
    useful_power_skating = models.CharField(max_length=10, choices=USEFUL_CHOICES)
    useful_goalie_skills = models.CharField(max_length=10, choices=USEFUL_CHOICES)
    useful_full_ice = models.CharField(max_length=10, choices=USEFUL_CHOICES)
    useful_half_ice = models.CharField(max_length=10, choices=USEFUL_CHOICES)

    head_coach_positive = models.CharField(max_length=10, choices=YES_SOME_NO)
    assistant_coaches_position = models.CharField(max_length=10, choices=YES_SOME_NO)
    session_amount = models.CharField(max_length=10, choices=ENOUGH)

    most_favorite_thing = models.CharField(max_length=2000)
    least_favorite_thing = models.CharField(max_length=2000)

    participate_next_season = models.CharField(max_length=10, choices=YES_POSS_NO)
    why_not_participate = models.CharField(max_length=2000)
