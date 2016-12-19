# coding=utf-8

from dateutil.relativedelta import relativedelta

from edc_base.utils import get_utcnow

from survey.site_surveys import site_surveys
from survey.survey import Survey
from survey.survey_schedule import SurveySchedule


survey_one = SurveySchedule(
    name='example-survey-1',
    group_name='example-survey',
    start_date=(get_utcnow() - relativedelta(years=3)).date(),
    end_date=(get_utcnow() - relativedelta(years=2)).date())

survey_two = SurveySchedule(
    name='example-survey-2',
    group_name='example-survey',
    start_date=(get_utcnow() - relativedelta(years=2)).date(),
    end_date=(get_utcnow() - relativedelta(years=1)).date())

survey_three = SurveySchedule(
    name='example-survey-3',
    group_name='example-survey',
    start_date=(get_utcnow() - relativedelta(years=1)).date(),
    end_date=get_utcnow().date())

survey = Survey(
    name='annual',
    position=0,
    map_area='test_community',
    start_date=(get_utcnow() - relativedelta(years=3)).date(),
    end_date=(get_utcnow() - relativedelta(years=2)).date(),
    full_enrollment_date=(get_utcnow() - relativedelta(years=2)).date()
)
survey_one.add_survey(survey)

survey = Survey(
    name='annual',
    position=1,
    map_area='test_community',
    start_date=(get_utcnow() - relativedelta(years=2)).date(),
    end_date=(get_utcnow() - relativedelta(years=1)).date(),
    full_enrollment_date=(get_utcnow() - relativedelta(years=1)).date()
)
survey_two.add_survey(survey)

survey = Survey(
    name='annual',
    position=2,
    map_area='test_community',
    start_date=(get_utcnow() - relativedelta(years=1)).date(),
    end_date=get_utcnow().date(),
    full_enrollment_date=(get_utcnow()).date()
)
survey_three.add_survey(survey)

site_surveys.register(survey_one)
site_surveys.register(survey_two)
site_surveys.register(survey_three)
