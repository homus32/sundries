# Простой небольшой модуль для удобного управления музыки из вк

Пример использования:

```python
import vk_api
import audio_owner as aud
from vk_api import audio


login, password, my_id = '88005553535', '1123', '1'

path = "/media/homus/Вечная Память/Музыка/vkMusic/"

mode = 1

aud.exeption_list = {
    "Вардан": True,
    "голосование": True
}

delay = 1.5
audio_per_delay = 10

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()
vk_audio = audio.VkAudio(vk_session)

audio_count = vk.users.get(user_ids=my_id,fields="counters")[0].get("counters").get("audios")
seconds = (audio_count/audio_per_delay)*delay
print("Примерное время ожидания получения списка аудиозаписей - {} минут {} секунд".format(round(seconds/60),round(seconds%60),2))


print("Получаем список аудио.")
music_list = vk_audio.get(owner_id=my_id)

files = aud.File(path)
audios = aud.Audio(music_list)

for audio in audios:

    if mode == 1 or 3:

        if audio not in files:

            if aud.is_exception(audio): print("Это исключение"+audio.full_name); continue

            print("Скачивание " + audio.full_name)
            files.download(audio)
            print("Закончил скачивание " + audio.full_name + "\n\n\n\n\n")

    elif mode == 2:

        if audio not in files:

            if aud.is_exception(audio): print("Это исключение"+audio.full_name); continue

            print("Скачивание " + audio.full_name)
            files.download(audio)
            print("Закончил скачивание " + audio.full_name + "\n\n\n\n\n")

        else:
            break

if mode == 3:

    for file in files:

        if file in audios:
            continue

        else:
            print("Удаление "+file.file_name)
            file.delete()
```
