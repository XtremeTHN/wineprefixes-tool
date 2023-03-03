import argparse, os, glob, sys

parser = argparse.ArgumentParser("wineprefixes tool", "wineprefixes 0.0", "Herramienta para manipular directorios de windows emulados (wineprefixes)")

parser.add_argument("-g", "--get", action="store", dest="get", 
                    metavar="PREFIX")
parser.add_argument("-l", "--list", action="store_true", dest="ls")

parser.add_argument("-gp", "--get-path", action="store_true", 
                    dest="gpath")
parser.add_argument("-sp", "--set-path", action="store", dest="path", 
                    metavar="path")
parser.add_argument("-n", "--new", action="store", dest="new", 
                    metavar="NAME")
parser.add_argument("-rm", "--remove", action="store", dest="rm", 
                    metavar="PREFIX")

obj = parser.parse_args()
home = os.getenv("HOME")
path_prefix = os.path.join(os.getenv("HOME"), '.local', 'share', 'wineprefixes')
if obj.path != None:
    path_prefix = obj.path

if not os.path.exists(path_prefix):
    os.system(f"mkdir -p {path_prefix}")

if obj.gpath:
    print(path_prefix)
    sys.exit(0)

if obj.ls:
    print(glob.glob(path_prefix + '/*'))
    sys.exit(0)

if obj.get != None:
    prefixes = glob.glob(path_prefix + "/*")
    # Salir si no hay ninguna carpeta
    if len(prefixes) < 0:
        sys.exit(1)
    for x,v in enumerate(prefixes):
        if not os.path.isdir(v):
            prefixes.remove(x)
    # Salir si solo se encontraron archivos
    if len(prefixes) < 0:
        sys.exit(2)
    
    for x in prefixes:
        if obj.get == os.path.basename(x):
            print(x)
            sys.exit(0)
    sys.exit(3)

if obj.new != None:
    os.system(f'mkdir -p {os.path.join(path_prefix,obj.new)}')

if obj.rm != None:
    from shutil import rmtree
    rmtree(os.path.join(path_prefix,obj.rm))
