from mrjob.job import MRJob
from mrjob.step import MRStep
import simplejson as json

class MRPreprocessing(MRJob):

    def mapper(self, _, line):
        obj = json.loads(line)

        output = {}

        output['text'] = obj['text']
        output['useful'] = obj['votes']['useful'] > 0

        yield ('', output)

def make_json(filename):
    with file(filename) as f:
        lines = f.read().split('\n')
        for i in range(len(lines) - 2):
            lines[i] = lines[i].replace('""\t','')
            lines[i] = lines[i] + ','
        lines[0] = '[' + lines[0]
        lines[len(lines)-1] = ''
        lines[len(lines)-2] = lines[len(lines)-2].replace('""\t', '')+ ']'


    with file(filename, 'w') as f:
        f.write("\n".join(lines))

if __name__ == '__main__':
    MRPreprocessing.run()
    make_json('output.txt')
