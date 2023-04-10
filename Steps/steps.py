from behave import given, then, when, fixture


@fixture(u'Logo is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Logo is displayed')
    page = HomePage(context.driver)
    assert page.get_logo()


@given(u'Go to Form Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Go to Form Page')


@when(u'I enter first name "Ana"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Ana"')


@when(u'I enter first name "Banana"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Banana"')


@when(u'click submit')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click submit')


@then(u'A success message should be displayed.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A success message should be displayed.')


@when(u'I enter first name "Ileana"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Ileana"')


@when(u'I enter first name "Cosanzeana"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Cosanzeana"')


@when(u'I enter first name "Ion"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Ion"')


@when(u'I enter first name "Creanga"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Creanga"')


@then(u'The Form Page should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The Form Page should be displayed')


@when(u'go to home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When go to home page')


@then(u'the home page should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the home page should be displayed')


@when(u'logo is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: When logo is displayed')


@then(u'I should see "{keyword}"')
def step_impl(context, keyword):
    raise NotImplementedError(u'STEP: Then I should see "Welcome to Formy"')
    assert keyword in context.driver.page