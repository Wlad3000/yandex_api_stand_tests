# Владислав Рогожкин, 7я когорта, Venus — Финальный проект. Инженер по тестированию плюс.

def create_order():
    current_body = data.order_content.copy()
    current_body ["firstName"] = "Jan"
    track_num = sender_test.post_new_order(current_body)
    return str(track_num.json()["track"])
def positive_assert():
    track_num = create_order()
    current_params = data.params_get.copy()
    current_params["t"] = track_num
    response = sender_test.get_order(current_params)
    assert response.status_code == 200

def test_order():
    positive_assert()