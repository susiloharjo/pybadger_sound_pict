from adafruit_pybadger import PyBadger

pybadger = PyBadger()

pybadger.show_badge(name_string="susiloharjo", hello_scale=2, my_name_is_scale=2, name_scale=2)
# pybadger.pixels(10)

while True:
    pybadger.auto_dim_display(delay=5, movement_threshold=3) # Remove or comment out this line if you have the PyBadge LC
    if pybadger.button.a:
        pybadger.show_business_card(image_name="me.bmp")
        pybadger.play_file("starwars.wav")
    elif pybadger.button.b:
        pybadger.show_qr_code(data="https://kakeko.wordpress.com")
    elif pybadger.button.start:
        pybadger.show_badge(name_string="susiloharjo", hello_scale=2, my_name_is_scale=2, name_scale=2)
    elif pybadger.button.select:
        pybadger.play_file("starwars.wav")
        