# -*- coding: utf-8 -*-
"""ReadOnly FunkLoad test
"""
import unittest
from collective.funkload import testcase


class Readonly(testcase.FLTestCase):
    """ Read only load test scenario
        This test use a configuration file Readonly.conf.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')

    def test_ReadOnly(self):
        server_url = self.server_url

        self.get(server_url + "/",
            description="Get portada")

        self.get(server_url + "/noticias",
            description="Get Sección noticias")

        self.get(server_url + "/opinion",
            description="Get Sección Opinión")

        self.get(server_url + "/programas",
            description="Get Sección Programas")

        self.get(server_url + "/el-canal",
            description="Get Sección El Canal")

        self.get(server_url + "/programación",
            description="Get Sección Programación")

        self.get(server_url + "/sitemap",
            description="Get sitemap")

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")

def test_suite():
    return unittest.makeSuite(Readonly)

additional_tests = test_suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
