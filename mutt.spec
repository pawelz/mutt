Summary:	The Mutt Mail User Agent
Summary(de):	Der Mutt Mail-User-Agent 
Summary(fr):	Agent courrier Mutt
Summary(pl):	Program pocztowy Mutt
Summary(tr):	Mutt elektronik posta program�
Name:		mutt
Version:	0.96.4
Release:	1i
Copyright:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source0:	ftp://riemann.iam.uni-bonn.de/pub/mutt/%{name}-%{version}i.tar.gz
Source1:	mutt.wmconfig
Source2:	Muttrc
Patch:		mutt-mail.patch
URL:		http://www.mutt.org/
Requires:	smtpdaemon
Requires:	mailcap
Buildroot:	/tmp/%{name}-%{version}-root

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
%patch -p0

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
%configure \
	--with-sharedir=%{_datadir} \
	--sysconfdir=/etc \
	--enable-pop \
	--enable-imap \
	--with-curses \
	--disable-warnings \
	--disable-domain \
        --enable-compressed \
	--with-docdir=$RPM_BUILD_ROOT%{_datadir}/doc/mutt-%{version}

make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/mutt
install %{SOURCE2} $RPM_BUILD_ROOT/etc/Muttrc

gzip -9nf		$RPM_BUILD_ROOT%{_mandir}/man1/* \
			contrib/{*rc,*cap} \
			ChangeLog README TODO NEWS README.SECURITY

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {ChangeLog,README,TODO,NEWS,README.SECURITY}.gz

%config(noreplace) %verify(not size md5 mtime) /etc/Muttrc
%config(missingok) /etc/X11/wmconfig/mutt

%attr(0755,root,root) %{_bindir}/*
%lang(en) %{_mandir}/man*/*
