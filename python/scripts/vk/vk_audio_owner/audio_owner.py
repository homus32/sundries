import os
import requests
from eyed3 import id3
from abc import abstractmethod, ABC

# Сюда писать исключение для музыки, чтобы не скачивалась
exeption_list = {}


# Для редактирования метаданных
def load_mp3(path):
    tag = id3.Tag()
    tag.parse(path)
    return tag


# Функция для проверки исключения.
def is_exception(obj):
    for key in exeption_list:
        if key.lower() in obj.author.lower():
            if exeption_list[key] is True:
                return True
            else:
                for i in exeption_list[key]:
                    if i.lower() in obj.name.lower():
                        return True
    return False


# Коректировка названии, чтобы винда не рулагась.
def fix_name(string):
    big_str = string.replace("/", "+").replace("\\", "+").replace(":", ";")
    big_str = big_str.replace("*", "✶").replace("?", "Q").replace("\"", "'")
    return big_str.replace("<", "(").replace(">", ")").replace("|", "+")


# Абстрактный класс который нельзя создать, потому что этот класс может использоваться лишь в
# дочерних классах
class Get(ABC):

    @abstractmethod
    def __init__(self):
        pass

    # Получить музыку по позиции (алгоритмы поиска музыки не знаю)
    def get_by_index(self, index):
        for item in self:
            if str(index).lower() == str(item.index).lower():
                return item
        return None

    # Получить музыку по имени
    def get_by_name(self, name):
        name_list = list()

        for item in self:
            if name.lower() in item.name.lower():
                name_list.append(item)

        if name_list.__len__ != 0:
            return name_list
        else:
            return None

    # По автору
    def get_by_author(self, author):
        author_list = list()

        for item in self:

            if author.lower() in item.author.lower():
                author_list.append(item)

        if author_list.__len__ != 0:
            return author_list
        else:
            return None
        
    # Полное имя
    def get_by_full_name(self, author, name):
        for item in self:
            if author.lower() in item.author.lower() and name.lower() in item.name.lower():
                return item
        return None

    def __contains__(self, item):

        for i in self:
            if item.full_name.lower() in i.full_name.lower():
                return True
        return False

    def __iter__(self):
        for item in self.obj_list:
            yield item


class File(Get):

    def __init__(self, path):
        self.path = path
        File.path = path

        self.file_list = list(filter(lambda x: ".mp3" in x, os.listdir(self.path)))
        self.obj_list = list()

        for i in self.file_list:
            file = load_mp3(self.path + i)

            data = {
                "index": file.track_num[0],
                "author": file.artist,
                "name": file.title,
                "file_name": i,
                "path": self.path
            }

            self.obj_list.append(file_obj(data))
            
    # Скачать трек
    def download(self, audio_obj):
        file_name = fix_name("{}. {}.mp3".format(audio_obj.index, audio_obj.full_name))

        with open(self.path + file_name, "wb") as f:
            f.write(requests.get(audio_obj.url).content)

            file = load_mp3(self.path + file_name)
            file.title = audio_obj.name
            file.artist = audio_obj.author
            file.track_num = audio_obj.index

            data = {
                "index": audio_obj.index,
                "author": audio_obj.author,
                "name": audio_obj.name,
                "file_name": file_name,
                "path": self.path
            }

            file.save(version=id3.ID3_DEFAULT_VERSION, encoding='utf-8')

            return file_obj(data)


class file_obj:

    def __init__(self, audio):
        self._index = audio["index"]
        self._author = audio["author"]
        self._name = audio["name"]
        self.path = audio["path"]
        self.full_name = "{} - {}".format(self.author, self.name)
        self.file_name = audio["file_name"]

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self.file.track_num = str(value)
        self._index = str(value)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self.file.artist = value
        self._author = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.file.title = value
        self._name = value

    def start_edit(self):
        self.file = load_mp3(self.path + self.file_name)
        return self.file

    def end_edit(self):
        self.file.save(version=id3.ID3_DEFAULT_VERSION, encoding='utf-8')
        del self.file

    def __enter__(self):
        self.start_edit()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.end_edit()
        except:
            pass

    def delete(self):
        os.remove(self.path + self.file_name)

    def rename(self, name):
        os.rename(self.path + self.file_name, name)
        self.file_name = name


class Audio(Get):

    def __init__(self, media):
        self.audio_list = media
        self.obj_list = list()

        for i in range(len(self.audio_list)):
            self.audio_list[i]["index"] = str(i + 1)

        for a_obj in self.audio_list:
            self.obj_list.append(audio_obj(a_obj))


class audio_obj:

    def __init__(self, media):
        self.url = media.get("url")
        self.index = media["index"]
        self.author = media["artist"]
        self.name = media["title"]
        self.full_name = "{} - {}".format(self.author, self.name)

# Мне лень комментировать, все равно это никому не нужно :(
