import re


class ValidateInfos:
    url_regex = re.compile(
        r"(?:http(?:s)?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com"
        r"\/(?:(?:watch)?\?(?:.*&)?v(?:i)?=|"
        r"(?:embed|v|vi|user)\/))([^\?&\"'<> #]+)"
    )

    @staticmethod
    def validateUrl(url):
        check_url = re.match(ValidateInfos.url_regex, url)

        if not check_url:
            raise ValueError('Invalid Url')

    @staticmethod
    def validateExtension(extension):
        if extension != 'mp4' and extension != 'mp3':
            raise FileNotFoundError('Unexpected file extension')

    @staticmethod
    def validateRes(res):
        res_options = ['144p', '240p', '360p', '480p', '720p', '1080p']

        if not (res) in res_options:
            raise ValueError('Invalid resolution')
