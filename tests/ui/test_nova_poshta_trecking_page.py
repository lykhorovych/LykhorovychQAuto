import pytest

@pytest.mark.nova_poshta 
def test_open_tracking_page(nova_poshta_page):
    nova_poshta_page.check_title()

@pytest.mark.nova_poshta
def test_typing_and_erasing_number_of_parcel_in_search_field(nova_poshta_page):
    search_field = nova_poshta_page.type_number_of_invoice_into_search_field('20450453124981')
    typed_value = nova_poshta_page.get_elem_attribute(search_field, "value")

    assert typed_value == '20450453124981'

    nova_poshta_page.click_on_clear_sign_into_search_field()
    value = nova_poshta_page.get_elem_attribute(search_field, "value")

    assert value == ""

@pytest.mark.nova_poshta
def test_unable_search_with_an_empty_input_field(nova_poshta_page):
    search_field = nova_poshta_page.type_number_of_invoice_into_search_field('')
    empty_field = nova_poshta_page.get_elem_attribute(search_field, "value")
    assert empty_field == ''

    disabled, background_color = nova_poshta_page.get_search_button_properties()
    assert disabled == 'true'
    assert background_color == 'rgba(251, 251, 251, 1)'

@pytest.mark.nova_poshta
def test_able_searching_with_correct_value_in_input_field(nova_poshta_page):
    search_elem = nova_poshta_page.type_number_of_invoice_into_search_field('20450453124981')
    typed_value = nova_poshta_page.get_elem_attribute(search_elem, "value")
    assert typed_value == '20450453124981'

    disabled, background_color = nova_poshta_page.get_search_button_properties()
    assert disabled == None
    assert background_color == 'rgba(143, 226, 176, 1)'

@pytest.mark.nova_poshta
def test_redirection_to_nova_global_after_input_international_parcel(nova_poshta_page):
    nova_poshta_page.type_number_of_invoice_into_search_field('AENM0002497278NPI')

    assert nova_poshta_page.driver.current_url == "https://novaposhtaglobal.ua/track/?Tracking_ID=AENM0002497278NPI"
    assert nova_poshta_page.driver.title == "Трекінг посилки | Nova Global"


