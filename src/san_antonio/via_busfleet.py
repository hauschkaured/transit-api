class Models:
    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return f"{self.model}"
models = {}
model_list = ["Gillig Low Floor EV 40", "2010 New Flyer DE40LFR", 
              "2010 New Flyer DE40LFR", "2016 New Flyer XN40",
              "2016-2017 Novabus LFS CNG 40", "2018 Novabus LFS CNG 40",
              "2020 Novabus LFS CNG 40", "2022 Gillig Low Floor CNG 40"]

for i in range(8):
    j = i + 118
    vehicle = Models("2022 Gillig Low Floor EV 40")
    models[j] = vehicle

for i in range(30):
    j = i + 376
    vehicle = Models("2010 New Flyer DE40LFR")
    models[j] = vehicle

for i in range(15):
    j = i + 406
    vehicle = Models("2016 New Flyer XN40")
    models[j] = vehicle

for i in range(271):
    j = i + 421
    vehicle = Models("2016-2017 Novabus LFS CNG 40")
    models[j] = vehicle

for i in range(44):
    j = i + 692
    vehicle = Models("2018 Novabus LFS CNG 40")
    models[j] = vehicle

for i in range(22):
    j = i + 736
    vehicle = Models("2020 Novabus LFS CNG 40")
    models[j] = vehicle

for i in range(28):
    j = i + 758
    vehicle = Models("2022 Gillig Low Floor CNG 40")
    models[j] = vehicle


for i in range(6):
    j = i + 800
    vehicle = Models("2020 Novabus LFS CNG 40 LFX")
    models[j] = vehicle
