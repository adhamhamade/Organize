import shutil, os, sys, argparse

extFound = False

parser = argparse.ArgumentParser()

def getArgument(p):
    p.add_argument("--f", help="Directory to read from" , required=True)
    p.add_argument("--t", help="Destination to send to", required=True)
    p.add_argument("--ext", help="Extensions type to select", \
    choices=["pdf", "jpg", "txt", "docx","pptx", "png","exe","zip"], required=True)
    p.add_argument("--operation", help="operation", \
    choices=["move","copy"], required=True)

getArgument(parser)

args = parser.parse_args()


directoryPath = args.f
directoryDest = args.t

os.chdir(directoryPath)


for filename in os.listdir(os.getcwd()):
    if filename.endswith(args.ext):
        print(filename)
        if args.operation == 'move':
            shutil.move(filename, directoryDest)
            extFound = True
        elif args.operation == 'copy':
            shutil.copy(filename, directoryDest)
            extFound = True



if extFound == False:
    print("No files were found for the ext selected")
