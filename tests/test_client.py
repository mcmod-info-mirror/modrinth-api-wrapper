import pytest

from modrinth_api_wrapper import *


PROJECT_IDS = ["AANobbMI", "P7dR8mSH"]

SLUGS = ["fabric-api", "sodium"]

VERSION_IDS = ["3auffiOJ", "mnEhtGuH"]

SHA1 = [
    "9e1ccb3b136cff0715004bbd418c66eb38bb8383",
    "41594bd81f1e60e364f76b2e2bfca10cfdcf91bd",
]

SHA512 = [
    "5677d011800d88c5259a2a3c82d0e90b5dec83a7505fc7502a68a2ff7f21834564f02764dc8813f910bd768bff253892cf54ce7d3300d6d0bbc8b592db829251",
    "9135dd422a779d6e0c009adabf73091fd7e4de3e6f155b6f977c6380811af999bd1dbd416f0b0cd87ee159c46e20c900ff6b20184c3d5446bd4a3df3c553a5af",
]

TAG_NAMES = [
    "category",
    "loader",
    "game_version",
    "license",
    "donation_platform",
    "report_type",
    "project_type",
    "side_type",
]

client = Client()

@pytest.mark.search
def test_search_project():
    result = client.search_project(query="sodium")
    assert type(result) == SearchResult


@pytest.mark.project
def test_get_project():
    for project_id in PROJECT_IDS:
        project = client.get_project(project_id=project_id)
        assert type(project) == Project


@pytest.mark.project
def test_get_projects():
    projects = client.get_projects(ids=PROJECT_IDS)
    for project in projects:
        assert type(project) == Project
    projects = client.get_projects(ids=SLUGS)
    for project in projects:
        assert type(project) == Project


@pytest.mark.version
def test_get_project_versions():
    for project_id in PROJECT_IDS:
        versions = client.list_project_versions(project_id=project_id)
        for version in versions:
            assert type(version) == Version


@pytest.mark.version
def test_get_version():
    for version_id in VERSION_IDS:
        version = client.get_version(version_id=version_id)
        assert type(version) == Version


@pytest.mark.version
def test_get_versions():
    versions = client.get_versions(version_ids=VERSION_IDS)
    for version in versions:
        assert type(version) == Version


@pytest.mark.version_file
def test_get_version_from_hash():
    for sha1 in SHA1:
        version = client.get_version_from_hash(sha1=sha1)
        assert type(version) == Version
    for sha512 in SHA512:
        version = client.get_version_from_hash(sha512=sha512)
        assert type(version) == Version


@pytest.mark.version_file
def test_get_versions_from_hashes():
    versions = client.get_versions_from_hashes(hashes=SHA1, algorithm=Algorithm.SHA1)
    for version in versions.values():
        assert type(version) == Version
    versions = client.get_versions_from_hashes(
        hashes=SHA512, algorithm=Algorithm.SHA512
    )
    for version in versions.values():
        assert type(version) == Version


@pytest.mark.version_file
def test_get_latest_version_from_hash():
    for sha1 in SHA1:
        version = client.get_latest_version_from_hash(
            sha1=sha1, loaders=["fabric"], game_versions=["1.16.5"]
        )
        assert type(version) == Version
    for sha512 in SHA512:
        version = client.get_latest_version_from_hash(
            sha512=sha512, loaders=["fabric"], game_versions=["1.16.5"]
        )
        assert type(version) == Version


@pytest.mark.version_file
def test_get_latest_versions_from_hashes():
    versions = client.get_latest_versions_from_hashes(
        hashes=SHA1,
        algorithm=Algorithm.SHA1,
        loaders=["fabric"],
        game_versions=["1.16.5"],
    )
    for version in versions.values():
        assert type(version) == Version
    versions = client.get_latest_versions_from_hashes(
        hashes=SHA512,
        algorithm=Algorithm.SHA512,
        loaders=["fabric"],
        game_versions=["1.16.5"],
    )
    for version in versions.values():
        assert type(version) == Version


@pytest.mark.tag
def test_get_tag():

    for tag_name in TAG_NAMES:
        tag = client.get_tag(tag=tag_name)
        assert type(tag) == list or dict
