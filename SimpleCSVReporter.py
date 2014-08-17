__author__ = 'margery'

import csv,os
import collections
import IndentMessages



class SimpleCSVReporter:
    def __init__(self):
        self.count_of_values = collections.Counter()
        self.possible_values = dict()
        self.possible_tuples = dict()
        self.headers = None
        self.report_fd = None
        self.indenter = None
        self.total_levels = 0

    def readCSV(self, path):
        with open(path) as f:
            r = csv.DictReader(f)
            self.headers = (r.fieldnames)
            self.total_levels = len(self.headers)
            for level, head in enumerate(r.fieldnames):
                self.possible_values[head] = set()
                self.possible_tuples[level] = set()

            for row in r:
                combo_list = []
                for level, head in enumerate(r.fieldnames):
                    item = row[head]
                    self.possible_values[head].add(item)
                    self.count_of_values[item] += 1

                    # create tuple for combination count
                    combo_list.append(item)
                    if len(combo_list) > 1:
                        tup = tuple(combo_list)
                        self.count_of_values[tup] += 1
                        self.possible_tuples[level].add(tup)

    # This is a stub for a method that
    #   would look up the value,
    #   or apply some word formatting.
    #   e.g. 'with {0:s}'.format(word)
    def word_message(self, word):
        return word

    # This is also a stub for a more method
    #   that could define a special way
    #   to join the values returned
    #   by word_message
    def combo_message(self, combo):
        """
        :param combo: tuple for returned string
        """
        msg = ' '.join(combo)
        return msg

    # Write to the class-var file descriptor
    def write_line(self, msg):
        self.report_fd.write('{0:s}\n'.format(msg))

    # Uses the class-var IndentMessages object
    def write_indent(self, level, msg, total):
        outmsg = self.indenter.indent_message(level, msg, total)
        self.write_line(outmsg)

    # Here we will use recursion to print indented combo & sums
    def write_sub_levels(self, combo_start):
        level = len(combo_start)
        head = self.headers[level]
        for item in self.possible_values[head]:
            combo = combo_start + (item,)
            if combo in self.possible_tuples[level]:
                total = self.count_of_values[combo]
                msg = self.combo_message(combo)
                self.write_indent(level, msg, total)
                if total > 0 and (level + 1) < self.total_levels:
                    self.write_sub_levels(combo)

    #  Print level 0, pass tuple to recursive method
    def default_report(self):
        head = self.headers[0]
        vset = self.possible_values[head]
        level_one = 0
        for item in vset:
            total = self.count_of_values[item]
            msg = self.word_message(item)
            self.write_indent(level_one, msg, total)
            if total > 0 and (level_one + 1) < self.total_levels:
                self.write_sub_levels((item,))


def test_crime_stats():
    datadir = "/Users/margery/Documents/pystuff/pyGotham/demo/data"
    inputdir = "input"
    outputdir = "output"
    csv_file = 'crime_4_columns.csv'
    report_file = 'crime_report_4c60.txt'
    inpath = os.path.join(datadir, inputdir, csv_file)
    outpath = os.path.join(datadir, outputdir, report_file)
    test_csv(inpath,outpath,60)


def test_csv(inpath, outpath, line_width=0):
    """
    Test SimpleCSVReporter for input CSV
    :param inpath: path to input CSV file
    :param outpath: path to output report text
    :param line_width: desired report line-width
    """
    test = SimpleCSVReporter()
    test.readCSV(inpath)
    indent_tool = IndentMessages.IndentMessages()
    if line_width > 0:
        indent_tool.total_width = line_width
    output = open(outpath, 'w')
    test.report_fd = output
    test.indenter = indent_tool
    test.default_report()
    output.close()


if __name__ == '__main__':
    print "Test SimpleCSVReporter"
    inpath = "simplerCSV.txt"
    outpath= "simple_report.txt"
    test_csv(inpath,outpath,25)

    test_crime_stats()