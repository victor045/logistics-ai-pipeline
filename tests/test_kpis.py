
def test_kpis_output():
    import os
    import json

    path = os.path.join('data', 'kpis.json')
    assert os.path.exists(path), "kpis.json no existe"

    with open(path, 'r') as f:
        kpis = json.load(f)
    assert 'total_stops' in kpis
    assert 'total_distance_m' in kpis
    assert 'avg_distance_per_stop_m' in kpis
    assert kpis['total_stops'] > 0
    assert kpis['total_distance_m'] > 0

