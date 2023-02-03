import argparse, os, glob, sys

parser = argparse.ArgumentParser("wineprefixes tool", "wineprefixes 0.0", "Herramienta para manipular directorios de windows emulados (wineprefixes)")

parser.add_argument("-g", "--get", action="store", dest="get", metavar="PREFIX")
parser.add_argument("-rm", "--remove", action="store", dest="rm", metavar="PREFIX")

obj = parser.parse_args()
home = os.getenv("HOME")
path_prefix = os.path.join(os.getenv("HOME"), '.local', 'share', 'wineprefixes')

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