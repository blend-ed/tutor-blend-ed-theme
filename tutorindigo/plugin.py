import pkg_resources

from tutor import hooks

from .__about__ import __version__


################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "WELCOME_MESSAGE": "Learning in more dimensions",
        "PRIMARY_COLOR": "#009cc7",  # cool blue
        # Footer links are dictionaries with a "title" and "url"
        # To remove all links, run:
        # tutor config save --set BLEND_ED_FOOTER_NAV_LINKS=[] --set BLEND_ED_FOOTER_LEGAL_LINKS=[]
        "FOOTER_NAV_LINKS": [
            {"title": "About", "url": "/about"},
            {"title": "Contact", "url": "/contact"},
        ],
        "FOOTER_LEGAL_LINKS": [
            {"title": "Terms of service", "url": "/tos"},
            {
                "title": "Blend-ed theme for Open edX",
                "url": "https://github.com/blend-ed/tutor-blend-ed-theme",
            },
        ],
    },
    "unique": {},
    "overrides": {},
}

# Theme templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutorblended", "templates")
)
# This is where the theme is rendered in the openedx build directory
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("blend-ed-theme", "build/openedx/themes"),
    ],
)

# Force the rendering of scss files, even though they are included in a "partials" directory
hooks.Filters.ENV_PATTERNS_INCLUDE.add_item(
    r"blend-ed-theme/lms/static/sass/partials/lms/theme/"
)

# Load all configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"BLEND_ED_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"BLEND_ED_{key}", value) for key, value in config["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))
