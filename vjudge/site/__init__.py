from .hdu import *
from .scu import *
from . import exceptions

__all__ = hdu.__all__ + scu.__all__

supported_sites = ('scu', 'hdu')
supported_contest_sites = ('hdu',)

normal_clients = {'scu': SOJClient, 'hdu': HDUClient}
contest_clients = {'hdu': HDUContestClient}


def get_normal_client(site, auth=None):
    if site not in supported_sites:
        raise exceptions.JudgeException(f'Site "{site}" is not supported')
    return normal_clients[site](auth)


def get_contest_client(site, auth=None, contest_id=None):
    if site not in supported_contest_sites:
        raise exceptions.JudgeException(f'Site "{site}" is not supported')
    return contest_clients[site](auth, contest_id)
