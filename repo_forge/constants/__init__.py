"""
Constants for Eidosian Repo Forge.

This package contains constants and templates used throughout the repository
generator system, ensuring consistency across all generated components.
"""

from .content import (
    README_TEMPLATE,
    GITIGNORE_CONTENT,
    EDITORCONFIG_CONTENT,
    EIDOSIAN_CONFIG_TEMPLATE,
    CI_CONFIG_TEMPLATE,
    CONTRIBUTING_TEMPLATE,
    CODE_OF_CONDUCT_CONTENT,
    LICENSE_TEMPLATE, 
    SECURITY_TEMPLATE,
    CHANGELOG_TEMPLATE,
    PROJECT_READMES,
    PROJECT_CONFIG_FILES,
    PROJECT_MAIN_FILES
)

from .paths import (
    CORE_DIRECTORIES,
    LANGUAGE_DIRECTORIES,
    SCRIPT_DIRECTORIES,
    TEST_DIRECTORIES,
    BENCHMARK_DIRECTORIES,
    EXAMPLE_DIRECTORIES,
    CI_DIRECTORIES,
    GITHUB_DIRECTORIES,
    DOCUMENTATION_STRUCTURE,
    MANUAL_DOC_STRUCTURE,
    AUTO_DOC_STRUCTURE,
    ASSETS_STRUCTURE,
    SHARED_DIRECTORIES,
    CONFIG_DIRECTORIES,
    TOOL_DIRECTORIES
)

__all__ = [
    # Content constants
    "README_TEMPLATE",
    "GITIGNORE_CONTENT",
    "EDITORCONFIG_CONTENT",
    "EIDOSIAN_CONFIG_TEMPLATE",
    "CI_CONFIG_TEMPLATE",
    "CONTRIBUTING_TEMPLATE",
    "CODE_OF_CONDUCT_CONTENT",
    "LICENSE_TEMPLATE",
    "SECURITY_TEMPLATE",
    "CHANGELOG_TEMPLATE",
    "PROJECT_READMES",
    "PROJECT_CONFIG_FILES",
    "PROJECT_MAIN_FILES",
    
    # Path constants
    "CORE_DIRECTORIES",
    "LANGUAGE_DIRECTORIES",
    "SCRIPT_DIRECTORIES",
    "TEST_DIRECTORIES",
    "BENCHMARK_DIRECTORIES",
    "EXAMPLE_DIRECTORIES",
    "CI_DIRECTORIES",
    "GITHUB_DIRECTORIES",
    "DOCUMENTATION_STRUCTURE",
    "MANUAL_DOC_STRUCTURE",
    "AUTO_DOC_STRUCTURE",
    "ASSETS_STRUCTURE",
    "SHARED_DIRECTORIES", 
    "CONFIG_DIRECTORIES",
    "TOOL_DIRECTORIES"
]
