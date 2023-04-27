import argparse
import os
import sys

#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

def exit_error(message, exit_on_error=True):
    '''Print error message and (optionally) exit'''
    print('exit_error: ' + message)
    if exit_on_error:
        sys.exit(-1)

#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

if __name__ == "__main__":
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument("--build", dest="build", help="Test build", action='store_true', default=False)
    parser.add_argument("--run-test", dest="run_test", help="Run test", action='store_true', default=False)
    args = parser.parse_args(sys.argv[1:])

    if args.build and args.run_test:
        exit_error('Choose only --build OR --run-test')
    elif args.build:
        print('Build selected')
    elif args.run_test:
        print('Run test selected')
    else:
        exit_error('Missing action to perform')

    print('Environment:')
    print('-------------------------------------------------------------')
    print('{}'.format(os.environ))
    print('-------------------------------------------------------------')

    sys.exit(0)

#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////
