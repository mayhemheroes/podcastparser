#!/usr/bin/python3
import atheris
import sys
from urllib.error import URLError

with atheris.instrument_imports():
    from podcastparser import parse

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    str_1 = fdp.ConsumeUnicodeNoSurrogates(1000)
    str_2= fdp.ConsumeUnicodeNoSurrogates(1000)

    try:
        parse(str_1, str_2)
    except ValueError:
        pass
    except URLError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()