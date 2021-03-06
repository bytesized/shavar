__version__ = '0.7.0'


def includeme(config):
    "Load shavar WSGI app into the provided Pyramid configurator"
    # Dependencies first
    config.include("mozsvc")
    config.include('pyramid_mako')
    # Have to get the lists loaded before the views
    config.include("shavar.lists")
    config.include("shavar.views")


def get_configurator(global_config, **settings):
    import mozsvc.config
    config = mozsvc.config.get_configurator(global_config, **settings)
    config.begin()
    try:
        config.include(includeme)
    finally:
        config.end()
    return config


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = get_configurator(global_config, **settings)
    return config.make_wsgi_app()
