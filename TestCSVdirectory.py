import os,glob
import SimpleCSVReporter,IndentMessages



def set_specific_paths():
    datadir = "/Users/margery/Documents/pystuff/pyGotham/demo/data/bigtest/"
    inputdir = "input"
    outputdir = "output"
    wildcard_csv = "*.csv"
    out_dir = os.path.join(datadir,outputdir)
    in_dir = os.path.join(datadir,inputdir,wildcard_csv)
    return in_dir,out_dir

def test_csv(inpath, outpath, line_width=0):
    """
    Test SimpleCSVReporter for input CSV
    :param inpath: path to input CSV file
    :param outpath: path to output report text
    :param line_width: desired report line-width
    """
    test = SimpleCSVReporter.SimpleCSVReporter()
    test.readCSV(inpath)
    indent_tool = IndentMessages.IndentMessages()
    if line_width > 0:
        indent_tool.total_width = line_width
    output = open(outpath, 'w')
    test.report_fd = output
    test.indenter = indent_tool
    test.default_report()
    output.close()

def test_dir():
    in_dir,out_dir = set_specific_paths()
    print in_dir,out_dir
    for csv_path in glob.glob(in_dir):
        csv = os.path.basename(csv_path)
        name = os.path.splitext(csv)[0]
        report_name=name + "_report.txt"
        report_path = os.path.join(out_dir,report_name)
        print 'from {0:s} to {1:s}'.format(csv,report_name)
        test_csv(csv_path, report_path, 80)

test_dir()

