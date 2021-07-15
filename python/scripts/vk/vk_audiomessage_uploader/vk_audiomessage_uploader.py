# -*- coding: utf-8 -*-
"""
:author: homus32
:copyright: everyone can copy this code :D
:version: 1.2
"""

def enter(message=""):
    if message is not None:
        message = str(message)+"\n\n\n"
    input(message+"Press ENTER to exit...")
    exit()

try:
    import os
    import vk_api
    from threading import Thread
    from pydub import AudioSegment


    def question():
        services = str(
            "1. Как пользоваться этим скриптом?\n"+
            "2. Начать использование"
            )

        todo = input("Что вы хотите сделать?\n%s" % services+"\nНапишите цифру: ")
        print()

        try:
            return int(todo)
        except:
            if todo == '':
                enter()
            else:
                print("Вы указали не число. Попробуйте сново.\n\n")
                question()


    class UploadAudioMessages:

        def __init__(self,args,vk_session,id):
            ls = os.listdir(None)

            if self._cheack_audio(ls) is True:

                self.__task_messages = list()

                vk = vk_session.get_api()
                upload = vk_api.VkUpload(vk_session)
                tasks = list()

                if args[0] == "bot":
                    chats = args[2]
                else:
                    chats = args[3]

                for file in ls:
                    if file[-3:] == "mp3" or file[-3:] == "ogg":
                        task = Thread(name=file, target=self.__task, args=(file, chats, upload, vk, id),daemon=True)
                        tasks.append(task)
                        task.start()

                for task in tasks:
                    task.join()

                for m in self.__task_messages:
                    for i in m:
                        pass

        @staticmethod
        def _cheack_audio(ls):

            for file in ls:
                if file[-3:] == "ogg" or file[-3:] == "mp3":
                    break
            else:
                enter("В текущей директории не были найдены ogg и mp3 файлы... Abort...")
            return True

        def __task(self,file,chats,upload,vk,id):
            if file[-3:] != "ogg":
                file = self.reformat_to_ogg(file)
            self.__upload(file,chats,upload,vk,id)

        @staticmethod
        def reformat_to_ogg(file):
            print("Переделываем файл " + file + " в ogg..")
            new_filename = file[:-4] + '.ogg'
            AudioSegment.from_mp3(file).export(new_filename, format='ogg')
            print("Закончил обработку " + new_filename)
            os.remove(file)
            return new_filename

        def __upload(self,file,chats,upload,vk,id):
            with open(file, 'r') as f:
                print("Загрузка " + file + " на сервер ВК...")
                data = upload.audio_message(file[:-4] + ".ogg", group_id=id)["audio_message"]
                audio = "doc{}_{}".format(data['owner_id'], data['id'])
                self.__task_messages.append(self.__sender(vk,chats,audio,file))
            os.remove(file)

        @staticmethod
        def __sender(vk,chats,audio,filename):
            for chat in chats.replace(" ","").split(","):
                yield vk.messages.send(random_id=0, peer_id=chat, attachment=audio)
            print("Закончил отправку " + filename)



    def for_user(args):

        login, password, id = args[1], args[2], args[4]
        vk_session = vk_api.VkApi(login, password)

        try:
            print("Авторизация...")
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            enter(error_msg)

        UploadAudioMessages(args,vk_session,id)


    def for_bot(args):
        print("Авторизация через бота...\nP.S: Если токен неправильный, то скрипт крашнется во время исполнения")
        token = vk_api.VkApi(token=args[1],api_version="5.101")
        UploadAudioMessages(args,token,args[3])



    def start():

        todo = question()

        if todo == 1:
            print(
                "===Подготовка===\n"
                "1. Создайте файл login.txt\n"
                "2. В первую строчку введите тип авторизации (через свой акк - пишите user. через бота - пишите bot)\n"
                "3. Во вторую строчку введите свой логин или токен группы\n"
                "4. В третью строчку напишите пароль от акккаунта.\nЕсли вы используете авторизацию через "
                "токен сообщества то ничего не пишите в третью строчку (информация никуда не отправляется!)\n"
                "5. Если используете user, то в 4 строчке напишите куда отправлять (чаты указывать через запятую).\n"
                "Если используете bot то, в 3 строке.\n"
                "6. После строчки 'куда отправлять' пишем вашу ид группы или ид аккаунта.\n\n"
                "===ПРИМЕР ДЛЯ АККАУНТА===\n"
                "user - тип авторизации\n"
                "88005553535 - логин\n"
                "tipaparol2281337 - пароль\n"
                "-182868435 - куда отправлять голосовухи\n"
                "360089815 - ид вашего акка\n\n"
                "===ПРИМЕР ДЛЯ БОТА===\n"
                "bot - тип авторизации\n"
                "edn09gnmd3dadcd9376288214ed3063c347a19abbdbbdb3dvc8b8d819255f48c81ctldxza4tgnmk5tff3 - токен бота\n"
                "360089815 - куда отправлять голосовухи\n"
                "182868435 - ид бота(группы, без минуса)\n\n"
            )
            print(
                "===Начало===\n"
                "1. Закинте в папку там где скрипт mp3 музыку (ВНИМАНИЕ!!! после завершения скрипта mp3 удалятся)\n"
                "2. Подождите пока загрузится.\n"
                "3. Готово.\n\n\n"
            )

            start()

        elif todo == 2:
            with open("login.txt","r") as f:
                words = [line.replace("\n","") for line in f]
                if words[0] == "user":
                    for_user(words)
                elif words[0] == "bot":
                    for_bot(words)
                else:
                    raise Exception("Неправильный тип авторизации")

            enter("Усе")

    if __name__ == "__main__":
        start()

except Exception as error:
    enter("Error: "+str(error))
