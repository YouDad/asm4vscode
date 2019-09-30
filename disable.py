import sys
import os

DEBUG = True

def get_filename(path):
	filename = path

	if filename[-4:] != ".asm":
		print("需要asm作为文件名后缀")
		sys.exit(-1)

	filename = filename.split("\\")[-1][:-4]

	if len(filename) > 8:
		print("文件名不能大于8个字符")
		sys.exit(-1)

	if DEBUG:
		print("get_filename success, return %s" % filename)
	return filename

def chr_path():
	pwd = os.path.split(os.path.realpath(__file__))[0]

	os.chdir(pwd)
	if DEBUG:
		print("chr_path success, return %s" % pwd)
	return pwd

def set_path(pwd):
	os.environ["PATH"] += ";%s\\MASM" % pwd
	os.environ["PATH"] += ";%s\\EXE" % pwd
	os.environ["PATH"] += ";%s\\DOSBOX" % pwd

def make_asm(file):
	ret = os.system("MASM.EXE SRC\\%s.asm %s.obj" % (file, file))
	if ret != 0:
		sys.exit(ret)
	if DEBUG:
		print("make_asm success")

def link_asm(file):
	ret = os.system("LINK.EXE %s.obj;" % file)
	if ret != 0:
		sys.exit(ret)

	ret = os.system("del %s.obj" % file)
	if ret != 0:
		sys.exit(ret)
	if DEBUG:
		print("link_asm success")

def list_asm(file):
	ret = os.system("MASM.EXE SRC\\%s.asm,,SRC\\list.lst" % file)
	if ret != 0:
		sys.exit(ret)

	ret = os.system("del %s.obj" % file)
	if ret != 0:
		sys.exit(ret)
	if DEBUG:
		print("list_asm success")

def move_exe(file):
	ret = os.system("move /Y %s.exe EXE\\%s.exe" % (file, file))
	if ret != 0:
		sys.exit(ret)
	if DEBUG:
		print("move_exe success")

def set_conf(pwd, file, is_debug):
	conf = "%s\\AppData\\Local\\DOSBox\\dosbox-0.74.conf" % os.environ["UserProfile"]

	ret = os.system("copy /Y %s\\DOSBOX\\DosBoxConfig.conf %s" % (pwd, conf))
	if ret != 0:
		sys.exit(ret)
	
	with open(conf, "a") as f:
		debug_str = "debug" if is_debug else ""
		f.write("mount C %s\\EXE\nC:\n%s %s.exe" % (pwd, debug_str, file))

	ret = os.system("start /w DOSBOX -noconsole")
	if ret != 0:
		sys.exit(ret)

	ret = os.system("copy /Y %s\\DOSBOX\\DosBoxConfig.conf %s" % (pwd, conf))
	if ret != 0:
		sys.exit(ret)
	if DEBUG:
		print("set_conf success")

def new_asm(file):
	with open("SRC\\%s.asm" % file, "w") as f:
		f.writelines([
			"datas segment\n",
			"    string DB 'Hello World!',13,10,'$'\n",
			"datas ends\n",
			"\n",
			"codes segment\n",
			"    assume cs:codes,ds:datas\n",
			"main:\n",
			"    mov ax,datas\n",
			"    mov ds,ax\n",
			"\n",
			"    lea dx,string\n",
			"    mov ah,09h\n",
			"    int 21h\n",
			"\n",
			"    mov ah,4ch\n",
			"    int 21h\n",
			"codes ends\n",
			"end main\n",
		])

def main(cmd, pathname):
	file = get_filename(pathname)
	pwd = chr_path()
	set_path(pwd)

	if cmd == "new":
		file = input("请输入新文件名,无后缀:")
		new_asm(file)
		sys.exit(0)

	if cmd == "list":
		list_asm(file)
		sys.exit(0)

	make_asm(file)
	link_asm(file)

	if cmd == "make":
		sys.exit(0)

	move_exe(file)
	set_conf(pwd, file, cmd == "debug")

main(sys.argv[1], sys.argv[2])