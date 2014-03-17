from django import forms
from models import FamilyResponse, ChildResponse

class FamilyOverviewForm(forms.ModelForm):
    how_many_children = forms.IntegerField(min_value=1)
    class Meta:
        model = FamilyResponse
        fields = ['overall_experience', 'how_many_children']
        labels = {
            "overall_experience": "How would you rate your family's overall experience with Westwood Youth Hockey this season?",
            "how_many_children": "How many children did you have in Westwood Youth Hockey this season?"
        }

class ChildIntialForm(forms.ModelForm):
    class Meta:
        model = ChildResponse
        fields = [
                    'team_level', 
                    'overall_experience',
                ]

        labels = {
            "team_level": "Team Level or Name",
            "overall_experience": "How would you rate your family's overall experience with this team?",
        }

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

        labels = {
            'useful_coaches': "Team coaches?",
            'useful_practices': "Team practices?",
            'useful_short_weds': "Short Wednesday skills sessions?",
            'useful_babson_skill': "Babson skill sessions?",
            'useful_power_skating': "Power skating?",
            'useful_goalie_skills': "Goalie skills?",
            'useful_full_ice': "Full ice games?",
            'useful_half_ice': "Half-ice games?",
        }


class ChildFollowForm(forms.ModelForm):
    class Meta:
        model = ChildResponse
        fields = [
                    'head_coach_positive',
                    'assistant_coaches_position',
                    'session_amount',
                ]

        labels = {
            'head_coach_positive': "Did you feel this team's head coach offered a positive learning environment?",
            'assistant_coaches_position': "Did you feel this team's assistant coaches offered a positive learning environment?",
            'session_amount': "Do you feel the total amount of ice sessions offered to your team each week (i.e. games, practices, skills and power skating) was:",
        }

class ChildCloseForm(forms.ModelForm):
    why_not_participate = forms.CharField(required=False, label="If not, why not?")

    class Meta:
        model = ChildResponse
        fields = [
                    'most_favorite_thing',
                    'least_favorite_thing',
                    'participate_next_season',
                    'why_not_participate',
                ]

        labels = {
            'most_favorite_thing': "What was your favorite thing about your experience with this team?",
            'least_favorite_thing': "What was your least favorite thing about your experience with this team?",
            'participate_next_season': "Do you plan to have this child participate in Westwood Youth Hockey next season?",
            'why_not_participate': "If not, why not?",
        }

class FamilyCloseForm(forms.ModelForm):
    anything_else = forms.CharField(required=False, label="Is there anything else you would like us to know?", max_length=2000)

    class Meta:
        model = FamilyResponse
        fields = ['anything_else']

