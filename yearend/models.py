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
    ('NOT_ATTEND', 'Did Not Attend'),
    ('NOT_APPLIC', 'Not Applicable for this team'),
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

TEAMS = (
    ('House League', 'House League'),
    ('House League Bruins', 'House League Bruins'),
    ('House League Penguins', 'House League Penguins'),
    ('House League Rangers', 'House League Rangers'),
    ('House League Red Wings', 'House League Red Wings'),
    ('ADM', 'ADM'),
    ('ADM Bruins', 'ADM Bruins'),
    ('ADM Canucks', 'ADM Canucks'),
    ('ADM Ducks', 'ADM Ducks'),
    ('ADM Flyers', 'ADM Flyers'),
    ('ADM Lightning', 'ADM Lightning'),
    ('ADM Penguins', 'ADM Penguins'),
    ('ADM Coyotes', 'ADM Coyotes'),
    ('ADM Full-ice 1', 'ADM Full-ice 1'),
    ('ADM Full-ice 2', 'ADM Full-ice 2'),
    ('ADM Full-ice 3', 'ADM Full-ice 3'),
    ('Learn To Skate Session 1', 'Learn To Skate Session 1'),
    ('Learn To Skate Session 2', 'Learn To Skate Session 2'),
    ('Girls U14a', 'Girls U14a'),
    ('Girls U14b', 'Girls U14b'),
    ('Girls U12a', 'Girls U12a'),
    ('Girls U12b', 'Girls U12b'),
    ('Girls U10', 'Girls U10'),
    ('Bantams', 'Bantams'),
    ('Bantam A', 'Bantam A'),
    ('Bantam B1', 'Bantam B1'),
    ('Bantam B2', 'Bantam B2'),
    ('PeeWee A', 'PeeWee A'),
    ('PeeWee B', 'PeeWee B'),
    ('Squirt A', 'Squirt A'),
    ('Squirt B White', 'Squirt B White'),
    ('Squirt B Green', 'Squirt B Green'),
    ('Mite A', 'Mite A'),
    ('Middle School Boys Team 1', 'Middle School Boys Team 1'),
    ('Middle School Boys Team 2', 'Middle School Boys Team 2'),
    ('Middle School Girls', 'Middle School Girls'),
    ('Girls U19 Green', 'Girls U19 Green'),
    ('Midget A', 'Midget A'),
    ('Midget B', 'Midget B'),
    ('Midget Full Season', 'Midget Full Season'),
    ('Goalies', 'Goalies'),
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
    
    team_level = models.CharField(max_length=200, choices=TEAMS)
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
