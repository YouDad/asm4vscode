var3:
��һ�������ļ�����;:
 ASMPROJECT		--��๤��/���ļ���Ŀ
 ASMSINGLEFILE		--��൥�ļ�
 |- .vscode		--vscode�ļ��� �� �����ļ���
 |- list.lst		--list_asm��Ĭ�����ɵ��б��ļ�
 |- hw.asm		--hello world����
 DOSBOX			--����dosbox�����п�,�������б�������Ŀ�ִ���ļ�
 EXE			--Ĭ�ϱ�������ĳ����ŵ�λ��
 |- DEBUG.EXE		--���ڵ��Ի�����ĳ���
 |- debug_exe.bat	--����һ����ק���Գ���(����exe)
 |- run_and_type.exe	--�������һ����ק���Գ���
 |- run_exe.bat		--����ֱ����dosbox���������
 MASM			--���б����õ��ĳ���(����exe)
 PROBLEM		--�ӻ���������Դ����...(��������ʲô��,��Ҳ��֪��:)
 |- .vscode		--vscode�ļ��� �� �����ļ���
 |- list.lst		--list_asm��Ĭ�����ɵ��б��ļ�
 asmexp.code-workspace	--vscode�Ĺ������ļ�
 debug_asm.bat		--����һ�����Ա��������(����asm)
 list_asm.bat		--����һ�����ɱ�����Դ������б��ļ�(����asm)
 make_asm.bat		--����һ�����뱻�����Դ����(����asm)
 new_asm.bat		--��������һ������helloworld���̵�asm�ļ�
 readme_ver3.txt	--�����ļ� ����:Karl ��ʲôbug��ͶPSR�����ļ�(���аٶ�)�� 1632083718@qq.com
 run_asm.bat		--����һ������ִ�б������Դ����(����asm)

var4:
�ı�new_asm.bat,��������:����asm�ļ����ֲ��ܳ���8λ
ԭ��:dosbox����ʶ�𳬹�8λ���ļ���,�����ڴ���ʱ�����ƿ��Ա����������

var5:2018��5��5��02:02:07
1.һ��ȫ�µĸ���,��������:��Ҳ����debug_asm֮����q�˳���debug exe��.
2.������callģʽ���������д,ʹ�ô���ṹ��������
3.run_and_type.exe������
4.debug_exe.bat������
5.����dosbox��conf�ļ�,��dosbox�ļ�����
6.ASMPROJECT������,����û���õ�
�ļ��ṹ����Ϊ:
 ASMSINGLEFILE		--��൥�ļ�
 |- .vscode		--vscode�ļ��� �� �����ļ���
 |- list.lst		--list_asm��Ĭ�����ɵ��б��ļ�
 |- hw.asm		--hello world����
 DOSBOX			--����dosbox�����п�,�������б�������Ŀ�ִ���ļ�
 |- DOSBox.exe		--DOSBox������
 |- DosBoxConfig.conf	--DOSBox�����ļ�
 |- SDL.dll		--DOSBox���п�
 |- SDL_net.dll		--DOSBox���п�
 EXE			--Ĭ�ϱ�������ĳ����ŵ�λ��
 |- DEBUG.EXE		--���ڵ��Ի�����ĳ���
 |- hw.exe		--hello world��ִ�г���
 |- run_exe.bat		--����ֱ����dosbox���������(����exe)
 MASM			--���б����õ��ĳ���
 |- LINK.EXE		--���ӳ���
 |- MASM.EXE		--�������
 |- ML.ERR		--��������ļ�
 |- ml.exe		--��LINK.EXE���õĳ���
 PROBLEM		--�ӻ���������Դ����...(��������ʲô��,��Ҳ��֪��:)
 |- .vscode		--vscode�ļ��� �� �����ļ���
 |- list.lst		--list_asm��Ĭ�����ɵ��б��ļ�
 |- EXAM**.ASM		--����**����
 asm.code-workspace	--vscode�Ĺ������ļ�
 debug_asm.bat		--����һ�����Ա��������(����asm)
 get_filename.bat	--����ļ������ӳ���
 list_asm.bat		--����һ�����ɱ�����Դ������б��ļ�(����asm)
 make_asm.bat		--����һ�����뱻�����Դ����(����asm)
 new_asm.bat		--��������һ������helloworld���̵�asm�ļ�
 readme_ver5.txt	--�����ļ� ����:Karl ��ʲôbug��ͶPSR�����ļ�
			--(���аٶ�)�� 1632083718@qq.com
 run_asm.bat		--����һ������ִ�б������Դ����(����asm)
 run_dosbox.bat		--���ڴ�dosbox���ӳ���
 set_path.bat		--�������û����������ӳ���

var6:2018��5��5��16:38:48		!��ʱȷ����һ�������հ�!
1.�Ż�dosbox�򿪲���
2.new_asmʱ������dubug��Ϊ�ļ����½���.��ֹ����DEBUG.EXE
3.�������ж�˵���ļ���ascii����ձ�
4.ASMSINGLEFILE�ļ�������ΪSRC,��������
5.�޸���֮ǰPROBLEM�ļ�����Ļ�಻�ܴ򿪴���
6.�ָ��˿���������debug_exe.bat
7.�޸����ļ�����:ȫ��д��ĸ���ɵ��ļ����ļ����Ǳ�����ļ����ļ���
  ɾ������ܻ��в���Ԥ֪�Ĵ������(������.vscode�ļ��м����ڲ��ļ�)
�ļ��ṹ����Ϊ:
 SRC			--��൥�ļ�
 |- .vscode		--vscode�ļ��е������ļ���
 |- list.lst		--list_asm��Ĭ�����ɵ��б��ļ�
 |- hw.asm		--hello world����
 DOSBOX			--����dosbox�����п�,�������б�������Ŀ�ִ���ļ�
 |- DOSBox.exe		--DOSBox������
 |- DosBoxConfig.conf	--DOSBox�����ļ�
 |- SDL.dll		--DOSBox���п�
 |- SDL_net.dll		--DOSBox���п�
 EXE			--Ĭ�ϱ�������ĳ����ŵ�λ��
 |- DEBUG.EXE		--���ڵ��Ի�����ĳ���
 |- hw.exe		--hello world��ִ�г���
 |- run_exe.bat		--����ֱ����dosbox���������(����exe)
 MASM			--���б����õ��ĳ���
 |- LINK.EXE		--���ӳ���
 |- MASM.EXE		--�������
 |- ML.ERR		--��������ļ�
 |- ML.EXE		--��LINK.EXE���õĳ���
 PROBLEM		--�ӻ���������Դ����...(��������ʲô��,��Ҳ��֪��:)
 |- .vscode		--vscode�ļ��� �� �����ļ���
 |- list.lst		--list_asm��Ĭ�����ɵ��б��ļ�
 |- EXAM**.ASM		--����**����
 ASM.CODE-WORKSPACE	--vscode�Ĺ������ļ�
 DEBUG_ASM.BAT		--����һ�����Ա��������(����asm)
 GET_FILENAME.BAT	--����ļ������ӳ���
 LIST_ASM.BAT		--����һ�����ɱ�����Դ������б��ļ�(����asm)
 MAKE_ASM.BAT		--����һ�����뱻�����Դ����(����asm)
 NEW_ASM.BAT		--��������һ������helloworld���̵�asm�ļ�
 readme_ver6.txt	--�����ļ� ����:Karl ��ʲôbug��ͶPSR�����ļ�
			--(���аٶ�)�� 1632083718@qq.com
 RUN_ASM.bat		--����һ������ִ�б������Դ����(����asm)
 RUN_DOSBOX.bat		--���ڴ�dosbox���ӳ���
 SET_PATH.bat		--�������û����������ӳ���