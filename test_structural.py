import pytest
import example
import math


#Coverage 100%

@pytest.mark.parametrize("city, expected_coordinates", [
    ("Lima,Peru", (-12.0621065, -77.0365256)),
    ("Buenos Aires,Argentina", (-34.6037181, -58.38153)),
    ("Santiago,Chile", (-33.4377968, -70.6504451)),
    ("Quito,Ecuador", (-0.2201641, -78.5123274)),
    ("Caracas,Venezuela", (10.506098, -66.9146017)),
    ("La Paz,Bolivia", (-16.500097, -68.146946)),
    ("Montevideo,Uruguay", (-34.9011127, -56.1645314)),
    ("Asuncion,Paraguay", (-25.2637399, -57.575926)),
    ("Tokyo,Japan", (35.6828387, 139.7594549)),
    ("New York,USA", (40.7127281, -74.0060152))
])
def test_get_coordinates(city, expected_coordinates):
    detected_coordinates = example.get_coordinates(city)
    assert detected_coordinates is not None, f"No coordinates detected for {city}"
    assert math.isclose(detected_coordinates[0], expected_coordinates[0], rel_tol=1e-1), f"The latitude for {city} is not correct, Detected: {detected_coordinates[0]}, Expected: {expected_coordinates[0]}"
    assert math.isclose(detected_coordinates[1], expected_coordinates[1], rel_tol=1e-1), f"The longitude for {city} is not correct, Detected: {detected_coordinates[1]}, Expected: {expected_coordinates[1]}"

def test_non_existing_endpoint_raises_exception():
    with pytest.raises(Exception):
        example.something_not_existent("blah blah")
