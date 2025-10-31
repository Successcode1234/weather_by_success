from allauth.account.signals import user_signed_up, user_logged_in
from django.dispatch import receiver

@receiver(user_signed_up)
@receiver(user_logged_in)
def save_google_profile_pic(sender, request, user, **kwargs):
    if user.socialaccount_set.exists():
        social_account = user.socialaccount_set.first()
        provider = social_account.provider

        if provider == 'google':
            picture = social_account.extra_data.get('picture')
            if picture:
                user.profile_pic_url = picture
                user.google = True
                user.save()
