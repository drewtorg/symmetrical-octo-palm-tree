from mrjob.job import MRJob
from mrjob.step import MRStep
import simplejson as json
import re
import ntlk

WORD_RE = re.compile(r"[\w']+")


class MRStuff(MRJob):

    def mapper(self, _, line):
        obj = json.loads(line)

        yield (obj['votes']['useful'], 1)

    def reducer(self, count, counts):
        yield count, sum(counts)


if __name__ == '__main__':
    MRStuff.run()
