from germanium.static import close_browser


def after_scenario(context, scenario):
    close_browser()
