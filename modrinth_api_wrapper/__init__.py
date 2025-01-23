"""
modrinth_api_wrapper init file.    
"""

# Define some metadata here:

__version__ = '1.0.0'
__author__ = 'z0z0r4'

from modrinth_api_wrapper.client import Client, Tag, SearchIndex, Algorithm
from modrinth_api_wrapper.models import Project, Version, SearchResult

__all__ = [
    'Client',
    'Tag',
    'SearchIndex',
    'Algorithm',
    'Project',
    'Version',
    'SearchResult',
]