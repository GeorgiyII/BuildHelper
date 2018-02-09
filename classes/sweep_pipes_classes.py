from math import sqrt, cos, tan


class SweepCylinder:

    # Расчет координат для построения развертки врезки труб в листовой материалл

    def __init__(self, d, t, beta):
        self.t = float(t)
        self.beta = float(beta) * 0.0174533

        if float(beta) <= 45:
            self.d = float(d) - self.t
        else:
            self.d = float(d)

        self.h = (self.d / tan(self.beta)) / 2

        # Разбивка на количество промежутков в зависимости от диаметра трубы

        if float(d) < 250:
            self.n = 8
        elif 250 <= float(d) < 350:
            self.n = 12
        elif 350 <= float(d) < 500:
            self.n = 16
        elif 500 <= float(d) < 750:
            self.n = 24
        elif 750 <= float(d) < 1000:
            self.n = 32
        elif 1000 <= float(d) < 1500:
            self.n = 48
        elif 1500 <= float(d) < 2000:
            self.n = 64
        elif float(d) > 2000:
            self.n = 96

    def cylinder(self):

        # Список коэфициентов для умножения

        list_koef1 = [0, 0.004815, 0.019215, 0.043060, 0.076120, 0.118079, 0.168530, 0.226990, 0.292893, 0.365607,
                      0.444430, 0.528603, 0.617317, 0.709715, 0.804910, 0.901983, 1, 1.098017, 1.195090, 1.290285,
                      1.382683, 1.471397, 1.555570, 1.634393, 1.707107, 1.773010, 1.831470, 1.881921, 1.923880,
                      1.956940, 1.980785, 1.995185, 2]

        list_koef2 = [0, 0.002141, 0.008555, 0.019215, 0.034074, 0.053070, 0.076120, 0.103127, 0.133975, 0.168530,
                      0.206647, 0.248160, 0.292893, 0.340654, 0.391239, 0.444430, 0.5, 0.557711, 0.617317, 0.678561,
                      0.741181, 0.804910, 0.869474, 0.934597, 1, 1.065403, 1.130526, 1.195090, 1.258819, 1.321439,
                      1.382683, 1.442289, 1.5, 1.555570, 1.608761, 1.659346, 1.707107, 1.751840, 1.793353, 1.831470,
                      1.866025, 1.896873, 1.923880, 1.946930, 1.965926, 1.980785, 1.991445, 1.997859, 2]

        # Список в который будут записаны координаты для построения развертки трубы

        list_cylinder = []

        # Список индексов, которые зависят от того на сколько частей разбивается труба

        if self.n == 8:
            list_index = [0, 8, 16, 24, 32, 24, 16, 8, 0]

        elif self.n == 16:
            list_index = [0, 4, 8, 12, 16, 20, 24, 28, 32, 28, 24, 20, 16, 12, 8, 4, 0]

        elif self.n == 32:
            list_index = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 30, 28, 26, 24, 22, 20, 18,
                          16, 14, 12, 10, 8, 6, 4, 2, 0]

        elif self.n == 64:
            list_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                          26, 27, 28, 29, 30, 31, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16,
                          15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        elif self.n == 12:
            list_index = [0, 8, 16, 24, 32, 40, 48, 40, 32, 24, 16, 8, 0]

        elif self.n == 24:
            list_index = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0]

        elif self.n == 48:
            list_index = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48,
                          46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]

        else:
            list_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                          26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
                          47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25,
                          24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        # Заполнение списка координат

        for i in list_index:
            if self.n == 8 or self.n == 16 or self.n == 32 or self.n == 64:
                x = round(list_koef1[i] * self.h, 4)
                list_cylinder.append(x)
            else:
                x = round(list_koef2[i] * self.h, 4)
                list_cylinder.append(x)

        # Создание списка с индексом и значением

        list_result = []

        for index, value in enumerate(list_cylinder):
            a = (index, value)
            print(self.d)
            list_result.append(a)

        return list_result


class SweepPipes:

    # Расчет развертки для труб врезающихся в трубу

    def __init__(self, d, t, diam=0, beta=0):
        self.d = float(d)
        self.D = float(diam)
        self.t = float(t)
        self.beta = float(beta) * 0.0174533
        self.h = float(h) / 2

        # Разбивка на количество промежутков в зависимости от диаметра трубы

        if float(d) < 500:
            self.n = 16
        elif 500 <= float(d) < 750:
            self.n = 24
        elif 750 <= float(d) < 1000:
            self.n = 32
        elif 1000 <= float(d) < 1500:
            self.n = 48
        elif 1500 <= float(d) < 2000:
            self.n = 64
        elif float(d) > 2000:
            self.n = 96

    def pipe_90(self):

        d = self.d - 2 * self.t

        # Список коэфициентов для умножения

        list_koef1 = [0, 0.009607, 0.038060, 0.084265, 0.146446, 0.222215, 0.308658, 0.402454, 0.5, 0.597544, 0.691342,
                      0.777785, 0.853554, 0.915734, 0.961939, 0.990393, 1, 0.990393, 0.961939, 0.915734, 0.853554,
                      0.777785, 0.691342, 0.597544, 0.5, 0.402454, 0.308658, 0.222215, 0.146446, 0.084265, 0.038060,
                      0.009607, 0]

        list_koef2 = [0, 0.004278, 0.017037, 0.038060, 0.066987, 0.103323, 0.146446, 0.195620, 0.25, 0.308658,
                      0.370590, 0.434737, 0.5, 0.565263, 0.629405, 0.691342, 0.749999, 0.804381, 0.853554, 0.896676,
                      0.933013, 0.961939, 0.982963, 0.995723, 1, 0.995723, 0.982963, 0.961939, 0.933013, 0.896676,
                      0.853554, 0.804381, 0.749999, 0.691342, 0.629405, 0.565263, 0.5, 0.434737, 0.370590,
                      0.308658, 0.25, 0.195620, 0.146446, 0.103323, 0.066987, 0.038060, 0.017037, 0.004278, 0]

        # Список в который будут записаны координаты для построения развертки трубы

        list_pipe90 = []

        # Список индексов, которые зависят от того на сколько частей разбивается труба

        if self.n == 8:
            list_index = [0, 8, 16, 24, 32, 24, 16, 8, 0]

        elif self.n == 16:
            list_index = [0, 4, 8, 12, 16, 20, 24, 28, 32, 28, 24, 20, 16, 12, 8, 4, 0]

        elif self.n == 32:
            list_index = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 30, 28, 26, 24, 22, 20, 18,
                          16, 14, 12, 10, 8, 6, 4, 2, 0]

        elif self.n == 64:
            list_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                          26, 27, 28, 29, 30, 31, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16,
                          15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        elif self.n == 12:
            list_index = [0, 8, 16, 24, 32, 40, 48, 40, 32, 24, 16, 8, 0]

        elif self.n == 24:
            list_index = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0]

        elif self.n == 48:
            list_index = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48,
                          46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]

        else:
            list_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                          26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
                          47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25,
                          24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        # Заполнение списка координат

        for i in list_index:
            if self.n == 8 or self.n == 16 or self.n == 32 or self.n == 64:
                x = round((d / 2) * (self.D / d - sqrt((self.D / d) ** 2 - list_koef1[i])), 4)
                list_pipe90.append(x)
            else:
                x = round((d / 2) * (self.D / d - sqrt((self.D / d) ** 2 - list_koef2[i])), 4)
                list_pipe90.append(x)

        # Создание списка с индексом и значением

        list_result = []

        for index, value in enumerate(list_pipe90):
            a = (index, value)
            list_result.append(a)

        return list_result

    def pipe_beta(self):

        d = self.d - self.t

        # Список коэфициентов для умножения

        list_koef1 = [0, 0.009607, 0.038060, 0.084265, 0.146446, 0.222215, 0.308658, 0.402454, 0.5, 0.597544, 0.691342,
                      0.777785, 0.853554, 0.915734, 0.961939, 0.990393, 1, 0.990393, 0.961939, 0.915734, 0.853554,
                      0.777785, 0.691342, 0.597544, 0.5, 0.402454, 0.308658, 0.222215, 0.146446, 0.084265, 0.038060,
                      0.009607, 0]

        list_koef2 = [0, 0.004278, 0.017037, 0.038060, 0.066987, 0.103323, 0.146446, 0.195620, 0.25, 0.308658,
                      0.370590, 0.434737, 0.5, 0.565263, 0.629405, 0.691342, 0.749999, 0.804381, 0.853554, 0.896676,
                      0.933013, 0.961939, 0.982963, 0.995723, 1, 0.995723, 0.982963, 0.961939, 0.933013, 0.896676,
                      0.853554, 0.804381, 0.749999, 0.691342, 0.629405, 0.565263, 0.5, 0.434737, 0.370590,
                      0.308658, 0.25, 0.195620, 0.146446, 0.103323, 0.066987, 0.038060, 0.017037, 0.004278, 0]

        # Список в который будут записаны координаты для построения развертки трубы

        list_pipe = []

        # Список индексов, которые зависят от того на сколько частей разбивается труба

        if self.n == 8:
            list_index = [0, 8, 16, 24, 32, 24, 16, 8, 0]

        elif self.n == 16:
            list_index = [0, 4, 8, 12, 16, 20, 24, 28, 32, 28, 24, 20, 16, 12, 8, 4, 0]

        elif self.n == 32:
            list_index = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 30, 28, 26, 24, 22, 20, 18,
                          16, 14, 12, 10, 8, 6, 4, 2, 0]

        elif self.n == 64:
            list_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                          26, 27, 28, 29, 30, 31, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16,
                          15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        elif self.n == 12:
            list_index = [0, 8, 16, 24, 32, 40, 48, 40, 32, 24, 16, 8, 0]

        elif self.n == 24:
            list_index = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0]

        elif self.n == 48:
            list_index = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48,
                          46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]

        else:
            list_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                          26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
                          47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25,
                          24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        # Заполнение списка координат

        for i in list_index:
            if self.n == 8 or self.n == 16 or self.n == 32 or self.n == 64:
                if i < 16:
                    x = round((1 / cos(self.beta)) * (d / 2) * (self.D / d - sqrt((self.D / d) ** 2 -
                        list_koef1[i])) + (d / 2) * tan(self.beta) * (1 - sqrt(1 - list_koef1[i])), 4)
                    list_pipe.append(x)
                else:
                    x = round((1 / cos(self.beta)) * (d / 2) * (self.D / d - sqrt((self.D / d) ** 2 -
                        list_koef1[i])) + (d / 2) * tan(self.beta) * (1 + sqrt(1 - list_koef1[i])), 4)
                    list_pipe.append(x)
            else:
                if i < 24:
                    x = round((1 / cos(self.beta)) * (d / 2) * (self.D / d - sqrt((self.D / d) ** 2 -
                        list_koef2[i])) + (d / 2) * tan(self.beta) * (1 - sqrt(1 - list_koef2[i])), 4)
                    list_pipe.append(x)
                else:
                    x = round((1 / cos(self.beta)) * (d / 2) * (self.D / d - sqrt((self.D / d) ** 2 -
                        list_koef2[i])) + (d / 2) * tan(self.beta) * (1 + sqrt(1 - list_koef2[i])), 4)
                    list_pipe.append(x)

        # Создание списка с индексом и значением

        list_result = []

        for index, value in enumerate(list_pipe):
            a = (index, value)
            list_result.append(a)

        return list_result
