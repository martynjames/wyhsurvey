from django import forms
from models import FamilyResponse, ChildResponse

class FamilyOverviewForm(forms.ModelForm):
    class Meta:
        model = FamilyResponse
        fields = ['overall_experience', 'how_many_children']

class ChildIntialForm(forms.ModelForm):
    class Meta:
        model = ChildResponse
        fields = [
                    'team_level', 
                    'overall_experience'
                ]

class ChildUsefulForm(forms.ModelForm):
    class Meta:
        model = ChildResponse
        fields = [
                    'useful_coaches',
                    'useful_practices',
                    'useful_short_weds',
                    'useful_babson_skill',
                    'useful_power_skating',
                    'useful_goalie_skills',
                    'useful_full_ice',
                    'useful_half_ice',
                ]

class ChildFollowForm(forms.ModelForm):
    class Meta:
        model = ChildResponse
        fields = [
                    'head_coach_positive',
                    'assistant_coaches_position',
                    'session_amount',
                ]

class ChildCloseForm(forms.ModelForm):
    class Meta:
        model = ChildResponse
        fields = [
                    'most_favorite_thing',
                    'least_favorite_thing',
                    'participate_next_season',
                    'why_not_participate',
                ]

class FamilyCloseForm(forms.ModelForm):
    class Meta:
        model = FamilyResponse
        fields = ['anything_else']