class BaseConfig(object):
    USERNAME = '1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix'
    PASSWORD = 'a3eb3e22cddda14a068eef718f2921048e550f059a6c6e3230e42c51c08a5249'
    URL = 'https://1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix:a3eb3e22cddda14a068eef718f2921048e550f059a6c6e3230e42c51c08a5249@1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix.cloudantnosqldb.appdomain.cloud'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
