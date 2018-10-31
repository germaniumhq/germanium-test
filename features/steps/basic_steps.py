from behave import step, use_step_matcher
from germanium.static import open_browser, go_to, get_germanium

# we tell behave to allow us using regex params
use_step_matcher("re")


@step("I open '(.*?)'")
def i_open_a_page(context, url):
    open_browser("chrome")
    go_to(url)


@step("I check the page title")
def check_page_title(context):
    context.title = get_germanium().title


@step("the page title contains '(.+?)'")
def check_contains(context, contained_text):
    assert contained_text in context.title

