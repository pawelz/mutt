.\" -*-nroff-*-
.\"
.\"
.\"     Copyright (C) 1996-2000 Michael R. Elkins <me@cs.hmc.edu>
.\"
.\"     This program is free software; you can redistribute it and/or modify
.\"     it under the terms of the GNU General Public License as published by
.\"     the Free Software Foundation; either version 2 of the License, or
.\"     (at your option) any later version.
.\"
.\"     This program is distributed in the hope that it will be useful,
.\"     but WITHOUT ANY WARRANTY; without even the implied warranty of
.\"     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
.\"     GNU General Public License for more details.
.\"
.\"     You should have received a copy of the GNU General Public License
.\"     along with this program; if not, write to the Free Software
.\"     Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111, USA.
.\"
.\"     {PTM/TW/0.1/30-06-1999/"agent pocztowy u�ytkownika"}
.\"     Translation (c) 1999 Tomasz Wendlandt <juggler@cp.pl>.
.\" transl.updated: PTM/WK/2000-VI
.TH mutt 1 "luty 2000" Unix "podr�cznik u�ytkownika"
.SH NAZWA
mutt - agent pocztowy u�ytkownika (MUA)
.SH SK�ADNIA
.TP 6
.B mutt
.RB [ -hnpRvxyzZ ]
.RB [-a
.IR plik ]
.RB [ -b
.IR adres ]
.RB [ -c
.IR adres ]
.br
.RB [ -e
.IR polecenie ]
.RB [-f
.IR skrzynka ]
.RB [ -F
.IR muttrc ]
.RB [ -H
.IR szkic ]
.br
.RB [ -i
.IR za��cznik ]
.RB [ -m
.IR typ ]
.RB [ -s
.IR temat ]
.SH OPIS
.PP
Mutt jest ma�ym, lecz bardzo silnym programem tekstowym, przeznaczonym do
czytania poczty elektronicznej pod systemem operacyjnym unix, posiada takie
funkcje jak kolorowy terminal, MIME i w�tkowanie.
.SH OPCJE
.TP
.BI -a " plik"
Za��cza plik do twojej wiadomo�ci u�ywaj�c MIME.
.TP
.BI -b " adres"
Okre�la odbiorc� �lepej kopii wiadomo�ci (BCC).
.TP
.BI -c " adres"
Okre�la odbiorc� kopii wiadomo�ci (CC).
.TP
.BI -e " polecenie"
Okre�la polecenie konfiguracyjne, kt�re ma by� wykonane po inicjalizacji.
.TP
.BI -f " skrzynka"
Okre�la, kt�r� skrzynk� pocztow� wczyta�.
.TP
.BI -F " muttrc"
Okre�la plik inicjalizacji, kt�ry ma by� u�yty zamiast ~/.muttrc
.TP
.BI "-h"
Wy�wietla pomoc.
.TP
.BI -H " szkic"
Okre�la plik ze szkicem zawieraj�cy nag��wek i tre�� wiadomo�ci,
kt�re b�d� u�yte do wys�ania wiadomo�ci.
.TP
.BI -i " za��cznik"
Okre�la plik do w��czenia w tre�� wiadomo�ci.
.TP
.BI -m " typ"
Okre�la domy�lny typ skrzynki pocztowej.
.TP
.B -n
Sprawia, i� Mutt pomija og�lnosystemowy plik konfiguracyjny.
.TP
.B -p
Ponownie otwiera zarzucony list.
.TP
.B -R
Otwiera skrzynk� w trybie tylko do odczytu.
.TP
.BI -s " temat"
Okre�la temat wiadomo�ci.
.TP
.B -v
Wy�wietla wersj� Mutt'a i wkompilowane parametry.
.TP
.B -x
Symuluje tryb tworzenia wiadomo�ci mailx.
.TP
.BI -y
Uruchamia Mutt'a z list� wszystkich skrzynek pocztowych okre�lonych
poleceniem \fBmailboxes\fP.
.TP
.B -z
Kiedy jest u�ywane z \fB-f\fP, powoduje i� Mutt nie uruchamia si� je�eli
w skrzynce nie ma �adnych wiadomo�ci.
.TP
.B -Z
Powoduje, i� Mutt otwiera pierwsz� zawieraj�c� now� wiadomo�� skrzynk�
spo�r�d okre�lonych przez polecenie \fBmailboxes\fP.
.SH �RODOWISKO
.TP
.B EDITOR
Edytor wywo�ywany podczas komponowania wiadomo�ci.
.TP
.B HOME
Pe�na �cie�ka do katalogu domowego u�ytkownika.
.TP
.B MAIL
Pe�na �cie�ka do katalogu buforowania skrzynki u�ytkownika.
.TP
.B MAILCAPS
�cie�ka przeszukiwania dla plik�w mailcap.
.TP
.B MM_NOASK
Je�eli ta zmienna jest ustawiona, to mailcap s� zawsze u�ywane uprzedniego
pytania.
.TP
.B PGPPATH
Katalog, w kt�rym znajduje si� p�k kluczy PGP (keyring) u�ytkownika.
.TP
.B TMPDIR
Katalog, w kt�rym tworzone s� pliki tymczasowe.
.TP
.B REPLYTO
Standardowy adres, na kt�ry maj� by� odsy�ane odpowiedzi na wys�an� przez
u�ytkownika poczt�.
.TP
.B VISUAL
Edytor wywo�ywany kiedy we wbudowanym edytorze podane jest polecenie ~v.
.SH PLIKI
.IP "~/.muttrc"
Plik konfiguracyjny u�ytkownika.
.IP "/etc/Muttrc"
Og�lnosystemowy plik konfiguracyjny.
.IP "/tmp/muttXXXXXX"
Pliki tymczasowe tworzone przez Mutt'a.
.IP "~/.mailcap"
Definicja u�ytkownika do obs�ugi nietekstowych typ�w MIME.
.IP "/etc/mailcap"
Definicja systemu do obs�ugi nietekstowych typ�w MIME.
.IP "~/.mime.types"
Osobiste mapowanie u�ytkownika pomi�dzy typem MIME i rozszerzeniami pliku.
.IP "/etc/mime.types"
Mapowanie systemowe pomi�dzy typem MIME i rozszerzeniami pliku.
.IP "/usr/local/bin/mutt_dotlock"
Uprzywilejowany program do dotlockingu.
.SH B��DY
Zawieszenie/wznawianie pracy podczas edytowania pliku za pomoc� edytora
zewn�trznego nie dzia�a pod SunOS 4.x, je�eli u�ywasz bibliotek curses
w /usr/5lib. Jednak�e \fIdzia�a\fP to z bibliotekami S-Lang.
.PP
Zmiana wielko�ci ekranu podczas korzystania z zewn�trznego pagera powoduje,
i� Mutt fiksuje na niekt�rych systemach.
.PP
Zawieszenie/wznawianie nie dzia�a pod Ultrix.
.PP
Linia help dla menu nie jest uaktualniana, je�eli zmienisz powi�zania dla
jednej z pokazanych w niej funkcji podczas pracy z Muttem.
.SH BRAK GWARANCJI
Niniejszy program rozpowszechniany jest z nadziej�, i� b�dzie on u�yteczny
\-\- jednak BEZ JAKIEJKOLWIEK GWARANCJI, nawet domy�lnej gwarancji
PRZYDATNO�CI HANDLOWEJ albo PRZYDATNO�CI DO OKRE�LONYCH ZASTOSOWA�.
W celu uzyskania bli�szych informacji - Powszechna Licencja Publiczna GNU.
.SH ZOBACZ TAK�E
.BR muttrc (5),
.BR curses (3),
.BR mutt_dotlock (1),
.BR ncurses (3),
.BR sendmail (1),
.BR smail (1),
.BR mailcap (5)
.PP
Strona domowa Mutt'a: http://www.mutt.org/
.PP
Powszechna Licencja Publiczna GNU (The GNU General Public License).
.SH AUTOR
Michael Elkins i inni. Skorzystaj z <mutt-dev@mutt.org> by skontaktowa�
si� z tw�rcami.
