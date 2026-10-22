def test_importing_api():
    from differ_pld4energy_dashboard.apis import api_entry_point

    assert api_entry_point.prefix == 'newapi'
    assert api_entry_point.name == 'NewAPI'
