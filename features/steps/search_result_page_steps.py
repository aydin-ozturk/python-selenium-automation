from behave import given, when, then


@when('Click on the first product')
def select_first_product(context):
    context.app.search_results_page.select_first_product()


@then('Search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)


@then('Verify every product has a name and image')
def verify_product_name_img(context):
    context.app.search_results_page.verify_product_name_img()


@then("Verify {department} department is selected")
def verify_department(context, department):
    context.app.search_results_page.verify_department(department)