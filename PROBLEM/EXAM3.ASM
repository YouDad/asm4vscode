dseg    segment
ral     db      ?
htab	db	'0123456789ABCDEF'
dseg    ends
cseg    segment
        assume  cs:cseg,ds:dseg
start:  mov     ax,dseg
        mov     ds,ax
        mov     ah,01h		;�����һ����
        int     21h
        sub     al,30h
        mov     bl,al
        mov     dl,'+'		;��ʾ�Ӻ�
        mov     ah,02h
        int     21h
        mov     ah,01h		;����ڶ�����
        int     21h
        sub     al,30h
        add     bl,al
        mov     ral,bl		;��������ral��Ԫ
        mov     dl,'='		;��ʾ��=����
        mov     ah,02h
        int     21h
        mov     al,bl       ;al=a+b
        mov	    ch,bl       ;ch=a+b
        mov	    cl,4
        shr	    al,cl       ;al/=16
        lea	    bx,htab     ;bx=&htab
        xlat                ;al=bx[al]
        mov	    dl,al		;��ʾ���ʮλ�ϵ���
        mov	    ah,02h
        int	    21h
        and	    ch,0fh      ;ch%=16
        mov	    al,ch       ;al=ch
        xlat
        mov	    dl,al
        mov	    ah,02h
        int	    21h
        mov     dl,'h'		;��ʾ�ַ���h��
        mov     ah,02h
        int     21h
        mov     ah,4ch
        int     21h
cseg    ends
        end     start