#!/usr/bin/python3
import atheris
import sys
from urllib.error import URLError

with atheris.instrument_imports():
    from podcastparser import parse

def RandomString(fdp, min_len, max_len):
  str_len = fdp.ConsumeIntInRange(min_len, max_len)
  return fdp.ConsumeUnicodeNoSurrogates(str_len)

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    str_1 = RandomString(fdp, 1, 100)
    str_2= RandomString(fdp, 1, 100)

    try:
        parse(str_1, str_2)
    except ValueError:
        pass
    except URLError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()