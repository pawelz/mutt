Summary:	The Mutt Mail User Agent
Summary(de):	Der Mutt Mail-User-Agent 
Summary(fr):	Agent courrier Mutt
Summary(pl):	Program pocztowy Mutt
Summary(tr):	Mutt elektronik posta program�
Name:		mutt
Version:	1.3.17i
Release:	1
Epoch:		4
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplica��es/Correio Eletr�nico
Source0:	ftp://ftp.mutt.org/pub/mutt/devel/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.mutt.org/
Requires:	smtpdaemon
Requires:	mailcap
Requires:	iconv
BuildRequires:	iconv
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de
Mutt ist ein kleiner aber leistungsf�higer Vollbild-Mail-Client f�r
Unix mit MIME-Unterst�tzung, Farbe, POP3-Unterst�tzung,
Nachrichten-Threading, zuweisbaren Tasten und Sortieren nach Threads.

%description -l fr
mutt est un client courrier Unix plein �cran, petit mais tr�s
puissant. Il dispose de la gestion MIME, des couleurs, de la gestion
POP, des fils de discussion, des touches li�es et d'un mode de tri sur
les fils.

%description -l pl
Mutt jest niewielkim programem pocztowym dla terminali tekstowych
posiadaj�cym du�e mo�liwo�ci. Obs�uguje MIME, POP3, cztery formaty
skrzynek pocztowych, kolory, w�tki, ocen� wa�no�ci list�w (scoring)
oraz skompresowane foldery.

%description -l tr
Mutt, k���k ama �ok g��l� bir tam-ekran Unix mektup istemcisidir. MIME
deste�i, renk ve POP3 deste�i i�erir.

%prep
%setup -q -n %{name}-%(echo %{version} | sed 's/i$//')

%build
aclocal -I m4
automake -a -c
autoheader
autoconf
%configure \
	--with-curses \
	--with-regex \
	--with-homespool=Maildir \
	--with-mailpath=/var/mail \
	--enable-external-dotlock \
	--with-sharedir=%{_datadir} \
	--with-iconv \
	--with-docdir=%{_defaultdocdir}/%{name}-%{version} \
	--enable-pop \
	--enable-imap \
	--with-ssl \
	--with-sasl \
	--disable-debug \
	--disable-warnings \
	--enable-mailtool \
	--without-included-nls

%{__make} keymap.h
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf contrib/{*rc*,*cap*} \
	ChangeLog README TODO NEWS README.SECURITY README.SSL README.UPGRADE

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz contrib/{*rc*,*cap*} doc/manual*html
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/Muttrc
%attr(755,root,root) %{_bindir}/mutt
%attr(755,root,root) %{_bindir}/flea
%attr(755,root,root) %{_bindir}/muttbug
%attr(755,root,root) %{_bindir}/pgp*
%attr(2754,root,mail) %{_bindir}/mutt_dotlock

%{_applnkdir}/Network/Mail/mutt.desktop
%{_pixmapsdir}/mutt.png
%{_mandir}/man*/*
