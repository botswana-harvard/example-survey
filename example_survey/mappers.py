from edc_map.site_mappers import site_mappers

from edc_map.mapper import Mapper

from .landmarks import TEST_LANDMARKS


class TestPlotMapper(Mapper):

    map_area = 'test_community'
    map_code = '01'
    pair = 0
    regions = None  # SECTIONS
    sections = None  # SUB_SECTIONS

    landmarks = TEST_LANDMARKS

    center_lat = -24.655949
    center_lon = 25.923439
    clinic_lat = -24.656037
    clinic_lon = 25.921765
    radius = 3.5
    location_boundary = ()

    intervention = True

site_mappers.register(TestPlotMapper)


class AnonymousMapper(Mapper):

    map_area = 'austin'
    map_code = '88'
    center_lat = -30.2671500
    center_lon = 97.7430600
    radius = 100.5
    location_boundary = ()

    intervention = True
    regions = None  # SECTIONS
    sections = None  # SUB_SECTIONS
    landmarks = None

site_mappers.register(AnonymousMapper)
