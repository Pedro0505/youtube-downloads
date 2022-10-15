from pytube import YouTube
from services.ValidateInfos import ValidateInfos
from services.YouTubeDownload import YouTubeDownload


class Program:
    def __init__(self, validator, youtube):
        self.validator = validator
        self.youtube = youtube

    def start(self):
        url = input('Digite a url: ')

        try:
            self.validator.validateUrl(url)
            extension = input('Qual o formato desejado? (mp3/mp4) ')
            self.validator.validateExtension(extension)
            path = input(
                'Pasta de destino do download (deixe branco para pasta atual) '
                )
        except ValueError:
            print('Ops está não é uma url válida!')
            return
        except FileNotFoundError:
            print('Está não é uma extensão suportada!')
            return

        if extension == 'mp3':
            print('Baixando...')
            self.youtube.only_song(url, path)
        else:
            res_options = '(144p/240p/360p/480p/720p/1080p) '
            try:
                resolution = input('Qual a resolução do vídeo? ' + res_options)
                self.validator.validateRes(resolution)
            except ValueError:
                print('Tipo de resolução não esperada')
                return

            print('Baixando...')
            self.youtube.video(url, resolution, path)


if __name__ == '__main__':
    program = Program(ValidateInfos, YouTubeDownload(YouTube))
    program.start()
