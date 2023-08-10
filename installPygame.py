import subprocess

def installPygame():
	subprocess.Popen(['pip', 'install', 'pygame'], stdout=sys.stdout, stderr=sys.stdout)