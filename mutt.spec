Summary:     The Mutt Mail User Agent
Summary(de): Der Mutt Mail-User-Agent 
Summary(fr): Agent courrier Mutt
Summary(pl): Program pocztowy Mutt
Summary(tr): Mutt elektronik posta program�
Name:        mutt
Version:     0.95
Release:     3d
Copyright:   GPL
Group:       Applications/Mail
Group(pl):   Aplikacje/Poczta
Source0:     ftp://riemann.iam.uni-bonn.de/pub/mutt/%{name}-%{version}i.tar.gz
Source1:     %{name}.wmconfig
Source2:     Muttrc
Source3:     %{name}.pl.po
Patch0:	     %{name}-mail.patch
Patch1:      %{name}-pl.patch
URL:         http://www.mutt.org/
Requires:    smtpdaemon
Buildroot:   /tmp/%{name}-%{version}-root

%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de
Mutt ist ein kleiner aber leistungsf�higer Vollbild-Mail-Client f�r Unix mit
MIME-Unterst�tzung, Farbe, POP3-Unterst�tzung, Nachrichten-Threading,
zuweisbaren Tasten und Sortieren nach Threads.

%description -l pl
Mutt jest niewielkim programem pocztowym dla terminali tekstowych
posiadaj�cym du�e mo�liwo�ci. Obs�uguje MIME, POP3, cztery formaty
skrzynek pocztowych, obs�uguje kolory, w�tki i ocen� wa�no�ci list�w
(scoring).  W tej wersji dodano tak�e obs�ug� skompresowanych folder�w.

%description -l fr
mutt est un client courrier Unix plein �cran, petit mais tr�s puissant.
Il dispose de la gestion MIME, des couleurs, de la gestion POP, des fils
de discussion, des touches li�es et d'un mode de tri sur les fils.

%description -l tr
Mutt, k���k ama �ok g��l� bir tam-ekran Unix mektup istemcisidir. MIME deste�i,
renk ve POP3 deste�i i�erir.

%prep
%setup -q 
%patch0 -p0
%patch1 -p0

install %{SOURCE3} $RPM_BUILD_DIR/%{name}-%{version}/po/pl.po

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/slang" LDFLAGS=-s \
        ./configure \
	--prefix=/usr \
	--with-sharedir=/etc \
	--enable-pop \
	--enable-imap \
	--with-slang \
	--disable-warnings \
	--disable-domain \
        --enable-compressed \
	--with-docdir=$RPM_BUILD_DIR/%{name}-%{version}/rpm_docs 

make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make prefix=$RPM_BUILD_ROOT/usr sharedir=$RPM_BUILD_ROOT/etc install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/mutt
install %{SOURCE2} $RPM_BUILD_ROOT/etc/Muttrc

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*
gzip -9nf contrib/{*rc,*cap} rpm_docs/{html/*,*.txt,ChangeLog,README,TODO,NEWS}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc contrib/*.gz rpm_docs/{html,*.gz}

%config(noreplace) %verify(not size md5 mtime) /etc/Muttrc
%config(missingok) /etc/X11/wmconfig/mutt

%attr(0711,root,root) /usr/bin/mutt
%attr(2711,root,mail) /usr/bin/mutt_dotlock

%lang(en) %attr(644,root, man) /usr/man/man1/*

%lang(en) /usr/share/locale/de/LC_MESSAGES/mutt.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/mutt.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/mutt.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/mutt.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/mutt.mo
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/mutt.mo
%lang(uk) /usr/share/locale/uk/LC_MESSAGES/mutt.mo

%changelog
* Thu Feb 10 1999 Micha� Kuratczyk <kurkens@polbox.com>
  [0.95i-3d]
- added gzipping documentation
- simplification in %files
- cosmetic changes

* Mon Dec 14 1998 Marcin Korzonek <mkorz@shadow.eu.org>
[0.95i-1]
- remove patch for compressed folders (not available yet)
- added %%lang macros
- added some missing doc files
- locale files included

* Sat Sep 19 1998 Marcin Korzonek <mkorz@shadow.eu.org>
[0.93.2i-1d]
- added pl translation,
- added patch for compressed folders,
- rewrites system Muttrc based on ones from Roland Rosenfeld.

* Sun Sep  6 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
[0.93.2i-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using %{SOURCE#} macro in %install,
- changed base Source Url to ftp://riemann.iam.uni-bonn.de/pub/mutt/.

* Wed Jul 29 1998 Bill Nottingham <notting@redhat.com>
- fix setgid removal
- spec file comsetics

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- security fix
- turn off setgid mail.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.91.1

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to mutt-0.89.1

* Thu Oct 16 1997 Otto Hammersmith <otto@redhat.com>
- Updated to mutt 0.85.
- added wmconfig entries.
- removed mime.types

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- Rebuilt to insure all sources were fresh and patches were clean.

* Wed Aug 6 1997 Manoj Kasichainula <manojk@io.com>
 - Initial version for 0.81(e)
