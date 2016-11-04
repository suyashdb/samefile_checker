# Example package with a console entry point
import filecmp
import glob, os

def check_same_files(dataset):
    all_files_dataset = glob.glob(os.path.join(dataset, '**/*.nii.gz'), recursive=True)
    for a, b in itertools.combinations(all_files_dataset, 2):
        if filecmp.cmp(a, b) is True:
            print("File A:", a, " is same as File B: ", b)


# def main():
#     check_same_files()
#     print "Hello World"



def main():
    class MyParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    parser = MyParser(
        description="BIDS to NDA converter.",
        fromfile_prefix_chars='@')
    # TODO Specify your real parameters here.
    parser.add_argument(
        "dataset",
        help="BIDS dataset location",
        metavar="dataset")
    args = parser.parse_args()
    check_same_files(dataset)
    print "Done"
