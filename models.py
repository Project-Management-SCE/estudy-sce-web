from __future__ import division, unicode_literals
from decimal import Decimal

import swapper
from warnings import warn
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg, Count, Sum
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel

from . import app_settings, get_star_ratings_rating_model_name, get_star_ratings_rating_model


def _clean_user(user):
    if not app_settings.STAR_RATINGS_ANONYMOUS:
        if not user:
            raise ValueError(_("User is mandatory. Enable 'STAR_RATINGS_ANONYMOUS' for anonymous ratings."))
        return user
    return None


class RatingManager(models.Manager):
    def for_instance(self, instance):
        if isinstance(instance, self.model):
            raise TypeError("Rating manager 'for_instance' expects model to be rated, not Rating model.")
        ct = ContentType.objects.get_for_model(instance)
        ratings, created = self.get_or_create(content_type=ct, object_id=instance.pk)
        return ratings

    def ratings_for_instance(self, instance):
        warn("RatingManager method 'ratings_for_instance' has been renamed to 'for_instance'. Please change uses of 'Rating.objects.ratings_for_instance' to 'Rating.objects.for_instance' in your code.", DeprecationWarning)
        return self.for_instance(instance)

    def delete_existing(self, existing_rating):
        rating = existing_rating.rating
        existing_rating.delete()
        rating._user_rating_deleted = True
        return rating

    def rate(self, instance, score, user=None, ip=None, clear=False):
        if isinstance(instance, self.model):
            raise TypeError("Rating manager 'rate' expects model to be rated, not Rating model.")
        ct = ContentType.objects.get_for_model(instance)

        user = _clean_user(user)
        existing_rating = UserRating.objects.for_instance_by_user(instance, user)

        if existing_rating:
            if not app_settings.STAR_RATINGS_CLEARABLE and not app_settings.STAR_RATINGS_RERATE:
                raise ValidationError(_('Already rated.'))

            same_as_previous = existing_rating.score == score

            if (app_settings.STAR_RATINGS_CLEARABLE and clear) or \
                    (app_settings.STAR_RATINGS_RERATE_SAME_DELETE and same_as_previous):
                return self.delete_existing(existing_rating=existing_rating)
            elif score is not None:
                existing_rating.score = score
                existing_rating.save()
                return existing_rating.rating
        elif clear:
            # user has cleared without an existing_rating
            return
        else:
            rating, created = self.get_or_create(content_type=ct, object_id=instance.pk)
            return UserRating.objects.create(user=user, score=score, rating=rating, ip=ip).rating
