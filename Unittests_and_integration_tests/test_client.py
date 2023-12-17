#!/usr/bin/env python3
"""Parameterize and patch as decorators
Parameterize and patch as decorators
"""


from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import Mock, patch
import utils
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient(unittest.TestCase) class"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """test_org method method to unit-test"""
        gitorg = GithubOrgClient(org)
        gitorg.org()
        mock.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url"""
        with patch("client.GithubOrgClient.org") as mock:
            playload = {"repos_url": "a"}
            mock.return_value = playload

    @patch('client.get_json')
    def test_public_repos(self, mock):
        """Test that the mocked property and
        the mocked get_json was called once"""
        with patch("client.GithubOrgClient._public_repos_url") as mock:
            playload = {"repos_url": "a"}
            mock.return_value = playload

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """TestGithubOrgClient.test_has_license
        to unit-test GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @parameterized_class(("org_payload", "repos_payload",
                         "expected_repos", "apache2_repos"), TEST_PAYLOAD)
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """class and implement the setUpClass and tearDownClass
        which are part of the unittest.TestCase API"""
        def setUpClass(cls):
            """should mock requests.get to return
            example payloads found in the fixtures"""
            cls.get_patcher = patch('requests.get')
            cls.get_patcher.start()

        def tearDownClass(cls):
            """tearDownClass class method to stop the patcher"""
            cls.get_patcher.stop()
