

from time import sleep

class User:

    def __init__(self, name, password, age):
        self.nickname = name
        self.password = hash(str(password))
        self.age = int(age)

    def __repr__(self):
        return self.nickname

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def  log_in(self, nickname, password):
        log_in_user = self.users.get(str(nickname))
        if log_in_user is not None:
            self.current_user = log_in_user

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        if self.users.get(str(nickname)) is not None:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.current_user = User(nickname, password, age)
            self.users.update({nickname : self.current_user})

    def add(self, *videos):
        for video in videos:
            if self.videos.get(video.title) is None:
                self.videos.update({video.title : video})

    def get_videos(self, video_keyword):
        list_videos = []
        for key in self.videos:
            if len(video_keyword) > 2 and key.lower().find(video_keyword.lower()) != -1:
                list_videos.append(key)
        return list_videos

    def watch_video(self, video_name):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            video = self.videos.get(video_name)
            if video is not None:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for second in range(1, video.duration+1):
                        print(second, sep=' ', end=" ")
                        sleep(1)
                    print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')