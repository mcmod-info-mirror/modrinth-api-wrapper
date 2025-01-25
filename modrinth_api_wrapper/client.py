from typing import Optional, Union, List, Dict
from enum import Enum
import json

from modrinth_api_wrapper.models import Project, Version, SearchResult
from modrinth_api_wrapper.network import request


class SearchIndex(Enum):
    RELEVANCE = "relevance"
    DOWNLOADS = "downloads"
    FOLLOWS = "follows"
    NEWEST = "newest"
    UPDATED = "updated"


class Algorithm(Enum):
    SHA1 = "sha1"
    SHA512 = "sha512"


class Tag(Enum):
    CATEGORY = "category"
    LOADER = "loader"
    GAME_VERSION = "game_version"
    DONATION_PLATFORM = "donation_platform"
    PROJECT_TYPE = "project_type"
    SIDE_TYPE = "side_type"


class Client:
    """
    Modrinth API client.

    Reference: https://docs.modrinth.com/api/
    """
    def __init__(self, token: str = None, endpoint: str = "https://api.modrinth.com"):
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}" if token else ""}
        self.endpoint = endpoint

    def get_project(self, project_id: Optional[str], slug: Optional[str] = None) -> Project:
        if not project_id and not slug:
            raise ValueError("project_id and slug cannot be both None.")

        url = f"{self.endpoint}/v2/project/{project_id or slug}"
        res = request(url, headers=self.headers)
        return Project(**res)

    def get_projects(self, ids: List[str]) -> List[Project]:
        url = f"{self.endpoint}/v2/projects"
        res = request(
            url, headers=self.headers, params={"ids": json.dumps(ids)}
        )
        return [Project(**item) for item in res]

    def search_project(
        self,
        query: Optional[str] = None,
        facets: Optional[str] = None,  # TODO
        index: Optional[Union[str, SearchIndex]] = SearchIndex.DOWNLOADS,
        offset: Optional[int] = None,
        limit: Optional[int] = 10,
    ) -> SearchResult:
        url = f"{self.endpoint}/v2/search"
        res = request(
            url,
            headers=self.headers,
            params={
                "query": query,
                "facets": facets,
                "index": index.value if isinstance(index, SearchIndex) else index,
                "offset": offset,
                "limit": limit,
            },
        )
        return SearchResult(**res)

    def list_project_versions(self, project_id: str) -> List[Version]:
        url = f"{self.endpoint}/v2/project/{project_id}/version"
        res = request(url, headers=self.headers)
        return [Version(**item) for item in res]

    def get_version(self, version_id: str) -> Version:
        url = f"{self.endpoint}/v2/version/{version_id}"
        res = request(url, headers=self.headers)
        return Version(**res)

    def get_versions(self, version_ids: List[str]) -> List[Version]:
        url = f"{self.endpoint}/v2/versions"
        res = request(
            url, headers=self.headers, params={"ids": json.dumps(version_ids)}
        )
        return [Version(**item) for item in res]

    def get_version_from_hash(
        self, sha1: Optional[str] = None, sha512: Optional[str] = None
    ) -> Version:
        if not sha1 and not sha512:
            raise ValueError("sha1 and sha512 cannot be both None.")
        url = f"{self.endpoint}/v2/version_file/{sha1 or sha512}"
        res = request(
            url,
            headers=self.headers,
            params={"algorithm": "sha1" if sha1 else "sha512", "multiple": False},
        )  # 没见过多个返回值的情况
        return Version(**res)

    def get_versions_from_hashes(
        self, hashes: List[str], algorithm: Union[str, Algorithm]
    ) -> Dict[str, Version]:
        url = f"{self.endpoint}/v2/version_files"
        res: dict = request(
            url,
            method="POST",
            headers=self.headers,
            json={
                "hashes": hashes,
                "algorithm": algorithm.value if isinstance(algorithm, Algorithm) else algorithm,
            },
        )
        return {key: Version(**item) for key, item in res.items()}

    def get_latest_version_from_hash(
        self,
        sha1: Optional[str] = None,
        sha512: Optional[str] = None,
        loaders: Optional[List[str]] = None,
        game_versions: Optional[List[str]] = None,
    ) -> Version:
        if not sha1 and not sha512:
            raise ValueError("sha1 and sha512 cannot be both None.")
        url = f"{self.endpoint}/v2/version_file/{sha1 or sha512}"
        res = request(
            url,
            method="GET",
            headers=self.headers,
            params={"algorithm": "sha1" if sha1 else "sha512"},
            json={"loaders": loaders, "game_versions": game_versions},
        )
        return Version(**res)

    def get_latest_versions_from_hashes(
        self,
        hashes: List[str],
        algorithm: Union[str, Algorithm],
        loaders: Optional[List[str]] = None,
        game_versions: Optional[List[str]] = None,
    ) -> Dict[str, Version]:
        url = f"{self.endpoint}/v2/version_files"
        res: dict = request(
            url,
            method="POST",
            headers=self.headers,
            json={
                "hashes": hashes,
                "algorithm": algorithm.value if isinstance(algorithm, Algorithm) else algorithm,
                "hashes": hashes,
                "loaders": loaders,
                "game_versions": game_versions,
            },
        )
        return {key: Version(**item) for key, item in res.items()}

    def get_tag(self, tag: Union[Tag, str]) -> Union[List, Dict]:
        url = f"{self.endpoint}/v2/tag/{tag.value if isinstance(tag, Tag) else tag}"
        res = request(url, headers=self.headers)
        return res