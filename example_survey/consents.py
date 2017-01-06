import arrow

from dateutil.relativedelta import relativedelta

from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE

from django.apps import apps as django_apps

app_config = django_apps.get_app_config('edc_protocol')

subjectconsent_v1 = Consent(
    'example_survey.subjectconsent',
    version='1',
    start=arrow.utcnow().floor('hour') - relativedelta(years=1),
    end=arrow.utcnow().ceil('hour'),
    age_min=16,
    age_is_adult=18,
    age_max=64,
    gender=[MALE, FEMALE])

site_consents.register(subjectconsent_v1)
