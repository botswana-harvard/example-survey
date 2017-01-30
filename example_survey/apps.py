from django.apps import AppConfig as DjangoAppConfig

from edc_base_test.apps import AppConfig as EdcBaseTestAppConfigParent
from edc_device.apps import AppConfig as EdcDeviceAppConfigParent, DevicePermission
from edc_device.constants import SERVER, CENTRAL_SERVER, CLIENT
from edc_map.apps import AppConfig as EdcMapAppConfigParent
from survey.apps import AppConfig as SurveyAppConfigParent
from survey import S


class AppConfig(DjangoAppConfig):
    name = 'example_survey'


class EdcBaseTestAppConfig(EdcBaseTestAppConfigParent):
    consent_model = 'example_survey.subjectconsent'
    survey_group_name = 'example-survey'


class EdcMapAppConfig(EdcMapAppConfigParent):
    verbose_name = 'Example Mappers'
    mapper_model = 'plot.plot'
    mapper_survey_model = 'survey.survey'
    landmark_model = 'example_survey.landmark'
    verify_point_on_save = False
    zoom_levels = ['14', '15', '16', '17', '18']


class EdcDeviceAppConfig(EdcDeviceAppConfigParent):

    device_permissions = {
        'plot.plot': DevicePermission(
            model='plot.plot',
            create_roles=[SERVER, CENTRAL_SERVER, CLIENT],
            change_roles=[SERVER, CENTRAL_SERVER, CLIENT])
    }


class SurveyAppConfig(SurveyAppConfigParent):
    current_surveys = [
        S('example-survey.example-survey-1.annual.test_community'),
        S('example-survey.example-survey-2.annual.test_community'),
        S('example-survey.example-survey-3.annual.test_community')]
