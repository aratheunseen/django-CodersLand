# config.py

# Site Information
SITE_NAME = "CodersLand"
SITE_URL = "codersland.xyz"

# meta tags
META_TITLE = "CodersLand"
META_DESCRIPTION = "CodersLand is a platform where we are showcasing all coders portfolio. You can find your portfolio by just typing your GitHub username."
META_KEYWORDS = "coders portfolio, codersland, github users portfolio"

# GitHub API Details
GITHUB_PAT = "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"
GITHUB_API_URL = "https://api.github.com"
GITHUB_API_HEADERS = {
    'Authorization': f'Token {GITHUB_PAT}',
    'Accept': 'application/json'
}
