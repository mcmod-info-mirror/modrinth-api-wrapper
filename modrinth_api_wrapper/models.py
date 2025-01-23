from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import datetime


class DonationUrl(BaseModel):
    id: Optional[str] = None
    platform: Optional[str] = None
    url: Optional[str] = None


class License(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    url: Optional[str] = None


class GalleryItem(BaseModel):
    url: str
    featured: bool
    title: Optional[str] = None
    description: Optional[str] = None
    created: datetime
    ordering: Optional[int] = None


class Project(BaseModel):
    id: str
    slug: str
    title: Optional[str] = None
    description: Optional[str] = None
    categories: Optional[List[str]] = None
    client_side: Optional[str] = None
    server_side: Optional[str] = None
    body: Optional[str] = None
    status: Optional[str] = None
    requested_status: Optional[str] = None
    additional_categories: Optional[List[str]] = None
    issues_url: Optional[str] = None
    source_url: Optional[str] = None
    wiki_url: Optional[str] = None
    discord_url: Optional[str] = None
    donation_urls: Optional[List[DonationUrl]] = None
    project_type: Optional[str] = None
    downloads: Optional[int] = None
    icon_url: Optional[str] = None
    color: Optional[int] = None
    thread_id: Optional[str] = None
    monetization_status: Optional[str] = None
    team: str
    body_url: Optional[str] = None
    published: datetime
    updated: datetime
    approved: Optional[datetime] = None
    queued: Optional[datetime] = None
    followers: int
    license: Optional[License] = None
    versions: Optional[List[str]] = None
    game_versions: Optional[List[str]] = None
    loaders: Optional[List[str]] = None
    gallery: Optional[List[GalleryItem]] = None


class Dependencies(BaseModel):
    version_id: Optional[str] = None
    project_id: Optional[str] = None
    file_name: Optional[str] = None
    dependency_type: str


class Hashes(BaseModel):
    sha512: str
    sha1: str


class File(BaseModel):
    hashes: Hashes
    url: str
    filename: str
    primary: bool
    size: int
    file_type: Optional[str] = None


class Version(BaseModel):
    id: str
    project_id: str
    slug: Optional[str] = None
    name: Optional[str] = None
    version_number: Optional[str] = None
    changelog: Optional[str] = None
    dependencies: Optional[List[Dependencies]] = None
    game_versions: Optional[List[str]] = None
    version_type: Optional[str] = None
    loaders: Optional[List[str]] = None
    featured: Optional[bool] = None
    status: Optional[str] = None
    requested_status: Optional[str] = None
    author_id: str
    date_published: datetime
    downloads: int
    changelog_url: Optional[str] = None  # Deprecated
    files: List[File]


class Hit(BaseModel):
    project_id: str
    author: str
    versions: List[str]
    follows: int
    date_created: datetime
    date_modified: datetime
    project_type: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    categories: Optional[List[str]] = None
    display_categories: Optional[List[str]]
    downloads: Optional[int] = None
    icon_url: Optional[str] = None
    latest_version: Optional[str] = None
    license: Optional[str] = None
    client_side: Optional[str] = None
    server_side: Optional[str] = None
    gallery: Optional[List[str]] = None
    featured_gallery: Optional[str] = None
    color: Optional[int] = None


class SearchResult(BaseModel):
    hits: List[Hit]
    offset: int
    limit: int
    total_hits: int
